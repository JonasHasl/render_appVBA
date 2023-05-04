import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output

dash.register_page(__name__, path='/VBA')
colors = {
    'background': '#D6E4EA',
    'text': '#718BA5',
    'accent': '#004172',
    'text-white':'white',
    'content':'#EDF3F4'
}
fonts = {
    'heading': 'PT Serif',
    'body': 'Abel'
}

card_content = html.Div([html.H1("VBA in MS Office: Tailored Solutions", className="headerfinvest", style={}), html.P("Unlocking the Power of VBA for workflows in MS Office: Enhancing Efficiency and Driving Business Growth", className=""),        html.Hr(),        dbc.Row([        dbc.Col([            html.P("VBA is a powerful tool for improving your organization's efficiency and removing repetitive work for your employees. Customized solutions in VBA not only enhance operational efficiency, but also empower your employees to achieve their full potential by providing them with a streamlined and user-friendly workflow.", style={'textAlign':'center'}),        ], width=7),
        dbc.Col([], width=2), dbc.Col([dbc.CardImg(src="",style={'display': 'block'})], width=3, style={'text-align': 'right'}),
    ], className='parent-container'),
], className='headers', style={
        'text-align': 'center',
    })


# Define the card and tabs


tabs = dbc.Tabs(
    [dbc.Tab(label="VBA", tab_id="vba", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'font-size':'1.5rem', 'text-transform': 'none'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label="Macros", tab_id="macros", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'font-size':'1.5rem', 'text-transform': 'none'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label='UserForms: "Mini Applications"', tab_id="userforms", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'font-size':'1.5rem', 'text-transform': 'none'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label='Projects', tab_id="previousprojects", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'font-size':'1.5rem', 'text-transform': 'none'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     ],
    id="tabs2",
    active_tab="vba",
    className='tabs-line',
    style={
    }
)

#Define the content for each tab


vba_tab = html.Div([html.Div(
    [
        html.H2("VBA", className='tabheaders'),
        html.P("Visual Basic for Applications (VBA) is a programming language that is widely used to create powerful, automated solutions in Microsoft Office applications such as Excel, Word, and Access. It enables users to automate repetitive tasks, build user-friendly interfaces, and manipulate data in complex ways, making it an ideal tool for anyone looking to streamline their workflow."),
                            html.Br(),
                            html.P("Additionally, VBA can be used to create user-friendly interfaces that allow non-technical users to interact with complex systems in a simple and intuitive way. VBA can also be used to enhance efficiency and productivity in business operations. By automating tasks such as data entry, report generation, and financial analysis, VBA can help businesses reduce errors and improve the accuracy of their data. This, in turn, can lead to better decision-making and increased profitability. Overall, VBA is a powerful tool that can help businesses and individuals work smarter, not harder. By automating repetitive tasks and freeing up time for more important work, VBA can help individuals focus on tasks that require their unique skills and expertise, ultimately leading to increased productivity, efficiency, and job satisfaction.")

    ],
    className="card-item",
    style={
        'border': 'none',
        'text-align': 'center',
        'background':'white'
    }
)], style={
        'height': '100vh'
    }
)

macros_tab = html.Div(
    [html.Div([#'border-radius':'10px'
        html.H2("Macros", style={}, className='tabheaders'),
        html.P("Macros are a set of instructions that automate repetitive tasks in programs such as Microsoft Excel. Macros can save time and reduce the chance of errors by automating these tasks, which can range from simple formatting to more complex calculations. For example, you can create a macro that automatically applies formatting to a large set of data, or a macro that performs a series of calculations and presents the results in a specific format. Macros can also be customized to fit specific needs and requirements, making them a powerful tool for streamlining workflows and increasing productivity. With macros, users can focus on more important tasks that require unique skills and expertise, while allowing the program to handle repetitive tasks efficiently.", style={}, className=''),


    ], className="card-item",
    style={
        'text-align': 'center',
                'border-radius': '10px',
'background':'white'
    }
)], style={'height': '100vh',}
)

userform_tab = html.Div([html.Div(
    [
        html.H2("UserForms", style={},className='tabheaders'),
        html.Div([
                    html.P("UserForms in VBA are like mini applications that can be created within Excel to provide a more user-friendly and interactive interface for data input and manipulation. With UserForms, users can input data more easily and accurately, and perform complex operations with just a few clicks. UserForms can be used for a variety of tasks, such as data entry, report generation, and even creating custom dialog boxes. They can also be customized with various controls, such as text boxes, drop-down lists, and buttons, to provide a more intuitive and engaging experience. By using UserForms, businesses can enhance their data management processes, streamline their operations, and free up time for employees to focus on more important tasks.")
                ]),
            html.Div([dbc.CardImg(
                src="assets/userform.png",
                top=True,
                style={'width': '60%', 'height': '60%'}
            )], ),

], className='card-item', style={'background':'white'})],style={'height': '100vh'})












@callback(
Output("tab-content2", "children"),
[Input("tabs2", "active_tab")],
)
def render_tab_content(active_tab):
    if active_tab == "vba":
        return vba_tab
    elif active_tab == "macros":
        return macros_tab
    elif active_tab == "userforms":
        return userform_tab
    elif active_tab == "previousprojects":
        return previousprojects_tab

#Define the previous projects tab

previousprojects_tab = html.Div([html.Div([
html.H2("Projects", className='tabheaders')]),


    html.Div([html.Div([html.Div([dbc.CardImg(
                    src="assets/search.png",
                    top=True,
                    style={'width':'70%', 'height':'70%'}
                    )],style={ 'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center'}),
                #'height': '100%'}),
                html.Div(
                    [
                        html.H4(
                            "Quick Searches",
                            className="card-title",
                            style={'background':'white',
                   'color':colors['text']}
                            ),
                        html.P(
                            "By assigning macros to shortcut keys, users can efficiently access and retrieve data from a variety of web pages. This powerful functionality can significantly reduce the time and effort required for data lookup, freeing up valuable resources for other high-priority tasks. Whether used for research, analysis, or other purposes, the ability to swiftly navigate and retrieve information from the web can be a game-changer for businesses seeking to maximize their productivity and competitiveness. By leveraging automation and advanced technology in this way, organizations can unlock new opportunities for growth and innovation, empowering their workforce to achieve more and reach their full potential.",
                            className="card-text",
                            style={'background':colors['text-white'],
                   'color':colors['text']}
                            ),
                        ]
                    ),
                ],className='page-intro',
            style={#"width": "14rem",
                   'background':colors['text-white'],
                   'color':colors['text']},
            ),
    html.Div([
        html.Div(
            [
                html.Div([dbc.CardImg(
                    src="assets/text.png",
                    top=True,
                    style={'width':'60%', 'height':'60%', 'text-align':'center'}
                    )],style={ 'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center'}),
                #'height': '100%'}),
                html.Div(
                    [
                        html.H4(
                            "Text Generators",
                            className="card-title",
                            style={'background':colors['text-white'],
                                   'color':colors['text']}
                            ),
                        html.P(
                            "Leveraging input data from Excel sheets, macros can automatically generate summaries and other textual outputs that are often required to be produced. This capability can streamline and enhance the efficiency of various workflows, enabling professionals to focus on high-value tasks while still ensuring accurate and high-quality deliverables. By harnessing the power of automation, organizations can increase productivity, optimize resource utilization, and unlock new opportunities for growth and innovation.",
                            className="card-text",
                            style={'background':colors['text-white'],
                                   'color':colors['text']}
                            ),
                        ]
                    ),
                ],
            style={#"width": "14rem",
                   'background':'text-white',
                   'color':'black'},
            ),
        ],className='page-intro',),
    html.Div([
        html.Div([
                dbc.CardImg(
                    src="assets/data.png",
                    top=True,
                    #style={'height': '100%'}
                    ),
                html.Div(
                    [
                        html.H4(
                            "Data UserForms",
                            className="card-title",
                            style={'background':colors['text-white'],
                   'color':colors['text']}
                            ),
                        html.P(
                            "By utilizing data from other Excel sheets, UserForms can provide employees with a user-friendly interface for swiftly retrieving relevant information. Additionally, shortcut keys can be assigned to refresh the UserForms, thereby optimizing and accelerating the data retrieval process. These functionalities can significantly boost productivity and efficiency, enabling organizations to make the most of their resources and achieve their goals with greater ease and effectiveness.",
                            className="card-text",
                            style={'background':colors['text-white'],
                   'color':colors['text']}
                            ),
                        ]
                    ),
                ],#"width": "14rem",
            style={'background':colors['text-white'],
                   'color':colors['text']})], className='page-intro',
        ),
    ], className='page-intros', style={'height': '100vh auto'})])

#Define the resume tab
resume_tab = html.Div(
    [
     html.H2("Resume"),
     html.A("Download my resume", href="/assets/resume.pdf", target="_blank"),
     ]
    )

layout = dbc.Container(
    [
        card_content,
        tabs,
        dbc.Container(
            [
                html.Div(id="tab-content2"),
            ], style={'width':'90%',
                      'border-radius': '10px',
                      },
            #className="mt-4",
        ),
    ],
    fluid=True,
    className='parent-container',
    style={
    'min-height': '100vh'
}
)
