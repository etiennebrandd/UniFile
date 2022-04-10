# import jwt
# from security import key
import foodAPI

# # Fetch user detais for displaying on dashboard
# def dashboardLoad(token):

#     decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
#     return

def simpleSearch(query):
    query = query.to_dict()

    results = foodAPI.getRecipesBySearch(query["query"], 20)
    print(results)

    return results



