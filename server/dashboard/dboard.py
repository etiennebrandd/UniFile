# import jwt
from datetime import datetime
from core.security import key
from core.foodAPI import getRecipesBySearch
import jwt
import re
import pytz
import json

regions = []

for x in pytz.all_timezones:
    regions.append(x)

# Return details for welcome message
def decodeJWT(token):

    # Decode token
    decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
    # Get name
    name = re.split(" ", decodedJWT["usr"])

    # Get time in user's timezone
    tz = pytz.timezone(decodedJWT["tmz"])
    time = datetime.now(tz)
    time = time.strftime("%H")

    if int(time) < 12: p = "Morning"
    elif int(time) < 17: p = "Afternoon"
    else: p = "Evening"

    greeting = "Good {}, {}."

    return greeting.format(p, name[0])


def simpleSearch(query):
    query = query.to_dict()

    results = getRecipesBySearch(query["query"], 20)
    return results


def updateUser(token, form, file):

    # Turn form into dictionary
    form = form.to_dict()

    # Fetch users
    f = open("../database/users.json", "r")
    users = json.loads(f.read())
    f.close()

    # Get name of user from JWT
    decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
    # Loop through users to find the right user based on JWT value
    for user in users:

        # Construct full name
        fullName = str(user["fname"] + " " + user["lname"])

        if decodedJWT["usr"] == fullName:

            # Update values
            user["timezone"] = form["region"]

            if "theme" in form:
                user["theme"] = int(form["theme"])

            break
            # user["theme"] == form["theme"]

        else: continue

    # Convert dictionary back to json and write to file
    users = json.dumps(users, indent=4)
    f = open("../database/users.json", "w")
    f.write(users)
    f.close()

    # Upload user's profile picture if there is one
    if "profpic" in file:

        allowedExtensions = {'png', 'jpg', 'jpeg', 'gif'}
        profilePic = file["profpic"]

        decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
        hash = decodedJWT["hsh"]

        if profilePic.filename.split('.')[1].lower() in allowedExtensions:

            dst = '../database/userImages/' + hash + "." + profilePic.filename.split('.')[1].lower()
            profilePic.save(f"{dst}")

    return