import json
import os 
import random

import plotly.utils
import plotly.express as px  
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_scatterplot_selection",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_scatterplot_selection", path=build_dir)


def st_scatterplot(fig, key="st_plotly"):
    spec = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    selected_points = _component_func(spec=spec, default=[], key=key)
    return selected_points


if not _RELEASE:
    import streamlit as st

    @st.cache
    def random_data():
        return random.sample(range(100), 50), random.sample(range(100), 50)

    st.subheader("Plotly interactive scatterplot")
    x, y = random_data()
    fig = px.scatter(x=x, y=y, title="My fancy plot")
    v = st_scatterplot(fig)
    st.write(v)
