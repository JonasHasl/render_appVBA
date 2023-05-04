import dash
import dash_bootstrap_components as dbc

from dash import html

dash.register_page(__name__, path='/Contact')

colors = {
    'background': '#D6E4EA',
    'text': '#718BA5',
    'accent': '#004172',
    'text-white':'white',
    'header': '#004172'
}

layout = dbc.Card([dbc.CardBody([html.H1("Contact", className="headerfinvest", style={'text-align':'center'}),
         html.Div([
             html.Div([
                    html.P("If you have any questions or inquiries, please feel free to contact me using the information below:"),
                    html.Hr(),
                    html.P("Email: jonas_fbh@hotmail.com"),
                    html.P("LinkedIn: https://www.linkedin.com/in/jonashasl"),
                    html.P("Phone: +47 45101329")], style={'background': 'white', 'border-radius': '10px', 'color': colors['text'], 'text-align': 'center', 'padding':'20px'}, className=''),
         ], className='parent-container'),],)],

    #className="mt-5",
    style={
        'background-color': 'white',
        'border-radius':'10px',
        'min-height': '100vh'
    }
)

