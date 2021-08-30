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
        rowCount = dataAccess.dbRegister(request.form)

        # If row count is less than 1, signup failed - redirect to registration form
        if rowCount < 1:
            return render_template('pages/register.html', message = "Signup unsuccessful. Please try again.")

        # If row count is 1 or more, signup successful, return dashboard
        else:
            return render_template('pages/register.html', message = "")

    else:
        return render_template('pages/register.html', message = "")



# Starting the server
if __name__ == '__main__':
    app.run()