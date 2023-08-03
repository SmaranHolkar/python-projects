import requests
import json
import pandas as pd
import plotly.express as px

# Make a request to get flood data
flood = requests.get("http://environment.data.gov.uk/flood-monitoring/id/floods")
response_json = json.loads(flood.text)

# Normalize the response into a pandas dataframe
df = pd.json_normalize(response_json['items'])

# Get the polygon data for each flood
poly_df = []
for polygon in df['floodArea.polygon']:
    flood = requests.get(polygon)
    response_json = json.loads(flood.text)
    poly_df.append(response_json)

# Merge the polygon data with the original dataframe
df['polygon_response'] = poly_df

# Remove any warnings that are no longer in force
df = df[df['severity'] != 'Warning no longer in force']

# Create a list of GeoJSON features from the polygon data
features = []
for polygon in df['polygon_response']:
    features.append({"type": "Feature", "geometry": polygon})

# Create a GeoJSON object
geojson = {"type": "FeatureCollection", "features": features}

# Add the polygons to the map
fig = px.choropleth_mapbox(df, geojson=geojson, locations=df.index, 
                           color='severity', color_discrete_sequence=['#FF0000','#000000'],
                           mapbox_style="open-street-map",
                           center={"lat": 52, "lon": -2}, zoom=4)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
