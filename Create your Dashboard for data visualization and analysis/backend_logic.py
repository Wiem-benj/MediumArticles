import base64
import io
import pandas as pd
from dash import dcc
import plotly.express as px

def line_plot(xaxis, yaxis, color, df):

    figure = px.line(df,
        x = xaxis,
        y = yaxis,
        color = color,
        title = 'Line chart')
    
    return figure

def scatter_plot(xaxis, yaxis, color, df):
    figure = px.scatter(df,
                        x = xaxis,
                        y = yaxis,
                        color = color,
                        title = 'Scatter plot')
    
    
    return figure


def area_plot(xaxis, yaxis, color, df):

    figure = px.area(df,
                     x = xaxis,
                     y = yaxis,
                     color = color,
                     title = 'Area plot')

    return figure


def bar_plot(xaxis, yaxis, color, df):

    # If xaxis and color are the same column and no yaxis is selected then there wouldn't be a plot generated
    if yaxis is None and xaxis == color:
        return None
    elif yaxis is None:
        # For the Bar chart specifically we allow the yaxis to be not selected by the user and in this case we treat it
        # as the count of the xaxis
        yaxis = 'count'

        group = [xaxis, color] if color is not None else xaxis

        df = df.groupby(group).size().reset_index(name='count')

    figure = px.bar(df,
                    x = xaxis,
                    y = yaxis,
                    color = color,
                    title = 'Bar Plot')

    return figure


def read_data(contents, filename):
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    try:
        if '.csv' in filename.lower():
            # Read CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return None
    
    return df
    
def generate_graph(chart_type, xaxis, yaxis, color, df):

    graph = None
    if chart_type[0] == 'L':
        figure = line_plot(xaxis, yaxis, color, df)

    elif chart_type[0] == 'S':
        figure = scatter_plot(xaxis, yaxis, color, df)

    elif chart_type[0] == 'A':
        figure = area_plot(xaxis, yaxis, color, df)

    elif chart_type[0] == 'B':
        figure = bar_plot(xaxis, yaxis, color, df)
        
    if figure is not None:
        figure.update_layout(paper_bgcolor = '#333333', title_font = dict(color = 'white'),
                             legend_font = dict(color = 'white'))
        figure.update_xaxes(
        tickfont=dict(color="white"),  # X-axis ticks
        title_font = dict(color = 'white')
            )

        figure.update_yaxes(
            tickfont=dict(color="white"),  # Y-axis ticks
            title_font = dict(color = 'white')
        )
        graph = dcc.Graph(figure = figure)

    return graph

