import requests
from geopy import distance

def get_food_truck_info():
    """Get food truck dataset from endpoint"""
    r = requests.get('https://data.sfgov.org/resource/rqzj-sfat.json')
    return r.json()

def get_n_closest_trucks(latitude, longitude, n):
    """Calculate distance to food truck from current location, then filter closest"""
    food_truck_data = get_food_truck_info()
    current_location = (latitude, longitude)
    for truck in food_truck_data:
        truck_location = (truck['latitude'], truck['longitude'])
        distance_from_truck = distance.distance(current_location, truck_location).miles
        truck['distance_from_truck'] = distance_from_truck

    trucks_with_distance = sorted(food_truck_data, key=lambda x: x['distance_from_truck'])

    return format_response(trucks_with_distance[:n])

def format_response(res):
    """Format response to have type of food and address"""
    response = "Here are some options: \n"
    for r in res:
        response += r['fooditems']
        response += " at "
        response += r['address']
        response += "\n"
    
    return response