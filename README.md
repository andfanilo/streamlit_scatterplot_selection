# Streamlit - Selectable Scatterplot in Plotly.js

Companion code for Dev.to [Streamlit components - Scatterplot with selection using Plotly.js](https://dev.to/andfanilo/streamlit-components-scatterplot-with-selection-using-plotly-js-3d7n)

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
npm run start
```

- Python side

```shell script
streamlit run streamlit_scatterplot_selection/__init__.py
```

## References

- https://stackoverflow.com/questions/53230823/fatal-error-ineffective-mark-compacts-near-heap-limit-allocation-failed-javas
