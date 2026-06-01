from google.colab import files
uploaded = files.upload() # Directs you to upload zip file here

# importing libraries and modules
! pip install geopandas folium mapclassify

import geopandas as gpd
import folium
import pandas as pd
import zipfile
import os

# Unzip the shapefile
with zipfile.ZipFile('gadm41_KEN_1.json.zip', 'r') as z:
    z.extractall('kenya_shapefile')
  # Load shapefile
kenya = gpd.read_file('kenya_shapefile/gadm41_KEN_1.json')
print(kenya.columns)
print(kenya['NAME_1'].unique()) #Show county names
# Create data
county_data = pd.DataFrame({
    'County': kenya['NAME_1'].tolist(),
    'GDP_Index': [round(x,1)for x in 
                  pd.Series(range(len(kenya))).sample(frac=1).reset_index(drop=True) *2.3 + 10]
    
})
# Merge spatial + attribute data
kenya = kenya.merge(county_data, left_on='NAME_1', right_on='County')
# Convert to WGS84 for folium
kenya = kenya.to_crs('EPSG:4326')

# Create choropleth map
m = folium.Map(location=[0.0236, 37.9062], zoom_start=6,
               tiles='CartoDB positron')
folium.Choropleth(
    geo_data=kenya,
    data=kenya,
    columns=['County', 'GDP_Index'],
    key_on='feature.properties.NAME_1',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='GDP Index by County'
).add_to(m)

# Add county name tooltips
folium.GeoJson(
    kenya,
    tooltip=folium.GeoJsonTooltip(
        fields=['NAME_1', 'GDP_Index'],
        aliases=['County:', 'GDP Index:']
    )
).add_to(m)

m.save('kenya_county_gdp.html')
print("Choropleth map created!")
