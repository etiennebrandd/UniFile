from core.foodAPI import mealPlanGenerate, mealPlanAddTo, mealPlanDeleteFrom, mealPlanGetWeek, mealPlanGetDay

def generateMealPlan(timeperiod):

    mealPlan = mealPlanGenerate(timeperiod)

    return mealPlan


def addToMealPlan(uname, hash, timestamp, slot, type, val):

    payload = {
        "date": timestamp,
        "slot": slot,
        "position": 0,
        "type": type,
        "value": val
    }

    print("Payload: ", payload)

    print(mealPlanAddTo(uname, hash, payload))

    return


def viewMealPlan(uname, hash, date):

    plan = mealPlanGetDay(uname, hash, date)

    print(plan)

    return