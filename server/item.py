from foodAPI import getRecipeInformation
from security import inputValidator
import random

def recipeInfo(id):

    # Fetch recipe info by calling API
    recipeInfo = getRecipeInformation(id, False)

    # Capitalise first letter of each ingredient
    for ingredient in recipeInfo["extendedIngredients"]:
        ingredient["name"] = ingredient["name"].capitalize()
        
    # Strip summary of HTML tags
    recipeInfo["summary"] = inputValidator(recipeInfo["summary"])

    # Truncate Spoonacular Score to remove decimal places
    recipeInfo["spoonacularScore"] = int(recipeInfo["spoonacularScore"])

    return recipeInfo


def relatedRecipes(recipes, id):

    # Loop through list of recipes and remove the recipe being viewed from the list so it isn't returned
    for recipe in recipes["results"]:
        if recipe["id"] == id:
            recipes["results"].pop(recipes["results"].index(recipe))

    # Generate random index between 0 and length of list, and assign recipe of that index to rel1
    rel1 = recipes["results"][random.randint(0, len(recipes["results"]))]

    # Remove the recipe assigned as rel1 from the list so it cannot be picked again
    for recipe in recipes["results"]:
        if recipe["id"] == rel1["id"]:
            recipes["results"].pop(recipes["results"].index(rel1))

    # Generate random index between 0 and length of list, and assign recipe of that index to rel2
    rel2 = recipes["results"][random.randint(0, len(recipes["results"]))]

    # Convert images to 240x150
    rel1["image"] = imageResize(rel1["image"])
    rel2["image"] = imageResize(rel2["image"])
    
    return rel1, rel2


def imageResize(image):

    url = image.split("-")
    url[1] = '-240x150.jpg'

    image = url[0] + url[1]

    return image
