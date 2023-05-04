import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, callback, Input, Output

dash.register_page(__name__, path='/SQL')


colors = {
    'background': '#D6E4EA',
    'text': '#718BA5',
    'accent': '#004172',
    'text-white':'white'
}

fonts = {
    'heading': 'Helvetica Neue, Helvetica, sans-serif',
    'body': 'Helvetica, sans-serif'
}


image_src = r'assets/sql2.png'
# Define content for the card

card_content = html.Div([html.Div([html.H1("SQL Simplified ", className="headerfinvest", style={}), html.P("Your Comprehensive Resource for Database Development", className="card-text"), html.Hr(), dbc.Row([        dbc.Col([            html.P("SQL is the preferred language for managing relational databases for several reasons. Firstly, SQL is a standardized language, meaning it can be used with different database management systems (DBMS) such as MySQL, Oracle, Microsoft SQL Server, and PostgreSQL. This allows developers and administrators to switch between DBMSs without having to learn a new language. Secondly, SQL is a declarative language, which means that users can specify what they want to do with the data, without having to worry about how to do it. This makes SQL easy to learn and use, even for beginners. Finally, SQL is a highly optimized language, with built-in features for indexing, sorting, and filtering data, making it highly efficient for managing large datasets. All of these factors contribute to SQL's popularity and make it an essential tool for managing databases.", style={'textAlign':'center'})], width=7),
        dbc.Col([], width=2), dbc.Col([dbc.CardImg(src="",style={'display': 'block'})], width=3, style={'text-align': 'right'}),
    ], className=''),
], className='', style={'display':'absolute'})])


# Define the card and tabs

tabs = dbc.Tabs(
    [dbc.Tab(label="Introduction to SQL", tab_id="intro", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'text-transform': 'none' ,'font-size':'1.5rem',}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label="SQL Operations and Syntax", tab_id="syntax", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'text-transform': 'none','font-size':'1.5rem'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label='Database Structure', tab_id="structure", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'text-transform': 'none','font-size':'1.5rem'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     dbc.Tab(label='Kimball Methodology', tab_id="kimball", label_style={'color':colors['text-white'], 'backgroundColor':'#004172', 'text-transform': 'none','font-size':'1.5rem'}, active_label_style = {"backgroundColor": "#8EA9C1", 'text-transform': 'none'}),
     ],
    id="tabs",
    active_tab="intro",
    className='tabs-line',
    style={
    }
)

#Define the content for each tab


intro_tab = html.Div([dbc.Card([ dbc.CardBody([


                            html.P("Welcome to SQL Mastery: The Ultimate Guide to Database Management! SQL (Structured Query Language) is a powerful programming language that is used to manage and manipulate relational databases. Whether you're a data analyst, database administrator, or software developer, SQL is an essential skill for anyone working with data."),
                            html.Br(),
                            html.P("In this introduction, we'll cover the basics of SQL, including its purpose, syntax, and various components. You'll learn how to use SQL to query and manipulate data, create and modify tables, and much more. Whether you're a beginner or an experienced user, this page will provide you with a solid foundation in SQL programming."),
                            html.Br(),
                            html.P("To get started, let's take a brief look at the history of SQL. SQL was first developed in the 1970s by IBM researchers Donald Chamberlin and Raymond Boyce. It was initially called SEQUEL (Structured English Query Language) and was designed to be an English-like language for querying relational databases."),
                            html.Br(),
                            html.P("Over the years, SQL has evolved and expanded to become the de facto standard for managing relational databases. Today, SQL is used by millions of developers and database administrators around the world, and it continues to be an essential tool for managing and analyzing data."),
                            html.Br(),
                            html.P("In the next section, we'll dive into the basics of SQL syntax and learn how to write simple queries. So, let's get started!"),

    ]),], style = {'backgroundColor':'white', 'color':colors['text'], 'border-radius':'10px'},)]
)



