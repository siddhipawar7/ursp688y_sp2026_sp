Evaluating the Equity of Urban Heat Mitigation in Transit-Oriented Development Districts in Maryland
An assessment of tree canopy, land surface temperature, and environmental justice

**Author:** Siddhi Pawar 
**Course:** URSP688Y: Urban Data Science & Smart Cities 
**Professor:** Dr. Chester Harvey 
**Date:** April 29, 2026 

--- 

## Notebook Contents
This notebook presents the approach, pseudocode, prelimiary code, and future steps for the proposed research. A portion of this analysis has been, and will be, conducted in ArcGIS Pro, specifically in standardizing and processesing the raw raster files for LST, tree canopy, and impervious surface data. Zonal statistics for these variables will also done in ArcGIS Pro to geographically attribute these characteristics to the respective census tracts. Zonal statistics CSVs will be imported for the environmental analysis portion of this research. 

--- 

## Large Data Files
This exercise utilizes an external course Google Drive (688y_final_project_data) to store the following data files needed for this project: 
- 2024 ACS Census tract boundaries shapefile
- Maryland TOD boundaries shapefile
- Landsat 9 scene for Land Surface Temperature (will be provided)
- NLCD 2021 Tree Canopy raster CSV (will be provided)
- NLCD Impervious Surface raster CSV (will be provided)
These can all be copy and pasted in the same directory as this notebook.

Additionally, a personal Census API key will be required to get data from the the ACS. Please obtain one at https://api.census.gov/data/key_signup.html
When prompted in the code, replace 'YOUR_API_KEY_HERE' with your personal key.


