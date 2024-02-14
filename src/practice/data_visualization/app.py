# Connect data practice
# from: https://dash.plotly.com/tutorial

# Import packages
# import dcc module which stands for Dash Core Components
# This module contains a Graph function for rendering graphs
# we will use plotly express to build an iteractive graph.
# To work with callback in a Dash app, we import callback as well as Output and Input
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
# Using plotly express package, we built a histogram and assign it to figure property of the dcc.Graph
# RadioItems is added on top of data table to add a control button.
# Both RadioItems and Graph components were given id names and will be used by the callback
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
# Our input is the value property of the component with controls-and-radio-item
# Our output is the figure property of the component with controls-and-graph
# The call back function's col_chosen refers to the component property of the input and assign to y-axis attribute
# we return the histogram and assigns it to the figure property of the dcc.Graph
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)