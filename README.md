# Streamlit - Selectable Scatterplot in Plotly.js

Companion code for Dev.to [Streamlit components - Scatterplot with selection using Plotly.js](https://dev.to/andfanilo/streamlit-components-scatterplot-with-selection-using-plotly-js-3d7n)

```python
import random
import plotly.express as px
import streamlit as st
from streamlit_scatterplot_selection import st_scatterplot

@st.cache
def random_data():
	return random.sample(range(100), 50), random.sample(range(100), 50)

st.subheader("Plotly interactive scatterplot")
x, y = random_data()
fig = px.scatter(x=x, y=y, title="My fancy plot")
v = st_scatterplot(fig)
st.write(v)
```

## Development

### Install

- JS side

```shell script
cd frontend
npm install
```

- Python side

```shell script
conda create -n streamlit-scatterplot-selection python=3.7
conda activate streamlit-scatterplot-selection
pip install -e .
```

### Run

Both webpack dev server and Streamlit should run at the same time.

- JS side

```shell script
cd frontend
set NODE_OPTIONS="--max-old-space-size=8192"
npm run start
```

- Python side

```shell script
streamlit run streamlit_scatterplot_selection/__init__.py
```

## References

- https://stackoverflow.com/questions/53230823/fatal-error-ineffective-mark-compacts-near-heap-limit-allocation-failed-javas
