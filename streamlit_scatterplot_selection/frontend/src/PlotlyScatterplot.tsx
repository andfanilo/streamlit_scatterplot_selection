import React from "react"
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib"
import Plot from "react-plotly.js"

const PlotlyScatterplot = (props: ComponentProps) => {
  const { data, layout, frames, config } = JSON.parse(props.args.spec)

  const handleSelected = function (eventData: any) {
    Streamlit.setComponentValue(
      eventData.points.map((p: any) => {
        return { index: p.pointIndex, x: p.x, y: p.y }
      })
    )
  }

  return (
    <Plot
      data={data}
      layout={layout}
      frames={frames}
      config={config}
      revision={0}
      onSelected={handleSelected}
      onInitialized={() => Streamlit.setFrameHeight()}
    />
  )
}

export default withStreamlitConnection(PlotlyScatterplot)
