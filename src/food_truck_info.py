import requests
from geopy import distance

def get_food_truck_info():
    r = requests.get('https://data.sfgov.org/resource/rqzj-sfat.json')
    return r.json()

def get_n_closest_trucks(latitude, longitude, n):
    food_truck_data = get_food_truck_info()
    current_location = (latitude, longitude)
    for truck in food_truck_data:
        truck_location = (truck['latitude'], truck['longitude'])
        distance_from_truck = distance.distance(current_location, truck_location).miles
        truck['distance_from_truck'] = distance_from_truck

    trucks_with_distance = sorted(food_truck_data, key=lambda x: x['distance_from_truck'])
    return trucks_with_distance[:n]