syntax_tab  = html.Div([
    dbc.Card(
    [
        #dbc.CardHeader("SQL Operations and Syntax"),
        dbc.CardBody(
            [
                html.H5("SELECT: Used to retrieve data from a table", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                SELECT column1, column2, ... FROM table_name WHERE condition;
                ```
                '''),
                html.H5("INSERT: Used to add new records to a table", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
                ```
                '''),
                html.H5("UPDATE: Used to modify existing records in a table", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
                ```
                '''),
                html.H5("DELETE: Used to delete records from a table", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                DELETE FROM table_name WHERE condition;
                ```
                '''),
                html.H5("Foreign Keys", className="card-title", style={'color':'#333333'}),
                html.H6("Foreign keys are an important concept in relational databases, as they help to maintain the integrity of the data by enforcing referential integrity rules between tables. A foreign key is a column or a set of columns in one table that refers to the primary key of another table. ", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                ALTER TABLE table_name ADD CONSTRAINT constraint_name FOREIGN KEY (column_name) REFERENCES reference_table (reference_column);
                ```
                '''),
                html.P("Example:"),
                dcc.Markdown('''
                ```
                ALTER TABLE orders ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers (customer_id);
                ```
                '''),
                html.H5("Index", className="card-title", style={'color':'#333333'}),
                html.H6("An index is a data structure that helps to speed up queries on a table. It creates a copy of a subset of data from a table in a more efficient data structure for faster access.", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                CREATE INDEX index_name ON table_name (column_name);
                ```
                '''),
                html.P("Example:"),
                dcc.Markdown('''
                ```
                CREATE INDEX idx_customers_country ON customers (country);
                ```
                '''),
                html.H5("Unique Index", className="card-title", style={'color':'#333333'}),
                html.H6('''A unique index is an index on one or more columns in a table that enforces a unique constraint on the data in those columns. This means that the values in the indexed columns must be unique across all rows in the table. Unique indexes are often used to enforce business rules or to prevent duplicate data from being inserted into the database.
                For example, if you have a users table and you want to ensure that each user has a unique email address, you can create a unique index on the email column. This will prevent any two users from having the same email address.''', className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                CREATE UNIQUE INDEX index_name ON table_name (column1, column2, ...);
                ```
                '''),
                html.P("Example:"),
                dcc.Markdown('''
                ```
                CREATE UNIQUE INDEX idx_unq_orders_customer ON orders (customer_id, order_date);
                ```
                '''),

                html.H5("Replace Values in a Column and Change Format to Numeric", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                UPDATE my_table SET my_column = REPLACE(my_column, 'old_char', 'new_char');
                ALTER TABLE my_table MODIFY COLUMN my_column DECIMAL(10,2);
                ```
                '''),
                html.H5("Format a Date Column as a Date String in 'YYYY-MM-DD' Format", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                SELECT DATE_FORMAT(created_at, '%Y-%m-%d') as formatted_date FROM orders;

                ```
                '''),
                html.H5("Round a Numeric Column to 2 Decimal Places", className="card-title", style={'color':'#333333'}),
                dcc.Markdown('''
                ```
                SELECT ROUND(price, 2) as formatted_price FROM products;
                ```
                '''),
            ], style={'backgroundColor':'white',
                      'border-radius': '10px'}
        )
    ],
    #color="light",
    inverse=False,
    outline=False,

)], style={})


database_structure_content = html.Div([
    dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4('Database Structure', style={'color': colors['text'], 'font-family': fonts['heading']}),
                html.P('A properly designed database structure is essential for efficient data management and retrieval. '
                       'A good database schema should be optimized for data storage, retrieval and modification, and should '
                       'be flexible and scalable.'),
                html.P('Normalization is an important technique used in database design to ensure data consistency, reduce '
                       'data redundancy, and improve data integrity. The goal of normalization is to eliminate '
                       'data anomalies that arise when data is duplicated or updated in one table but not in others. There are several levels of normalization, but the most common are first normal form (1NF), second normal form (2NF), and third normal form (3NF)'),
                html.P('In addition to normalization, indexing is another important technique for optimizing database '
                       'performance. Indexes can improve query performance by allowing the database to locate data '
                       'faster.'),
                html.P('When designing a database schema, it is important to consider the relationships between '
                       'different tables. The use of foreign keys can help enforce these relationships and ensure '
                       'data consistency.'),
                html.P('Overall, a well-designed database structure can improve data consistency, reduce data '
                       'redundancy, and improve query performance. By following best practices in database design, '
                       'you can create a schema that is optimized for your specific data management needs.'),
            ], style={'backgroundColor':'white', 'color':colors['text'], 'border-radius':'10px'}
        ),
    ]

)
], style={})

kimball_card = html.Div([dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Kimball Methodology", className="card-title", style={'color': colors['text']}),
                html.P(
                    "The Kimball Methodology is a popular approach to designing and managing large databases. "
                    "It emphasizes the importance of building a data warehouse that can support the needs of the business, "
                    "and provides a framework for organizing data in a way that is both efficient and effective. "
                    "The methodology is based on a set of best practices that have been developed over many years, "
                    "and is widely used by organizations around the world.",
                    className="card-text",
                    style={}
                ),
                html.P(
                    "The Kimball Methodology is based on several key principles, including the following:",
                    className="card-text",
                    style={}
                ),
                html.Ul(
                    [
                        html.Li("Business Requirements: The methodology emphasizes the importance of understanding the "
                                "business requirements for the data warehouse, and designing the schema to support those "
                                "requirements."),
                        html.Li("Dimensional Modeling: The methodology is based on dimensional modeling, which involves "
                                "organizing data into dimensions and facts. This approach makes it easier to analyze "
                                "large datasets, and provides a framework for building complex queries."),
                        html.Li("Data Integration: The methodology emphasizes the importance of integrating data from "
                                "different sources, and provides tools and techniques for doing so."),
                        html.Li("Data Quality: The methodology emphasizes the importance of data quality, and provides "
                                "a framework for managing data quality throughout the lifecycle of the data warehouse."),
                        html.Li("Iterative Development: The methodology is based on an iterative development process, "
                                "which involves building and testing the data warehouse in small increments."),
                    ],
                    style={}
                ),
                html.P(
                    "Overall, the Kimball Methodology is a powerful tool for designing and managing large databases. "
                    "By following the best practices outlined in the methodology, organizations can build data "
                    "warehouses that are both efficient and effective, and that can support the needs of the business "
                    "for years to come.",
                    className="card-text",
                    style={}
                ),
            ], style={'backgroundColor':'white', 'color':colors['text'], 'border-radius':'10px'},
        ),
      ],
    )
  ]
)












