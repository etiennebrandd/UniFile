import requests

# API key used to allow us to call the API (this needs to be hidden eventually)
api_key = "f163cdaa932542509e6f18bb466b4c14"

############################################################
## View the page linked in comment before each function to see
# #relevant parameters that can be passed in as the payload

# Search Recipes
# https://spoonacular.com/food-api/docs#Search-Recipes-Complex
def getRecipesBySearch(payload):

    endpoint = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + api_key

    #######################
    # Testing Purposes
    #
    # payload = {
    #     'query': "tomato",
    #     'cuisine': "italian",
    #     'number': 5

    # }

    r = requests.get(endpoint, params=payload)
    results = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return results


# Search Recipes by Ingredients
# https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients
def getRecipesByIngredients(payload):

    endpoint = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + api_key

    #######################
    # Testing Purposes
    #
    # payload = {
    #     'ingredients': ingredients,
    #     'number': 5

    # }

    r = requests.get(endpoint, params=payload)
    results = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return results


# Get Recipe Information (nutrition boolean)
# https://spoonacular.com/food-api/docs#Get-Recipe-Information
def getRecipeInformation(recipeID, nutrition):

    endpoint = "https://api.spoonacular.com/recipes/" + str(recipeID) + "/information?apiKey=" + api_key

    payload = {
        "includeNutrition": nutrition
    }

    r = requests.get(endpoint, params=payload)
    result = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return result


# Get Analyzed Recipe Instructions
# https://spoonacular.com/food-api/docs#Get-Analyzed-Recipe-Instructions
def getRecipeInstructions(recipeID, stepBreakdown):

    endpoint = "https://api.spoonacular.com/recipes/" + str(recipeID) + "/analyzedInstructions?apiKey=" + api_key

    payload = {
        "stepBreakdown": stepBreakdown
    }

    r = requests.get(endpoint, params=payload)
    instructions = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return instructions



# recipe = getRecipeInformation(716429)
# print(recipe)







# recipes = getRecipesByIngredients('apples')

# for recipe in recipes:
#     print(recipe["title"])