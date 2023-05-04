

#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import dash_bootstrap_components as dbc
import dash
from dash import html, dcc

dash.register_page(__name__, path='/economy')


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

economy = pd.read_csv('econW.csv')
economy['InflationExp'] = economy['InflationExp'] / 100
economy['unemp_rate'] = economy['unemp_rate'] / 100
economy['TenYield'] = economy['TenYield'] / 100



def create_graph(color, yaxis, title, dataframe, y, tick, starts, ends, hline1=False, textbox=False, pred=False,
                 legend=False, YoY=False, Score=False):
    dataframe = dataframe.ffill().fillna(0)
    mask = (dataframe['Date'] > starts) & (dataframe['Date'] <= ends)
    dataframe = dataframe.loc[mask]
    fig = px.line(dataframe, x='Date', y=y, color_discrete_sequence=[color])
    fig.update_layout(
        yaxis_title=yaxis,
        xaxis_title='Date',
        title=title,
        title_x=0.5,
        margin={
            'l': 0,
            'r': 0
        },
        font=dict(family="Abel", size=15, color=colors['text']))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(tickformat=".1" + str(tick))
    init = 1
    fig.layout.plot_bgcolor = 'white'
    # fig.update_traces(line_color=color, line_width=1)
    if pred == True:
        fig.update_traces(line_color='orange', line_width=2)
        fig.add_traces(
            list(px.line(dataframe, x='Date', y='Forward Return', color_discrete_sequence=["skyblue"]).select_traces()))
        fig.add_traces(
            list(px.line(dataframe, x='Date', y='SP Trailing 4 Weeks Return',
                         color_discrete_sequence=["red"]).select_traces()))
        # fig.update_traces(line_width=1)
    if hline1 == True:
        fig.add_hline(y=35, line_width=3, line_dash="dash", line_color="orange")
        fig.add_hline(y=20, line_width=3, line_dash="dash", line_color="red")

    if YoY == True:
        fig.add_hline(y=0.02, line_width=3, line_dash="dash", line_color="orange")
        fig.add_annotation(
            text='Yellow Line: FED Target Rate',
            align='left',
            showarrow=False,
            xref='paper',
            yref='paper',
            x=0.05,
            y=1.0,
            bordercolor='black',
            borderwidth=1)
    else:
        next
    if textbox == True:
        fig.add_annotation(
            text='Yellow Line Recommendation: 70 % Long <br> 30% Short <br> Red Line Recommendation: Risk Neutral <br> i.e 50 % Long, 50 % Short',
            align='left',
            showarrow=False,
            xref='paper',
            yref='paper',
            x=0.05,
            y=1.0,
            bordercolor='black',
            borderwidth=1)
    if Score == True:
        fig.update_layout(
        #height=600

        )
    fig.update_layout(template='simple_white', margin=dict(l=50, r=50, t=50, b=50),
                      paper_bgcolor=colors['background'],
                      plot_bgcolor=colors['content'])
    # if legend == True:
    #    fig['data'][0]['showlegend']=True
    #    fig['data'][0]['name']=y
    if ((legend == True) & (y == 'Preds')):
        fig['data'][0]['showlegend'] = True
        fig['data'][0]['name'] = 'Predicted Forward Return'
        fig['data'][1]['showlegend'] = True
        fig['data'][1]['name'] = 'Actual Forward Return'

    return fig



