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

    userjson = json.dumps(user, indent=4)


    f = open("../database/data.json", "a")
    f.write(userjson)
    f.close()

    f = open("../database/data.json", "r")
    print(f.read())

    # connection = dbConnection()
    # cursor = connection.cursor()

    # sql = "CALL myDB.Register(%s, %s, %s, %s, %s, %s)"
    # values = (user["firstName"], user["lastName"], user["email"], user["username"], user["password"], user["salt"])

    # try:
    #     cursor.execute(sql, values)
    #     connection.commit()
    # except:
    #     print("An error occurred during user signup")


    return


