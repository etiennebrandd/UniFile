from flask import Flask, render_template, request, redirect, url_for, session
import dataAccess
import calendarAPI

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')
app.secret_key = "4d148eb6ddb34438a07fcb3d3c054bc9"


# Routes

############################################################
## Route logic for landing page
############################################################
@app.route('/', methods = ['GET', 'POST'])
def index():
    # If route receives a POST request (a user has registered)
    if request.method == 'POST':

        # Call the register method and return the inserted row count
        registered, id = dataAccess.dbRegister(request.form)

        # If false returned, signup failed - redirect to registration form
        if registered == False:
            return render_template('index.html', message = "Registration failed. Please try again")

        # # If true returned, signup successful, return dashboard
        else:
            return redirect(url_for('dashboard', user = id))

    else:
        return render_template('index.html', message = "")


############################################################
## Route logic for when login button is clicked
############################################################
@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':

        loggedIn, id = dataAccess.dbLogin(request.form)  

        if loggedIn == False:
            return redirect(url_for('index'))

        else:
            session["userID"] = id
            print("Login: ", session["userID"])
            return redirect(url_for('dashboard', user = id))


############################################################
## Route logic for dashboard page
############################################################
@app.route('/dashboard')
def dashboard():

    print("Dash: ", session["userID"])

    if session["userID"]:

        user = dataAccess.dbRetrieveUserByID(request.args.get('user'))
        return render_template('pages/dashboard.html', firstName = user["firstName"], liUser = user["id"])
    
    else: return redirect(url_for('index'))


############################################################
## Route logic for calendar page
############################################################
@app.route('/calendar', methods = ['GET', 'POST'])
def calendar():

    if not request.args:
        return redirect(url_for('index'))
        

    # Retrive a users ID
    user = dataAccess.dbRetrieveUserByID(request.args.get("user"))

    # Retrieve access token or direct user through auth flow
    try:
        auth = calendarAPI.apiOAuth(request.args.get("user"))
        cal = calendarAPI.calendarListGet(auth, "primary")

    except:
        print("** ERROR: OAUTH AUTHENTICATION FAILED **")


    if request.method == "POST":

        # Retrive query params
        args = request.args.to_dict()
        
        # If request to create event
        if args["action"] == "createEvent":
            
            GMTOffset = '+01:00'

            # Retrieve event creation form data
            data = request.form

            # Create event object using form data
            eventData = {
                "summary": data["summary"],
                "description": data["description"],
                "start": {
                    "dateTime": data["startDate"] + "T" + data["startTime"] + ":00" + "%s" % GMTOffset
                },
                "end": {
                    "dateTime": data["endDate"] + "T" + data["endTime"] + ":00" + "%s" % GMTOffset
                }
            }

            # Call API to insert event
            try:
                calendarAPI.eventInsert(auth, "primary", False, eventData)
            except: print("** ERROR: EXCEPTION WHEN TRYING TO CREATE EVENT **")
        
        return redirect(url_for('calendar', user = user["id"]))

    else:

        # Render calendar.html with user and calendar variables for DOM
        return render_template("pages/calendar.html", liUser = user["id"], calendar = cal["id"])


############################################################
## Route logic for logout button is clicked
############################################################
@app.route('/logout')
def logout():

    print("Logout: ", session["userID"])
    session.pop("userID", None)
    
    return redirect(url_for('index'))






# Starting the server
if __name__ == '__main__':
    app.run()