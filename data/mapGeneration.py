import folium
import pandas as pd

# Read the CSV data into a pandas DataFrame
data = pd.read_csv('restraunts.csv')

# Get latitude and longitude
latitude = (data['latitude'].min() + data['latitude'].max()) / 2
longitude = (data['longitude'].min() + data['longitude'].max()) / 2

# Create a map
map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Iterate over the rows of the DataFrame
for index, row in data.iterrows():
    name = row['name']
    address = row['street_address']
    category = row['category']
    latitude = row['latitude']
    longitude = row['longitude']

    # Create a marker for each restaurant
    marker = folium.Marker(
        location=[latitude, longitude],
        popup=f'<strong>Name:</strong> {name}<br>'
              f'<strong>Address:</strong> {address}<br>'
              f'<strong>Category:</strong> {category}'
    )

    # Add the marker to the map
    marker.add_to(map)

# Save the map as an HTML file
map.save('map.html')