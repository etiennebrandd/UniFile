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
        register, id = dataAccess.dbRegister(request.form)

        # If false returned, signup failed - redirect to registration form
        if register == False:
            return render_template('index.html', message = "Registration failed. Please try again")

        # # If true returned, signup successful, return dashboard
        else:
            return redirect(url_for('dashboard', user = id))

    else:
        return render_template('index.html', message = "")


@app.route('/dashboard')
def dashboard():

    user = dataAccess.dbRetrieve(request.args.get('user'))
    return render_template('pages/dashboard.html', firstName = user["firstName"])



# Starting the server
if __name__ == '__main__':
    app.run()