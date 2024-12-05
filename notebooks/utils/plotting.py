import plotly.graph_objects as go
import pandas as pd

def candlestick_plotting(data: pd.DataFrame) -> go.FigureWidget:
    """Generates an interactive candlestick chart with dynamic y-axis adjustment.

    Args:
        data (pd.DataFrame): A DataFrame containing OHLC (Open, High, Low, Close) data 
            with a datetime index. 
            Expected columns: ['open', 'high', 'low', 'close']

    Returns:
        go.FigureWidget: A Plotly candlestick chart widget with dynamic y-axis scaling.
    """

    # Create the candlestick trace using OHLC data
    trace = go.Candlestick(
        x=list(data.index),               # Time values for x-axis
        open=list(data['open']),           # Opening prices
        high=list(data['high']),           # High prices
        low=list(data['low']),             # Low prices
        close=list(data['close'])          # Closing prices
    )

    # Define the layout for the chart
    layout = dict(
        title='Candlestick Chart',         # Title of the chart
        xaxis=dict(
            rangeslider=dict(
                visible=False             # Disable the range slider for x-axis
            ),
            type='date'                   # Set x-axis to date type
        ),
        height=500                          # Set the figure height
    )

    # Create the Plotly figure widget
    fig = go.FigureWidget(data=[trace], layout=layout)

    def zoom(layout: dict, xrange: list) -> None:
        """Adjusts the y-axis range dynamically based on the visible x-axis range.

        Args:
            layout (dict): The layout object from Plotly to manage axis settings.
            xrange (list): The current range of the x-axis being viewed as [min, max].
        """
        # Get the current x-axis range (visible time window)
        x_min = fig.layout.xaxis.range[0]
        x_max = fig.layout.xaxis.range[1]
        
        # Filter the data to include only the points within the visible range
        in_view = data.loc[x_min:x_max]
        
        # Update the y-axis range based on the visible high and low values
        y_min = in_view['low'].min()      # Minimum low value in the visible range
        y_max = in_view['high'].max()     # Maximum high value in the visible range
        fig.layout.yaxis.range = [y_min - 100, y_max + 100]  # Add padding for clarity

    # Attach the zoom function to the x-axis range change event
    fig.layout.on_change(zoom, 'xaxis.range')

    return fig
