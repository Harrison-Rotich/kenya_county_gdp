# Kenya County GDP Visualization

A Python-based geospatial analysis project that visualizes GDP indices across Kenya's counties using interactive choropleth mapping.

## Overview

This project processes Kenya's administrative boundaries and generates an interactive map displaying GDP distribution by county. The visualization uses color gradients to represent economic metrics, enabling quick identification of regional economic patterns.

## Features

- **Geospatial Data Processing**: Loads and processes Kenya's county boundaries from GeoJSON format
- **Interactive Choropleth Map**: Color-coded county visualization with GDP index values
- **Tooltip Information**: Hover over counties to view detailed county names and GDP metrics
- **Data Integration**: Merges spatial and attribute data seamlessly
- **Web Export**: Generates an HTML map file for easy sharing and viewing

## Dependencies

The project requires the following Python libraries:

- `geopandas` - Geospatial data analysis
- `folium` - Interactive mapping
- `pandas` - Data manipulation and analysis
- `mapclassify` - Classification schemes for choropleth mapping

## Installation & Usage

1. **Upload Data**: Run the script in Google Colab to upload the `gadm41_KEN_1.json.zip` shapefile
2. **Install Dependencies**: Execute the pip install command to set up required packages
3. **Run the Script**: The script automatically:
   - Extracts the shapefile
   - Generates synthetic GDP data
   - Creates an interactive choropleth map
   - Saves output as `kenya_county_gdp.html`
4. **View Results**: Open the generated HTML file in any web browser

## Project Structure

```
kenya_county_gdp/
├── kenya_gdp.py              # Main analysis script
├── README.md                 # This file
└── kenya_county_gdp.html     # Generated map output
```

## Data Source

- **Boundaries**: GADM (Global Administrative Areas) v4.1 Kenya county boundaries
- **GDP Data**: Synthetically generated for demonstration purposes

## Output

The project generates an interactive map centered on Kenya displaying:
- County boundaries
- GDP index values (color-coded from yellow to red)
- County names and GDP metrics on hover
- CartoDB basemap for geographic context

## Notes

- This project uses synthetic GDP data for demonstration. Replace with actual economic data for production use
- Map is optimized for web viewing with responsive zoom and pan controls
- Requires internet connection for Colab and folium map rendering

## License

Open source - Feel free to use and modify for your needs.
