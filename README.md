# Geo Plotter

A simple Python program to plot locations on a map using Folium and Geopy.

## Overview

This program takes a list of locations and plots them on a map. It utilizes the [Folium](https://python-visualization.github.io/folium/) library for map creation and [Geopy](https://geopy.readthedocs.io/) for geocoding.

## Dependencies

- Folium
- Geopy

## Installation

```bash
pip install folium geopy

Usage
Modify the input_locations list in the __main__ section with the locations you want to plot. Then run the script.
if __name__ == "__main__":
    input_locations = [
        "St Paul, MN",
        "Dallas County, TX",
        "Kenneth Square, PA",
        # ... add more locations as needed
    ]
    result_map = plot_locations_on_map(input_locations)
    
    # Save the map to an HTML file
    result_map.save("output_map.html")
The resulting map will be saved as "output_map.html" in the same directory.

Customization
You can customize the map center and zoom level by modifying the map_center and zoom_start variables in the plot_locations_on_map function.
map_center = (latitude, longitude)  # Set the desired center coordinates
my_map = folium.Map(location=map_center, zoom_start=desired_zoom_level)


Certainly! Below is a sample README.md for the provided Python program:

markdown
Copy code
# Geo Plotter

A simple Python program to plot locations on a map using Folium and Geopy.

## Overview

This program takes a list of locations and plots them on a map. It utilizes the [Folium](https://python-visualization.github.io/folium/) library for map creation and [Geopy](https://geopy.readthedocs.io/) for geocoding.

## Dependencies

- Folium
- Geopy

## Installation

```bash
pip install folium geopy
Usage
Modify the input_locations list in the __main__ section with the locations you want to plot. Then run the script.

python
Copy code
if __name__ == "__main__":
    input_locations = [
        "St Paul, MN",
        "Dallas County, TX",
        "Kenneth Square, PA",
        # ... add more locations as needed
    ]
    result_map = plot_locations_on_map(input_locations)
    
    # Save the map to an HTML file
    result_map.save("output_map.html")
The resulting map will be saved as "output_map.html" in the same directory.

Customization
You can customize the map center and zoom level by modifying the map_center and zoom_start variables in the plot_locations_on_map function.

python
Copy code
map_center = (latitude, longitude)  # Set the desired center coordinates
my_map = folium.Map(location=map_center, zoom_start=desired_zoom_level)
Note
If a location cannot be geocoded, its coordinates won't be included on the map.
Ensure you have an internet connection as Geopy performs online geocoding.
Feel free to explore and adapt the code for your specific needs!

