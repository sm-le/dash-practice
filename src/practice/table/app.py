# Connect data practice
# from: https://dash.plotly.com/tutorial

# Import packages
# import dash_table additionally to display data inside a Dash DataTable.
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
# Read csv file with pandas package.
# Instead we can use a local csv or excel file using read_csv and read_excel respectively.
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
# In additional title defined by inner html.Div, we add DataTable component and use pandas dataframe
app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=20)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)