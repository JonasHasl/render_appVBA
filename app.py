from dash import html, dcc
import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=['custom.css', 'missing.css'],
                meta_tags=[{'name' :'viewport', 'content':'width=device-width, initial-scale=0.5, height=device-height'}])


server = app.server

colors = {
    'background': '#D6E4EA',
    'text': '#718BA5',
    'accent': '#004172',
    'text-white':'white',
    'header': '#004172'
}

header = html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Home",
                                                        href="/",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "transparent",
                                                            "color": '#eee',
                                                            'text-transform': 'none'
                                                        },
                                                    ),
                                                    width="auto",
                                                ),
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Finvest",
                                                        href="/Finvest",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "transparent",
                                                            'color':'#eee',
                                                            'text-transform': 'none'
                                                        },
                                                    ),
                                                    width="auto",
                                                ),
                                                dbc.Col(
                                                    dbc.Button(
                                                        "Economy Overview",
                                                        href="/economy",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "transparent",
                                                            'color':'#eee',
                                                            'text-transform': 'none'
                                                        },
                                                    ),
                                                    width="auto",
                                                ),
                                                dbc.Col(
                                                    dbc.Button(
                                                        "VBA Solutions",
                                                        href="/VBA",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "transparent",
                                                            'color':'#eee',
                                                            'text-transform': 'none'
                                                        },
                                                    ),
                                                    width="auto",
                                                ),

                                                dbc.Col(
                                                    html.A(
                                                        "SQL Introduction",
                                                        href="/SQL",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "",
                                                            'color':'black',
                                                            #'text-transform': 'none'
                                                        },
                                                    ),
                                                    width="auto",
                                                ),

                                                dbc.Col(
                                                    dbc.Button(
                                                        "Contact",
                                                        href="/Contact",
                                                        className="",
                                                        style={
                                                            "border": "none",
                                                            "background-color": "transparent",
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'textAlign':'right'

                                                        },
                                                    ),#,,fluid=True,,
#headerstab
                                                ) #className='parent-container',
                                            ],className='parent-row ',style={},
                                        ), #className="navbar navbar-expand-lg",
                                                       # style={'color':colors['text']}
    ],style={'color':'#eee','background':'#487890', 'height':'100px'},
)

header_banner = dbc.Navbar(
    [

        dbc.Nav(
            [html.H1("Jonas Hasle", style={'font-size':'2rem', 'font-weight':'bold', 'color': '#eee', 'margin-right': 'auto', 'margin-left':'20px'}),
                dbc.NavItem(dbc.NavLink("Home", href="/", style={
                                                            "border": "none",
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'font-size':'24px',
                                                            'textAlign':'right'

                                                        },)),
                dbc.NavItem(dbc.NavLink("Finvest", href="/Finvest", style={
                                                            "border": "none",
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'font-size':'24px',
                                                            'textAlign':'right'

                                                        },)),
                dbc.NavItem(dbc.NavLink("Economy Overview", href="/economy", style={
                                                            "border": "none",
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'font-size':'24px',
                                                            'textAlign':'right'

                                                        },)),
                dbc.NavItem(dbc.NavLink("VBA Solutions", href="/VBA", style={
                                                            "border": "none",
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'font-size':'24px',
                                                            'textAlign':'right'

                                                        },)),
                dbc.NavItem(dbc.NavLink("SQL Introduction", href="/SQL", style={
                                                            "border": "none",
                                                            'font-size':'24px',
                                                            "color": '#eee',
                                                            'text-transform': 'none',
                                                            'textAlign':'right'

                                                        },)),
            ],
            style={},
            className='banner-row',
            navbar=True
        ),
    ],
    sticky="top",
    className='headerbanner',
    color='#18344a'
)

menu = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Link 1', 'value': 'link1'},
            {'label': 'Link 2', 'value': 'link2'},
            {'label': 'Link 3', 'value': 'link3'}
        ],
        placeholder='...',
        searchable=False,
        clearable=False,
        style={
            'position': 'absolute',
            'top': '10px',
            'right': '10px',
            'width': '150px',
            'border': 'none',
            'background-color': 'transparent',
            'font-size': '1.2em',
'           dropdownIndicator': {
                'color': 'white'}
        },
        #indicator_style={
        #    'display': 'none'
        #}
    )
])

contact = html.Div([
    html.H3("Contact Information"),
    html.A("jonas_fbh@hotmail.com", href="mailto:jonas_fbh@hotmail.com"),
    html.Br(),
    html.A("https://www.linkedin.com/in/jonashasl", href="https://www.linkedin.com/in/jonashasl"),
    html.Br(),
    html.A("+47 45101329",href="tel:+4745101329")],
    style={'color':'white', 'font-weight':'normal', 'textAlign':'center'}, className='footer-left')

app.layout = html.Div([
    header_banner,
    dash.page_container,
    html.Div([contact], className='footer')
], style={'margin-top':'0'},
) #className='parent-container')

# Define different styles for different screen sizes using CSS media queries



if __name__ == '__main__':
	app.run_server(debug=True)