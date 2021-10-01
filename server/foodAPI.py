import requests
from io import StringIO
from html.parser import HTMLParser

# API key used to allow us to call the API (this needs to be hidden eventually)
api_key = "f163cdaa932542509e6f18bb466b4c14"

############################################################
## View the page linked in comment before each function to see
## relevant parameters that can be passed in as the payload


#########################################################
## Recipe API Calls

# Search Recipes
# https://spoonacular.com/food-api/docs#Search-Recipes-Complex
def getRecipesBySearch(payload, number):

    endpoint = "https://api.spoonacular.com/recipes/complexSearch?apiKey=" + api_key + "&number=" + str(number)

    r = requests.get(endpoint, params=payload)
    results = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return results


# Search Recipes by Ingredients
# https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients
def getRecipesByIngredients(payload):

    endpoint = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + api_key

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


# Get Recipe Information Bulk (nutrition boolean)
# https://spoonacular.com/food-api/docs#Get-Recipe-Information-Bulk
def getRecipeInformationBulk(recipeIDs, nutrition):

    endpoint = "https://api.spoonacular.com/recipes/informationBulk?ids=" + str(recipeIDs) + "&apiKey=" + api_key

    payload = {
        "includeNutrition": nutrition
    }

    r = requests.get(endpoint, params=payload)
    results = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return results


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

#########################################################
## Ingredient API Calls

# Get Ingredient Information
# https://spoonacular.com/food-api/docs#Get-Ingredient-Information
def getIngredientInformation(ingredID, amount, unit):

    endpoint = "https://api.spoonacular.com/food/ingredients/" + str(ingredID) + "/information?apiKey=" + api_key

    payload = {
        "amount": amount,
        "unit": unit
    }

    r = requests.get(endpoint, params=payload)
    ingredient = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return ingredient


# Get Ingredient Substitutes
# https://spoonacular.com/food-api/docs#Get-Ingredient-Substitutes
def getIngredientSubstitutes(ingredName):

    endpoint = "https://api.spoonacular.com/food/ingredients/substitutes?apiKey=" + api_key

    payload = {
        "ingredientName": ingredName
    }

    r = requests.get(endpoint, params=payload)
    substitutes = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return substitutes


#########################################################
## Grocery Products API Calls

# Search Grocery Products
# https://spoonacular.com/food-api/docs#Search-Grocery-Products
def getGroceryProducts(payload):

    endpoint = "https://api.spoonacular.com/food/products/search?apiKey=" + api_key

    r = requests.get(endpoint, params=payload)
    products = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return products


# Get Product Information
# https://spoonacular.com/food-api/docs#Get-Product-Information
def getProductInfo(productID):

    endpoint = "https://api.spoonacular.com/food/products/" + str(productID) + "?apiKey=" + api_key

    r = requests.get(endpoint)
    product = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return product


# Get Comparable Products
# https://spoonacular.com/food-api/docs#Get-Comparable-Products
def getComparableProducts(productUPC):
    
    endpoint = "https://api.spoonacular.com/food/products/upc/" + str(productUPC) + "/comparable?apiKey=" + api_key

    r = requests.get(endpoint)
    products = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return products


#########################################################
## Menu Item API Calls

# Search Menu Items
# https://spoonacular.com/food-api/docs#Search-Menu-Items
def getMenuItem(payload):

    endpoint = "https://api.spoonacular.com/food/menuItems/search?apiKey=" + api_key

    r = requests.get(endpoint, params=payload)
    item = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return item


# Get Menu Item Information
# https://spoonacular.com/food-api/docs#Get-Menu-Item-Information
def getMenuItemInformation(itemID):

    endpoint = "https://api.spoonacular.com/food/menuItems/" + str(itemID) + "?apiKey=" + api_key

    r = requests.get(endpoint)
    information = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return information


#########################################################
## Meal Plan API Calls
## The Connect User call must be performed on each user
## before any mealplans can be edited. This only needs to
## be done once in order to generate a set of spoonacular
## credentials that are used in each call. These credentials
## must be saved somewhere or bad things will happen!

# Connect User
# https://spoonacular.com/food-api/docs#Connect-User
def mealPlanConnectUser(user):
    
    endpoint = "https://api.spoonacular.com/users/connect?apiKey=" + api_key

    r = requests.post(url=endpoint, json=user)
    userDetails = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return userDetails


# Get Meal Plan Templates
# https://api.spoonacular.com/mealplanner/{username}/templates
def mealPlanGetAllTemplates():

    endpoint = "https://api.spoonacular.com/mealplanner/public-templates?apiKey=" + api_key

    r = requests.get(endpoint)
    templates = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return templates


# Get Meal Plan Template
# https://spoonacular.com/food-api/docs#Get-Meal-Plan-Template
def mealPlanGetTemplate(username, hash, mealPlanID):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/templates/" + str(mealPlanID) + "?apiKey=" + api_key + "&hash=" + hash

    r = requests.get(endpoint)
    template = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return template