@callback(
Output("tab-content", "children"),
[Input("tabs", "active_tab")],
)
def render_tab_content(active_tab):
    if active_tab == "intro":
        return intro_tab
    elif active_tab == "syntax":
        return syntax_tab
    elif active_tab == "structure":
        return database_structure_content
    elif active_tab == "kimball":
        return kimball_card

#Define the previous projects tab

previousprojects_tab = html.Div([
html.H2("Projects"),
dbc.Row([
    dbc.Col([
        dbc.Card(
            [
                html.Div([dbc.CardImg(
                    src="assets/search.png",
                    top=True,
                    style={'width':'60%', 'height':'60%'}
                    )],style={ 'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center'}),
                #'height': '100%'}),
                dbc.CardBody(
                    [
                        html.H4(
                            "Quick Searches",
                            className="card-title",
                            style={'background':'white',
                   'color':'black'}
                            ),
                        html.P(
                            "By assigning macros to shortcut keys, users can efficiently access and retrieve data from a variety of web pages. This powerful functionality can significantly reduce the time and effort required for data lookup, freeing up valuable resources for other high-priority tasks. Whether used for research, analysis, or other purposes, the ability to swiftly navigate and retrieve information from the web can be a game-changer for businesses seeking to maximize their productivity and competitiveness. By leveraging automation and advanced technology in this way, organizations can unlock new opportunities for growth and innovation, empowering their workforce to achieve more and reach their full potential.",
                            className="card-text",
                            style={'background':'white',
                   'color':'black'}
                            ),
                        ]
                    ),
                ],
            style={#"width": "14rem",
                   'background':'white',
                   'color':'black'},
            ),
        ], width=4, align="center"),
    dbc.Col([
        dbc.Card(
            [
                html.Div([dbc.CardImg(
                    src="assets/text.png",
                    top=True,
                    style={'width':'60%', 'height':'60%', 'text-align':'center'}
                    )],style={ 'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center'}),
                #'height': '100%'}),
                dbc.CardBody(
                    [
                        html.H4(
                            "Text Generators",
                            className="card-title",
                            style={'background':'white',
                                   'color':'black'}
                            ),
                        html.P(
                            "Leveraging input data from Excel sheets, macros can automatically generate summaries and other textual outputs that are often required to be produced. This capability can streamline and enhance the efficiency of various workflows, enabling professionals to focus on high-value tasks while still ensuring accurate and high-quality deliverables. By harnessing the power of automation, organizations can increase productivity, optimize resource utilization, and unlock new opportunities for growth and innovation.",
                            className="card-text",
                            style={'background':'white',
                                   'color':'black'}
                            ),
                        ]
                    ),
                ],
            style={#"width": "14rem",
                   'background':'white',
                   'color':'black'},
            ),
        ], width=4, align="top"),
    dbc.Col([
        dbc.Card([
                dbc.CardImg(
                    src="assets/data.png",
                    top=True,
                    #style={'height': '100%'}
                    ),
                dbc.CardBody(
                    [
                        html.H4(
                            "Data UserForms",
                            className="card-title",
                            style={'background':'white',
                   'color':'black'}
                            ),
                        html.P(
                            "By utilizing data from other Excel sheets, UserForms can provide employees with a user-friendly interface for swiftly retrieving relevant information. Additionally, shortcut keys can be assigned to refresh the UserForms, thereby optimizing and accelerating the data retrieval process. These functionalities can significantly boost productivity and efficiency, enabling organizations to make the most of their resources and achieve their goals with greater ease and effectiveness.",
                            className="card-text",
                            style={'background':'white',
                   'color':'black'}
                            ),
                        ]
                    ),
                ],#"width": "14rem",
            style={'background':'white',
                   'color':'black'})], width=4, align="top"
        ),
    ],
    style={},
    #className="mb-4",
    ),
    ], style ={'text-align':'center'},

    )

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
            html.Div(id="tab-content"),
            ], style={'width':'70%',
                       #'backgroundColor': '#7eddab',
                      },
            #className="mt-4",
        ),
    ],
    fluid=True,
    className='parent-container',
    style={
    'textAlign':'center',
    #'backgroundColor': '#7eddab',
    #'color': '#333333',
    #'font-family': ['Helvetica', 'sans-serif'],
    #'font-style': ['bold'],
    #'fontSize': 18,
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'min-height': '100vh'
}
)
