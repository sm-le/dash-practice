# Hello world practice
# from: https://dash.plotly.com/tutorial

# import Dash and html from dash
# advanced Dash apps require more packages
from dash import Dash, html

# initialze the Dash app
# It is a Dash constructor and remains unchanged for various applications.
app = Dash(__name__)

# app layout represents app components for web browser display.
# Normally it is contained within html.Div. In the example, we used another html.Div with Hello world children property.
app.layout = html.Div([
    html.Div(children='Hello World')
])

# Running dash app and remains unchanged for various applications. 
if __name__ == '__main__':
    app.run(debug=True)