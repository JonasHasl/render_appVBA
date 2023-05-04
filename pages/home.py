import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

dash.register_page(__name__, path='/')




layout = html.Div([html.Br(),
    html.Div([html.H1('Welcome', style={'textAlign': 'center', 'color':'white', 'padding-top':'5%'}, className='headerfinvest fadeinelement')]),
    #html.Img(src=('assets/littlethingbefore.jpg'),  style={'border-radius': '100px', 'width': '6%', 'margin':'15px'})], className='parent-row'),

    html.Br(),

    html.Div([
                html.Div([
                    html.H2("Finvest", style={'textAlign':'center'}, className='headers'),
                    dcc.Markdown("Empower your investment decisions with Finvest. Analyze stocks based on custom criteria, assign weights to your favorite fundamentals, and identify top performers for your investment portfolio.")

                ], className='page-intro', style={'background-color': '#F9F9F9', 'border-radius': '8px', 'padding': '10px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),


                html.Div([
                    html.H2("Economy Insights", style={'textAlign':'center'}, className='headers'),
                    dcc.Markdown("Stay ahead with real-time economic data. Get a comprehensive overview of the current state of the economy, powered by data from diverse sources including the FRED API.")
                ], className='page-intro',
                style={'background-color': '#F9F9F9', 'border-radius': '8px', 'padding': '10px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
                html.Br(),
                html.Div([
                    html.H2("VBA Automation", style={'textAlign':'center'}, className='headers'),
                    dcc.Markdown("Maximize productivity with VBA. Learn how to automate repetitive tasks in Microsoft Office and streamline your workflows, saving time and increasing efficiency.")
                ], className='page-intro',
                style={'background-color': '#F9F9F9', 'border-radius': '8px', 'padding': '10px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}
                ),
                html.Div([
                    html.H2("SQL Introduction", style={'textAlign':'center'}, className='headers'),
                    dcc.Markdown("Unlock the power of data with SQL. From basic queries to advanced database management, discover how SQL can revolutionize your data-driven decision-making process.")
                ],
                className='page-intro',
                style={'background-color': '#F9F9F9', 'border-radius': '8px', 'padding': '10px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}
                )], className='page-intros fadeinelement', style={'padding-top':'320px'}),

    html.Br(),
    html.Div([dcc.Markdown(''' Note for this version: If you're opening this web page on mobile, please use the horizontal view ''', style={'font-size':'0.8rem', 'textAlign':'center', 'font-weight':'bold'}, className='notetext')]),
html.Br(),
    html.Br(),
    html.H3("Kampen, Sylt, Schleswig-Holstein", style={'color':'white', 'font-style':'italic', 'font-weight':'lighter', 'position':'absolute', 'bottom':'10px', 'left':'10px'})
],
style={'background-image': 'url("/assets/pretty3.JPG")',
    'background-size': 'cover',
    'background-position': 'center',
    'min-height': '100vh',
    'position': 'relative'},
)
#, className='homecard fadeinelement',