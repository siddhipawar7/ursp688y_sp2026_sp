## Research Question: Is there a correlation between high school graduation rates and proximity of security cameras?  

## Outline:  

This research question will be investigated in ArcGIS Pro rather than through Python code.
The first step is to find shapefiles for my study areas, Baltimore City, Baltimore County, and D.C.. These shapefiles have to contain the school districts or 
boundary limits for high schools. In addition, I will have to either find CSV or other files that contain the high school graduation rate by high school. After
that, I will need to find another shapefile that contains all, or as many as possible, security camera locations for my study areas.  

All these files then need to be uploaded to an ArcGIS project and the graduation rates combined with high school districts. The points of the security cameras
then need to be overlaid. Hopefully, this information is readily available through local government or police datasets. If not, it might require manual input
or the use of Surveillance under Surveillance, which after further investigation may have missed many security camera locations.  

Analysis can then be conducted. Regression analysis can be conducted by seeing how many security cameras intersect with a district and correlating that with the 
graduation rate of the high school. Further analysis can also be conducted by proximity. If the locations of the schools are included, proximity analysis could
be conducted by grouping security cameras and gauging their distance to their closest high school. Again, regression analysis could then be conducted to see if
there is any correlation between proximity and graduation rates.  