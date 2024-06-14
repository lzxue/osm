import numpy as np
import pandas as pd
import streamlit as st
import osmnx as osm
from geo import get_aoi,amap_geocode,records_from_geo_interface,renderChoroplethMap

st.set_page_config(
    page_title="OSM Map",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded"
)
col1, col2, col3 = st.columns(3)
background_color = col1.color_picker("选择背景颜色", "#fff")
line_color = col1.color_picker("选择路网颜色", "#000")

radius = col2.slider("设置地图半径：米", min_value=500, max_value=10000, value=5000, step=100)
address=col3.text_input("请输入地图中心", "北京环球金融中心")

addressGeo= get_aoi(address=address,radius=radius)

point,formatted_address = amap_geocode(address)
lng,lat = point
st.write(formatted_address,point)

fivekm_buffer_nw = osm.features_from_point((lat,lng),tags={
       "highway": [
            "motorway",
            "trunk",
            "primary",
            "secondary",
            "tertiary",
            "cycleway",
            "residential",
            "service",
            "unclassified",
            "footway",
            "motorway_link",
        ],
        # "natural": ["water", "bay"],
        # "place": ["sea"],
    },dist=radius)

renderChoroplethMap(records_from_geo_interface(fivekm_buffer_nw),line_color,background_color)