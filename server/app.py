from flask import Flask, render_template, request, redirect, url_for
import dataAccess
import calendarAPI

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')


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

        loggedIn, id, token = dataAccess.dbLogin(request.form)  

        if loggedIn == False or token == "":
            return redirect(url_for('index'))

        else:
            return redirect(url_for('dashboard', user = id))



############################################################
## Route logic for dashboard page
############################################################
@app.route('/dashboard')
def dashboard():

    # Retrive ID of user
    id = request.args.get("user")

    # Check the user is authenticated by validating token exists
    x = dataAccess.dbCheckToken(id)

    if not request.args or x == False:
        return redirect(url_for('index'))

    user = dataAccess.dbRetrieveUserByID(id)
    return render_template('pages/dashboard.html',
        firstName = user["firstName"],
        liUser = user["id"]
    )
    
    # else: return redirect(url_for('index'))


############################################################
## Route logic for calendar page
############################################################
@app.route('/calendar', methods = ['GET', 'POST'])
def calendar():

    id = request.args.get("user")

    x = dataAccess.dbCheckToken(id)

    if not request.args or x == False:
        return redirect(url_for('index'))
        

    # Retrive a users ID
    user = dataAccess.dbRetrieveUserByID(id)

    # Retrieve access token or direct user through auth flow
    try:
        auth = calendarAPI.apiOAuth(id)
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
    
    dataAccess.dbLogout(request.args.get("user"))
    return redirect(url_for('index'))






# Starting the server
if __name__ == '__main__':
    app.run()