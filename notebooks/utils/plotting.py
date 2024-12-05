import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def candlestick_plot(data: pd.DataFrame,
                         title: str) -> go.FigureWidget:
    """Generates an interactive candlestick chart with dynamic y-axis adjustment.

    Args:
        data (pd.DataFrame): A DataFrame containing OHLC (Open, High, Low, Close) data 
            with a datetime index. 
            Expected columns: ['open', 'high', 'low', 'close']
        
        title (str): Chart name

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
        title=f'Candlestick Chart: {title}',         # Title of the chart
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

def local_maxima_minima_plot(x_data: list,
                             y_data: list,
                             x_pol: np.ndarray, 
                             y_pol: np.ndarray, 
                             l_min: np.ndarray, 
                             l_max: np.ndarray) -> None:
    """
    Plots the stock data and its polynomial fit, highlighting local maxima 
    and minima.

    Args:
        x_data (list): The x-axis values for the original stock data.
        y_data (list): The y-axis values (e.g., prices) for the original stock data.
        x_pol (np.ndarray): The x-axis values for the polynomial fit.
        y_pol (np.ndarray): The y-axis values for the polynomial fit.
        l_min (np.ndarray): Indices of local minima in the polynomial fit.
        l_max (np.ndarray): Indices of local maxima in the polynomial fit.

    Returns:
        None: The function generates and displays a plot but does not return any value.
    """
    
    # Set up the figure with size, resolution, and styling.
    plt.figure(figsize=(15, 5), dpi=120,
               facecolor='w', edgecolor='k')

    # Plot the original stock data as grey dots.
    plt.plot(x_data, y_data, 'o',
             markersize=2, color='grey')

    # Plot the polynomial fit as a black line.
    plt.plot(x_pol, y_pol, '-',
             markersize=1.0, color='black')

    # Highlight the local maxima with blue markers.
    plt.plot(x_pol[l_max], y_pol[l_max],
             "o", label="max", color='blue')

    # Highlight the local minima with red markers.
    plt.plot(x_pol[l_min], y_pol[l_min],
             "o", label="min", color='red')

    # Add a legend to label the data series in the plot.
    plt.legend(['Stock Data',
                'Polynomial Fit',
                'Local Maxima',
                'Local Minima'])

    # Display the plot.
    plt.show()