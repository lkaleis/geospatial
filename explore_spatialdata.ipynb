## This was done on Google Collab notebook

!apt-get install libgeos++ libproj-dev
!pip install geoviews

from google.colab import drive
drive.mount('/gdrive')

# Path to spatial files in google my Drive
%cd /gdrive/My Drive/Colab Notebooks/

#!pip install geopandas
#!pip install descartes
import geopandas as gpd
import descartes
import geoviews as gv
import geoviews.tile_sources as gvts
gv.extension('bokeh')
import numpy as np
import json
import pandas as pd
from geoviews import opts
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer



# load file
#l = "/gdrive/My Drive/Colab Notebooks/language/language.shp"
# Read file using gpd.read_file()
#data = gpd.read_file(l)
# make sure it read as geopandas df
#type(data)
#data.head()
#data.plot()
#data.crs

# simple absolute count of russian speakers per DAUID (dissemination area)

russian = data.groupby(['DAUID'])['HL_RUSSIAN'].agg(['sum'])
russian.head(10)
print(russian)

shapefile = '/gdrive/My Drive/Colab Notebooks/language/language.shp'

# 4ead shapefile - turn into Geopandas df
gdf = gpd.read_file(shapefile)[['CSDNAME','DAUID','geometry']]

# rename cols
gdf.columns = ['Municipality','DisseminationArea','geometry']
gdf.head()

# merge dataframes gdf and russian
#merged = gdf.merge(russian, left_on = ['CSDNAME','DAUID'], right_on = ['Municipality','DisseminationArea'])

gdf = gdf.drop_duplicates()
russian = russian.drop_duplicates()
new_df = pd.merge(gdf, russian,  how='left', left_on=['DisseminationArea'], right_on = ['DAUID'])
print(new_df)

# fill NaN cells w/ 0 count
new_df['sum'] = new_df['sum'].replace(np.nan, 0)
print(new_df)

#Read data to json
new_df_json = json.loads(new_df.to_json())

#Convert to string like object.
json_data = json.dumps(new_df_json)

# GeoJSON source which contains features for plotting
geosource = GeoJSONDataSource(geojson = json_data)

# define color palette.
palette = brewer['YlGnBu'][8]

# dark blue is highest abs. count of russian speakers
palette = palette[::-1]

# LinearColorMapper linearly maps numbers into a sequence of colors
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 1105)

# create colour bar 
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
border_line_color=None,location = (0,0), orientation = 'horizontal')

# create figure object
p = figure(title = '# of Russian Speakers', plot_height = 600 , plot_width = 950, toolbar_location = None)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# add patch renderer to figure
p.patches('xs','ys', source = geosource,fill_color = {'field' :'sum', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)

# specify figure layout
p.add_layout(color_bar, 'below')

# display figure
output_notebook()

# display figure
show(p)

russian["sum"].max()
topruski = russian['sum'].max()
topruski

# which area has highest count of russian speakers
new_df[new_df['sum'] == topruski]
