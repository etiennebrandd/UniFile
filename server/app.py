from flask import Flask, render_template, request, redirect, url_for
import dataAccess

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')


# Routes
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


@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':

        loggedIn, id = dataAccess.dbLogin(request.form)  

        if loggedIn == False:
            return redirect(url_for('index'))

        else:
            return redirect(url_for('dashboard', user = id))


@app.route('/dashboard')
def dashboard():

    user = dataAccess.dbRetrieveUserByID(request.args.get('user'))
    return render_template('pages/dashboard.html', firstName = user["firstName"])



# Starting the server
if __name__ == '__main__':
    app.run()