from flask import Flask, render_template, request, redirect
import dataAccess

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():

    # If route receives a POST request (a user has registered)
    if request.method == 'POST':

        # Call the register method and return the inserted row count
        register = dataAccess.dbRegister(request.form)

        # If false returned, signup failed - redirect to registration form
        if register == False:
            return render_template('pages/register.html', message = "Registration failed. Please try again")

        # # If true returned, signup successful, return dashboard
        else:
            return render_template('pages/register.html', message = "")

    else:
        return render_template('pages/register.html', message = "")



# Starting the server
if __name__ == '__main__':
    app.run()