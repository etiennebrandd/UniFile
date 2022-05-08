from core.security import validateJWT
from flask import Flask, render_template, request, redirect, url_for, session
from core.dataAccess import dbLogin, dbRegister, dbLogout
from dashboard.dboard import decodeJWT, simpleSearch, regions, updateUser
from config import secret_key
from recipes.item import recipeInfo, relatedRecipes

# Configure server and folder to fetch pages from
app = Flask(__name__, template_folder='../client/')
app.secret_key = secret_key

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
        jwt = dbLogin(request.form)

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
        jwt = dbRegister(request.form)

        if jwt != None: 
            session['Token'] = jwt
            return redirect(url_for('dashboard'))

        else: return redirect(url_for('portalregister'))


############################################################
## Route logic for dashboard page
############################################################
@app.route('/dashboard', methods = ["GET", "POST"])
def dashboard():

    # GET
    if request.method == "GET":

        # Validate JWT
        try:
            valid = validateJWT(session["Token"])

            if valid == False: 
                return redirect(url_for('logout'))

        except: pass

        # Find the name of the user if they have one.. guest if not!
        if "Token" in session:
            welcome = decodeJWT(session["Token"])
        else:
            welcome = "Welcome, guest!"

        # Render the dashboard with the user's name
        return render_template('pages/dashboard.html', name = welcome)

    # POST
    else:

        # Validate JWT
        # valid = validateJWT(session["Token"])
        # if valid == False: 
        #     return redirect(url_for('logout'))

        # # Use searchbar input as API query
        # results = dboard.simpleSearch(request.form)
        # print(results)

        return redirect(url_for('dashboard'))


############################################################
## Route logic for search results page
############################################################
@app.route('/search', methods = ['GET', 'POST'])
def search():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    else:

        # Validate JWT
        try:
            valid = validateJWT(session["Token"])
            if valid == False: 
                return redirect(url_for('logout'))
        except: pass

        # Use searchbar input as API query
        global results
        results = simpleSearch(request.form)

        return render_template('pages/search.html', results = results["results"])


############################################################
## Route logic for item page
############################################################
@app.route('/item/<id>', methods = ['GET', 'POST'])
def item(id):

    if id == None:
        return redirect(url_for('search'))

    # Validate JWT
    try:
        valid = validateJWT(session["Token"])
        if valid == False: 
            return redirect(url_for('logout'))
    except: pass

    # Perform recipe information collection
    info = recipeInfo(id)

    # Fetch related recipes
    if len(results["results"]) > 2:
        rel1, rel2 = relatedRecipes(results, id)
    else: rel1, rel2 = None, None

    return render_template('pages/item.html', info = info, rel1 = rel1, rel2 = rel2)


############################################################
## Route logic for settings page
############################################################
@app.route('/settings', methods = ['GET', 'POST'])
def settings():

    if request.method == "GET":

        if not "Token" in session:
            return redirect(url_for('dashboard'))

        valid = validateJWT(session["Token"])

        if valid == False: 
            return redirect(url_for('logout'))

        r = regions

        return render_template('pages/settings.html', regions = r)

    else:
        updateUser(session["Token"], request.form, request.files)

        return redirect(url_for('logout'))


############################################################
## Route logic for when logout button is clicked
############################################################
@app.route('/logout')
def logout():

    # Remove JWT from the client-side cookie and details from server
    if "Token" in session:

        dbLogout(session["Token"])
        session.pop('Token')

    # Return homepage
    return redirect(url_for('index'))


############################################################
## Route logic for custom error pages
############################################################
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/errors/page-not-found.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('pages/errors/server-error.html'), 500


# Starting the server
if __name__ == '__main__':
    app.run()