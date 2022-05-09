import json
from core.security import hash, generateJWT
import re
from core.foodAPI import mealPlanConnectUser
from flask import flash

def dbRegister(user):

    f = open("../database/users.json", "r")
    users = json.loads(f.read())
    f.close()

    for u in users:
        if user["email"] == u["email"]:
            return
        else: continue

    # Turn form data into dictionary & generate id, hashed pword, and default info
    user = (user.to_dict())

    # Ensure that the password and confirm password fields match; return if not.
    if user["password"] != user["confirm-password"]:
        return

    # Generate spoonacular API credentials and return if there is an error (quota exceeded)
    try:
        apiUsername, apiHash = mealPlanConnectUser(user)
    except:
        return

    user["password"], user["salt"] = hash(user["password"], True, "")
    user["apiUsername"] = apiUsername
    user["apiHash"] = apiHash
    user["tier"] = 0
    user["timezone"] = "Europe/London"
    user["theme"] = 0

    # Get rid of the duplicate password fielf
    user.pop("confirm-password")

    # Insert user information into database
    insertInto("../database/users.json", user)

    # Generate the JWT to pass back to the user
    jwt, exp, sig = generateJWT(user)

    # Store the new JWT details
    storeJWTDetails(sig, exp)

    return jwt


# Login function
def dbLogin(user):

    creds = (user.to_dict())

    # Open users for reading
    f = open("../database/users.json", "r")
    users = json.loads(f.read())
    f.close()

    # Loop through each user
    for user in users:

        # If entered email matches user record
        if creds["email"] == user["email"]:
            
            # Hash entered password with salt of found user record
            passwordAttempt = hash(creds["password"], False, user["salt"])

            # If entered password matches user record
            if passwordAttempt == user["password"]:

                # Generate the JWT to pass back to the user
                jwt, exp, sig = generateJWT(user)

                # Store the new JWT details and return to client
                storeJWTDetails(sig, exp)
                return jwt

            # Else wrong password
            else: return

        # Else no match found yet so continue looping
        else: continue

    # No match found
    return


# Logout and clear JWT
def dbLogout(jwt):

    # Find signature of JWT
    if jwt == None:
        return

    splitJWT = re.split("\.", jwt)
    sig = splitJWT[2]

    f = open("../database/jwt.json", "r")
    tokens = json.loads(f.read())
    f.close()

    for token in tokens:

        if sig == token["sig"]: 
            tokens.pop(tokens.index(token))
            break

        else: continue

    tokens = json.dumps(tokens, indent=4)

    f = open("../database/jwt.json", "w")
    f.write(tokens)
    f.close()

    return
    

# Store the signature and expiration time of the token in the database
def storeJWTDetails(sig, exp):

    # Structure the JWT data
    details = {
    "sig": sig,
    "exp": exp
    }

    # Insert JWT details into file
    insertInto("../database/jwt.json", details)


# Helper function to write to a given file
def insertInto(filepath, value):

    f = open(filepath, "r")
    data = json.loads(f.read())
    f.close()

    data.append(value)
    data = json.dumps(data, indent=4)

    f = open(filepath, "w")
    f.write(data)
    f.close()