# Generate Meal Plan
# https://spoonacular.com/food-api/docs#Generate-Meal-Plan
def mealPlanGenerate(payload):

    endpoint = "https://api.spoonacular.com/mealplanner/generate?apiKey=" + api_key

    r = requests.get(endpoint, params=payload)
    plan = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return plan


# Add to Meal Plan (the payload for this one is quite complex)
# https://spoonacular.com/food-api/docs#Add-to-Meal-Plan
def mealPlanAddTo(username, hash, payload):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/items" + "?apiKey=" + api_key + "&hash=" + hash

    r = requests.post(url=endpoint, json=payload)
    res = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return res


# Delete from Meal Plan
# https://spoonacular.com/food-api/docs#Delete-from-Meal-Plan
def mealPlanDeleteFrom(username, hash, mealID):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/items/" + mealID + "?apiKey=" + api_key + "&hash=" + hash
    r = requests.delete(endpoint)
    res = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return res


# Clear Meal Plan Day
# https://spoonacular.com/food-api/docs#Clear-Meal-Plan-Day
def mealPlanClearDay(username, hash, date):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/day/" + date + "?hash=" + hash + "&apiKey=" + api_key
    r = requests.delete(endpoint)
    res = r.json()
    
    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return res


# Get Meal Plan Day
# https://spoonacular.com/food-api/docs#Get-Meal-Plan-Day
def mealPlanGetDay(username, hash, date):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/day/" + date + "?hash=" + hash + "&apiKey=" + api_key
    r = requests.get(endpoint)

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    plan = r.json()

    return plan


# Get Meal Plan Week
# https://spoonacular.com/food-api/docs#Get-Meal-Plan-Week
def mealPlanGetWeek(username, hash, startDate):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/week/" + startDate + "?hash=" + hash + "&apiKey=" + api_key
    r = requests.get(endpoint)

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    plan = r.json()

    return plan


#########################################################
## Shopping List API Calls

# Compute Shopping List (payload is a list of simple ingredients)
# https://spoonacular.com/food-api/docs#Compute-Shopping-List
def shoppingListCompute(payload):

    endpoint = "https://api.spoonacular.com/mealplanner/shopping-list/compute?apiKey=" + api_key

    r = requests.post(endpoint, json=payload)
    list = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return list


# Add to Shopping List
# https://spoonacular.com/food-api/docs#Add-to-Shopping-List
def shoppingListAdd(username, hash, payload):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/shopping-list/items?apiKey=" + api_key + "&hash=" + hash
    r = requests.post(endpoint, json=payload)
    list = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return list


# Delete from Shopping List
# https://spoonacular.com/food-api/docs#Delete-from-Shopping-List
def shoppingListDelete(username, hash, itemID):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/shopping-list/items/" + str(itemID) + "?apiKey=" + api_key + "&hash=" + hash
    r = requests.delete(endpoint)
    list = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return list


# Get Shopping List
# https://api.spoonacular.com/mealplanner/{username}/shopping-list
def shoppingListGet(username, hash):

    endpoint = "https://api.spoonacular.com/mealplanner/" + username + "/shopping-list?apiKey=" + api_key + "&hash=" + hash
    r = requests.get(endpoint)
    list = r.json()

    print("** POINTS USED THIS REQUEST: ", r.headers["X-API-Quota-Request"], " **")
    print("** API QUOTA USED: ", r.headers["X-API-Quota-Used"], " **")

    return list


# Class to strip HTML
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


# Process user requests to call the correct API
def foodProcessor(formData):

    results = getRecipesBySearch(formData, 2)
    recipes = results["results"]

    ids = []

    for recipe in recipes:
        ids.append(str(recipe["id"]))

    stringIds = ",".join(ids)
        
    recipeDetails = getRecipeInformationBulk(stringIds, True)

    recipePrices = []
    recipeServings = []
    recipeTime = []
    recipeType = []
    recipeCalories = []
    recipeSummary = []

    for detail in recipeDetails:

        recipeTime.append(detail["readyInMinutes"])
        recipeServings.append(detail["servings"])
        recipeSummary.append(detail["summary"])
        recipePrices.append(detail["pricePerServing"])
        recipeType.append(detail["dishTypes"])
        recipeCalories.append(detail["nutrition"]["nutrients"][0]["amount"])


    for recipe in recipes:

        i = recipes.index(recipe)
        recipes[i]["time"] = recipeTime[i]
        recipes[i]["servings"] = recipeServings[i]

        s = MLStripper()
        s.feed(recipeSummary[i])
        sanitisedSummary = s.get_data()

        recipes[i]["summary"] = sanitisedSummary
        recipes[i]["price"] = int(recipePrices[i])
        recipes[i]["type"] = recipeType[i]
        recipes[i]["calories"] = recipeCalories[i]

    total = results["totalResults"]

    return recipes, recipeDetails, total

