def living_cost(days):
    return 5000*days
def plane_cost(city):
    if city=="lahore":
        return 10000
    elif city=="narankagan":
        return 15000
    elif city=="sakardu":
        return 12000
    def trip_expendature(city,days,shopping_money):
        return living_cost(days)+plane_cost(city)+shopping_money
    print("Total trip expandature:",trip_expandature("sakardu",5,50000))