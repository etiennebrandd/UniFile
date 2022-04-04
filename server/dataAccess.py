import json
import security
import re

def dbRegister(user):

    # Turn form data into dictionary & generate id, hashed pword, and default info
    user = (user.to_dict())

    user["password"], user["salt"] = security.hash(user["password"], True, "")
    user["username"] = user["fname"][0].lower() + user["lname"].lower()
    user["id"] = security.uid()[:6]
    user["tier"] = 0
    user["timezone"] = "GMT+0:00"
    user["theme"] = 0

    # Get rid of the duplicate password fielf
    user.pop("confirm-password")

    # Insert user information into database
    insertInto("../database/users.json", user)

    # Generate the JWT to pass back to the user
    jwt, exp, sig = security.generateJWT(user)

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
            passwordAttempt = security.hash(creds["password"], False, user["salt"])

            # If entered password matches user record
            if passwordAttempt == user["password"]:

                # Generate the JWT to pass back to the user
                jwt, exp, sig = security.generateJWT(user)

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



# def dbLogin(credentials):

#     # Define credentials as variables
#     email = (credentials.to_dict()["email"])
#     password = (credentials.to_dict()["password"])
    
#     # Open users file for reading and convert to dict
#     f = open("../database/users.json", "r")
#     data = json.loads(f.read())
#     f.close()

#     # Extract users
#     userData = data["users"]

#     for user in userData:

#         encoded = str.encode(user)
#         decrypted = security.decrypt(encoded)

#         x = decrypted.replace("'", "\"")
#         decrypted = json.loads(x)

#         i = userData.index(user)
#         userData[i] = decrypted

#     # Iterate through each user object to see if credential email matches record
#     for user in userData:

#         if email == user["email"]:

#             # Hash the input password using the retrieved salt for found user
#             checkpwd = security.hash(password, False, user["salt"])

#             # Check hashed input password matches what is in database
#             if checkpwd == user["password"]:
                
#                 # csrf = dbSession(user["id"])
#                 userJWT, exp = security.generateJWT(user)
#                 splitJWT = re.split("\.", userJWT)
#                 sig = splitJWT[2]

#                 storeJWTDetails(sig, exp)
#                 return True, user["id"], userJWT


#             else:
#                 return False, "", ""

#         # Keep iterating if not match
#         else:
#             continue

#     return False, "", ""


# def dbCheckToken(id):
    
#     # Get encrypted sessions and decrypt
#     f = open("../database/sessions.json", "r")
#     data = json.loads(f.read())
#     f.close()

#     sessionData = data["sessions"]
    
#     for session in sessionData:

#         encoded = str.encode(session)
#         decrypted = security.decrypt(encoded)

#         x = decrypted.replace("'", "\"")
#         decrypted = json.loads(x)

#         i = sessionData.index(session)
#         sessionData[i] = decrypted

#     # Check if the token exists for the user
#     for i in sessionData:

#         if i["user_id"] == id:
#             if i["csrf_token"]:

#                 return True

#             else: return False
        
#     else: return False


# def dbLogout(id):

#     # Get encrypted sessions and decrypt
#     f = open("../database/sessions.json", "r")
#     data = json.loads(f.read())
#     f.close()

#     sessionData = data["sessions"]
    
#     for session in sessionData:

#         encoded = str.encode(session)
#         decrypted = security.decrypt(encoded)

#         x = decrypted.replace("'", "\"")
#         decrypted = json.loads(x)

#         i = sessionData.index(session)
#         sessionData[i] = decrypted

#     # Loop through each session and delete the appropriate session
#     for i in sessionData:

#         if i["user_id"] == id:
#             sessionData.pop(sessionData.index(i))
#             break

#     # Encrypt remaining sessions and write back to file
#     for session in sessionData:

#         encrypted = security.encrypt(str(session))
#         decoded = encrypted.decode()
#         i = sessionData.index(session)
#         sessionData[i] = decoded

#     data["sessions"] = sessionData
#     newData = json.dumps(data, indent=4)
    
#     f = open("../database/sessions.json", "w")
#     f.write(newData)
#     f.close()