descriptioneconomy = ''' An overview of the economy for a better understanding of current market conditions. The presented data is raw and has not been altered. Source of data is FRED API and multpl.com.'''
cardeconomy = dbc.Container([
                    html.Div(children=[html.H1("Economy", style={}, className='headerfinvest'),
                                        html.H1("Overview", style={'color':'rgba(61, 181, 105)'}, className='headerfinvest'),
                                          ], className='parent-row', style={'margin':'15px'}),
            html.Div(children=[descriptioneconomy, html.Hr()], className='normal-text', style={'max-width':'75%', 'textAlign':'center', 'font-size':'1,5rem'}),


        html.Div([
                dcc.Graph(
                    figure=create_graph(colors['accent'], 'Inflation YoY', 'Inflation US YoY-Change %', economy, 'YoY', tick='%',
                                        starts='2000-01-01', ends=str(datetime.today()), YoY=True),  className='graph',
                    style={'border-right': '1px rgba(1, 1, 1, 1)'})
                # width={'size':5, 'offset':1, 'order':1},

                # xs=6, sm=6, md=6, lg=5, xl=5

                ,
                html.Div([

                    dcc.Graph(
                        figure=create_graph(colors['accent'], 'Money Supply Groth YoY', 'Money Supply US YoY-Change %', economy,
                                            'm2_growth', tick='%', starts='2000-01-01', ends=str(datetime.today())),
                         className='graph')
                ],  # className='six columns' #width={'size':5, 'offset':0, 'order':2},

                ), # className='graph-right')
        ], className='parent-row', style={'overflow': 'visible'}),

        html.Div([
            dcc.Graph(
                figure=create_graph(colors['accent'], 'Yield', '10-yr Treasury Yield %', economy, 'TenYield', tick='%',
                                    starts='2000-01-01', ends=str(datetime.today())), style={},  className='graph')
                # width={'size':5, 'offset':1, 'order':1},

                # xs=6, sm=6, md=6, lg=5, xl=5

                ,
                html.Div([

                    dcc.Graph(figure=create_graph(colors['accent'], 'Shiller P/E Ratio', 'Shiller P/E Ratio', economy,
                                                  'Shiller_P/E',
                                                  tick=' ', starts='2000-01-01', ends=str(datetime.today())), className='graph'),
                ],  # className='six columns' #width={'size':5, 'offset':0, 'order':2},

                ), # className='graph-right')
        ], className='parent-row', style={}),

        html.Div([
            dcc.Graph(figure=create_graph(colors['accent'], 'Confidence', 'Composite Confidence Indicator US', economy,
                                          'ConsumerConfidence', tick=' ', starts='2000-01-01',
                                          ends=str(datetime.today())), className='graph'),
                # width={'size':5, 'offset':1, 'order':1},

                # xs=6, sm=6, md=6, lg=5, xl=5

                html.Div([

                    dcc.Graph(
                        figure=create_graph(colors['accent'], 'Unemployment Rate', 'Unemployment Rate US', economy,
                                            'unemp_rate', tick='%', starts='2000-01-01',
                                            ends=str(datetime.today())), className='graph'),
                ],  # className='six columns' #width={'size':5, 'offset':0, 'order':2},

                ), # className='graph-right')
        ], className='parent-row', style={}),


        html.Div([
                html.H3(
                    "Below we present a combined economy score which tries to give a score for the current state of the economy. The score is created by weighing fundamental factors in the economy, like the data visualized above. The data is made stationary in order to conduct meaningful analysis. The weights are then "
                    "optimized in a long-short strategy of the S&P500 SPY ETF where Sharpe Ratio is maximized. Note that this score does not take into account interactions between the factors. We use data from 1998 for this purpose because of changes in economic conditions.",
                    className='normal-text', style={'textAlign':'center'}),
                html.Hr(),], style={'margin':'5%'}),

        html.Div([

            dcc.Graph(
                figure=create_graph(colors['accent'], 'Score', 'Combined Economy Score', economy, 'Combined Economy Score',
                                    tick=' ', starts='2000-01-01', ends=str(datetime.today()), hline1=True,
                                    textbox=True, Score=True), style={})  # 'height':'43vw'})
        ], className='graph' , style={}

        ),
        html.Br()
        # html.Div([
        # dbc.Card([html.Div([
        #                    html.H3("Finally we present a prediction for the next month return of the S&P500 index. The predictions are made using an LSTM Neural Network with two LSTM hidden layers. LSTM stands for Long-Short Term Memory and it fits the model "
        #                            "based on recent developments, as well as historic data to make a prediction for the future. The model is based on fundamental factors in the economy as well as price data from the S&P500 index. The model also accounts for autocorrelation"
        #                            " by looking at the data as a sequence. Based on autocorrelation analysis, we find that the data seems to be autocorrelated by a window of 1 year. We therefore choose a window of the sequence in the model as 52 weeks. The model also takes interactions between the factors into account. Measures to adjust for overfitting"
        #                            " includes both dropout and recurrent dropout layers and early stopping when the model does not improve.", style={'fontSize':'0.7em', 'font-family': ["Helvetica"], 'font-weight':'lighter'}),
        #                            ],
        #                                    style={}, className='header-items',

        # xs=12, sm=12, md=12, lg=5, xl=5)
        #   ),
        #        ])],className='header-main'),
        # html.Div([

        #           dcc.Graph(figure=create_graph('blue', 'Predicted Forward Return', 'Predictions One Month Return S&P500 LSTM Neural Network ', econW2, 'Preds', tick='%',starts='2020-01-01', ends=str(datetime.today()), hline1=False, textbox=False, pred=True, legend=True),style={})
        #       ],className='table-users' #width={'size':5, 'offset':0, 'order':2},


    # ])
], className='parent-container2', fluid=True, style={'background-color':'white'})


layout = dbc.Container([cardeconomy],
    className='')