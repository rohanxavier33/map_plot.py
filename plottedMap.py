import folium
from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="geo_plotter")
    result = geolocator.geocode(location, addressdetails=True, extratags=True, timeout=10)
    
    if result:
        return (result.latitude, result.longitude)
    else:
        return None

def plot_locations_on_map(locations):
    map_center = (39.8283, -98.5795)  # Default center
    my_map = folium.Map(location=map_center, zoom_start=4)

    for location in locations:
        coordinates = get_coordinates(location)
        if coordinates:
            folium.Marker(coordinates, popup=location).add_to(my_map)
        else:
            print(f"Could not find coordinates for location: {location}")

    return my_map

if __name__ == "__main__":
    # usage:
    input_locations = ["St Paul, MN",
        "Dallas County, TX",
        "Kenneth Square, PA",
        "Orlando, FL",
        "North Brunswick, New Jersey",
        "Champaign, IL",
        "Bennington, NE",
        "Somerset, NJ",
        "Stony Brook, NY",
        "Gary, Indiana",
        "San Jose, CA",
        "Brooklyn, NY",
        "Medford, MA",
        "Greensboro, North Carolina",
        "Tallahassee, FL",
        "Dallas, TX",
        "Napa, CA",
        "Huntington Beach, Ca"]
    result_map = plot_locations_on_map(input_locations)
    
    # Save the map to an HTML file
    result_map.save("output_map.html")
