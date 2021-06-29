# This python file exists because bokeh was unreliable and difficult to debug
# in ipynb files.  So eventually some of it needed to be ported back to its intended
# interface, via .py files.

# To run, copy/paste the pickle file saved from the last step into the filename
# below, and run this from an anaconda or python prompt:
#
# d: <br>
# cd Datasci\project_directory\twitter_usage <br>
# bokeh serve --show 4_bokeh_map_tweets_by_hour.py <br>

import pandas as pd
import json 
import pickle
import csv
#from bokeh.io import output_file, show, save, output_notebook, export_png, push_notebook
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool, Slider
from bokeh.models import annotations
from bokeh.plotting import figure, curdoc
#from bokeh import palettes
from bokeh.layouts import column
import colorcet

# get this from the jupyter ipynb file: 3_visualize_geotwitter.ipynb
# so that we can get the latest gdf from it and use it here
latest_pickle_file = 'bokeh_geodataframe.202105130906.pickle'

gdf2 = pd.read_pickle(latest_pickle_file)

# necessary function for using geopandas gdf with bokeh patches
def get_geodatasource(gdf):    
    """Get getjsondatasource from geopandas object"""
    json_data = json.dumps(json.loads(gdf.to_json()))
    return GeoJSONDataSource(geojson = json_data)

# start with initial data 
column_name='7'
geosource = get_geodatasource(gdf2) # the country outlines and data

#set palette
palette = colorcet.fire  # white at zero, darker at max

#Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 1)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20, 
                        location=(0,0), orientation='horizontal')

# add some nifty tools
tools = 'wheel_zoom,pan,reset'
p2 = figure(plot_height=400 , plot_width=850, toolbar_location='right', tools=tools)
p2.xgrid.grid_line_color = None
p2.ygrid.grid_line_color = None
p2.background_fill_color = 'black'
p2.background_fill_alpha = 0.95
p2.title.text = "Hour: " + column_name

#Add patch renderer to figure
disp = p2.patches('xs','ys', source=geosource, fill_alpha=1, line_width=0.5, line_color='blue',  
            fill_color={'field' :column_name , 'transform': color_mapper})

# define a callback that will get called when the time slider changes
def callback(attr, old, new):        
    column_name = str(new)
    disp = p2.patches('xs','ys', source=geosource, fill_alpha=1, line_width=0.5, line_color='blue',  
            fill_color={'field' :column_name , 'transform': color_mapper})
    p2.title.text = "Currently hour: " + column_name
    return

#Specify figure layout.
p2.add_layout(color_bar, 'below')

# Add the HoverTool to the figure
country_hover = HoverTool()
country_hover.tooltips = [('country ', '@country' + ' (' + '@cc' + ')')]
p2.add_tools(country_hover)

# Add a time slider
hour_slider = Slider(start=0, end=23, value=7, step=1, name="UTC hour slider")
hour_slider.on_change('value', callback)

# get it launched

#doc.add_root(column(slider, plot))
curdoc().add_root(column(hour_slider, p2))
