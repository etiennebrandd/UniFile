from flask import Flask, render_template

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def test():
    return render_template('pages/register.html')




# Starting the server
if __name__ == '__main__':
    app.run()