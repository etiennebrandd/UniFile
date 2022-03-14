from security import uid
from flask import Flask, render_template, request, redirect, url_for, session
import dataAccess
from foodAPI import foodProcessor

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')
app.secret_key = "0519f8cb9ecc4c0a8781d07512c795c8"


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
        
        return render_template('index.html')


############################################################
## Route logic for when login button is clicked
############################################################
# @app.route('/login', methods = ['POST'])
# def login():
#     if request.method == 'POST':

#         return    

@app.route('/portalsignin')
def portalsignin():

    return render_template('pages/portal.html', x = None)

@app.route('/portalregister')
def portalregister():

    return render_template('pages/portal.html', x = 1 )

############################################################
## Route logic for dashboard page
############################################################
@app.route('/dashboard')
def dashboard():

    return render_template('pages/dashboard.html')


# Starting the server
if __name__ == '__main__':
    app.run()