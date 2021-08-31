import json
import security


def dbRegister(user):

    # Prepare the user data - dictionary
    user = (user.to_dict())
    user["password"], user["salt"] = security.hash(user["password"], True, "")
    user["username"] = user["firstName"][0].lower() + user["lastName"].lower()
    user["id"] = security.uid()[:6]

    # Open the data file for reading and convert to dict
    f = open("../database/data.json", "r")
    data = json.loads(f.read())
    f.close()

    # Extract the users data from dictionary - now a list
    userData = data["users"]

    # Loop through existing user records to see if email exists
    for i in userData:

        if i["email"] == user["email"]:
            return False
            
        else:
            continue


    userData.append(user)

    # Set the value of the users data to be the new list
    data["users"] = userData

    # Open data file for writing and convert dict to json
    f = open("../database/data.json", "w")
    newData = json.dumps(data, indent=4)
            
    # Overwrite the data file
    f.write(newData)
    f.close()

    return True, user["id"]


def dbRetrieve(userID):

    f = open("../database/data.json", "r")
    data = json.loads(f.read())
    f.close()

    # Extract the users data from dictionary - now a list
    userData = data["users"]

    # Loop through existing user records to see if email exists
    for user in userData:

        if userID == user["id"]:
            print(user)
            return user
            
        else:
            continue





    


