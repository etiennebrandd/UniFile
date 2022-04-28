# import jwt
from datetime import datetime
from security import key
import foodAPI
import jwt
import re
import pytz
import json

regions = []

for x in pytz.all_timezones:
    regions.append(x)

# Decode token and return name
def decodeJWT(token):

    decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
    name = re.split(" ", decodedJWT["usr"])
    return name[0]


def simpleSearch(query):
    query = query.to_dict()

    results = foodAPI.getRecipesBySearch(query["query"], 20)
    return results


def updateUser(token, form):

    f = open("../database/users.json", "r")
    users = json.loads(f.read())
    f.close()

    decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
    for user in users:

        fullName = str(user["fname"] + " " + user["lname"])

        if decodedJWT["usr"] == fullName:

            user["timezone"] == form["region"]
            user["theme"] == form["theme"]

    return