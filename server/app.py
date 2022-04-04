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
@app.route('/')
def index():

    # If a session exists, we need to remove it
    if "Token" in session:
        return redirect(url_for('logout'))

    return render_template('index.html')


############################################################
## Route logic for when login button is clicked
############################################################
@app.route('/portalsignin', methods = ["GET", "POST"])
def portalsignin():

    if request.method == "GET":
        return render_template('pages/portal.html', x = None)

    else: 

        # Validate login and if a JWT is found, forward to dashboard
        jwt = dataAccess.dbLogin(request.form)

        if jwt != None: 
            session['Token'] = jwt
            return redirect(url_for('dashboard'))

        # Login error
        else: return redirect(url_for('portalsignin'))


############################################################
## Route logic for when register button is clicked
############################################################
@app.route('/portalregister', methods = ["GET", "POST"])
def portalregister():

    if request.method == "GET":
        return render_template('pages/portal.html', x = 1 )

    else:
        # Register the user and return JWT for session
        jwt = dataAccess.dbRegister(request.form)

        # Store JWT client-side
        session['Token'] = jwt
        return redirect(url_for('dashboard'))


############################################################
## Route logic for dashboard page
############################################################
@app.route('/dashboard')
def dashboard():

    return render_template('pages/dashboard.html')


############################################################
## Route logic for when logout button is clicked
############################################################
@app.route('/logout')
def logout():

    # Remove JWT from the client-side cookie and details from server
    if "Token" in session:

        dataAccess.dbLogout(session["Token"])
        session.pop('Token')

    # Return homepage
    return redirect(url_for('index'))


# Starting the server
if __name__ == '__main__':
    app.run()