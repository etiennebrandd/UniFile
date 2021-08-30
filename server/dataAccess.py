from flask import request
import json
import security

# Creates a connection to the database
# def dbConnection():

#     # Database object containing connection details
#     mydb = mysql.connector.connect (
#         host = "82.39.201.74",
#         user = "admin",
#         password = "P455w0rd!",
#         database = "myDB"
#     )

#     # Return DB object for use elsewhere
#     return mydb


def dbRegister(user):

    user = (user.to_dict())
    user["password"], user["salt"] = security.hash(user["password"], True, "")

    user["username"] = user["firstName"][0].lower() + user["lastName"].lower()


    f = open("../database/data.json", "r")
    data = json.loads(f.read())
    f.close()

    userData = data["users"]

    userData.append(user)

    data["users"] = userData

    f = open("../database/data.json", "w")
    newData = json.dumps(data, indent=4)
    
    f.write(newData)
    f.close()

    return


