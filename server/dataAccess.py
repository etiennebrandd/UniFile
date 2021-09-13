import json
import security


def dbRegister(user):

    # Prepare the user data - dictionary
    user = (user.to_dict())
    user["password"], user["salt"] = security.hash(user["password"], True, "")
    user["username"] = user["firstName"][0].lower() + user["lastName"].lower()
    user["id"] = security.uid()[:6]

    # Open the data file for reading and convert to dict
    f = open("../database/users.json", "r")
    data = json.loads(f.read())
    f.close()

    # Extract the users data from dictionary - now a list
    userData = data["users"]

    # Loop through existing user records to see if email exists
    for i in userData:

        if i["email"] == user["email"]:
            return False, ""
            
        else:
            continue


    userData.append(user)

    # Set the value of the users data to be the new list
    data["users"] = userData

    # Open data file for writing and convert dict to json
    f = open("../database/users.json", "w")
    newData = json.dumps(data, indent=4)
            
    # Overwrite the data file
    f.write(newData)
    f.close()

    return True, user["id"]


def dbRetrieveUserByID(userID):

    f = open("../database/users.json", "r")
    data = json.loads(f.read())
    f.close()

    # Extract the users data from dictionary - now a list
    userData = data["users"]

    # Loop through existing user records to see if email exists
    for user in userData:

        if userID == user["id"]:
            
            return user
            
        else:
            continue


def dbLogin(credentials):

    # Define credentials as variables
    email = (credentials.to_dict()["email"])
    password = (credentials.to_dict()["password"])
    
    # Open users file for reading and convert to dict
    f = open("../database/users.json", "r")
    data = json.loads(f.read())
    f.close()

    # Extract users
    userData = data["users"]

    # Iterate through each user object to see if credential email matches record
    for user in userData:

        if email == user["email"]:

            # Hash the input password using the retrieved salt for found user
            checkpwd = security.hash(password, False, user["salt"])

            # Check hashed input password matches what is in database
            if checkpwd == user["password"]:
                
                csrf = dbSession(user["id"])
                return True, user["id"], csrf

            else:
                return False, "", ""

        # Keep iterating if not match
        else:
            continue

    return False, "", ""


def dbSession(id):

    f = open("../database/sessions.json", "r")
    data = json.loads(f.read())
    f.close()

    sessionData = data["sessions"]

    try:
        for i in sessionData:

            if i["user_id"] == id:
                sessionData.pop(sessionData.index(i))
                break
    except Exception: 
        pass

    csrf = security.uid()

    sesh = {
        "user_id": id,
        "csrf_token": csrf
    }
        
    sessionData.append(sesh)
            

    data["sessions"] = sessionData

    f = open("../database/sessions.json", "w")
    newData = json.dumps(data, indent=4)
    
    f.write(newData)
    f.close()

    return sesh["csrf_token"]
        

    # f.write()
    
    # return cookie
    