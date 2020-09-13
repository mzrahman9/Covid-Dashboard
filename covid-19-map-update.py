#!/usr/bin/env python
# coding: utf-8

# In[44]:


import os
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs,plot
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np
import pandas as pd


# In[45]:


df = pd.read_excel('https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx')


# In[46]:


df.head()


# In[47]:


df1 = pd.pivot_table(df,index=['countriesAndTerritories','countryterritoryCode'],aggfunc={'cases':np.sum})
df1.reset_index(inplace=True)
df1.head()


# In[48]:


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# In[49]:


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# In[50]:


fig = go.Figure(data=go.Choropleth(
    locations = df1['countryterritoryCode'],
    z = df1['cases'],
    text = df1['countriesAndTerritories'],
    colorscale = 'Reds',
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'Total Cases',
))


# In[51]:


fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide">\
            European Centre for Disease Prevention and Control</a>',
        showarrow = False
    )]
)


# In[52]:


app.layout = html.Div(children=[
    html.H1(children='COVID-19 Worldmap',
            style= {'textAlign': 'center'}
           ),

    html.Div(children='''
        The Map below represents spread of COVID-19 cases worldiwde.Data is collected from European Centre for Disease Prevention and Control (ECDC) which is updated daily
    '''),

    dcc.Graph(
        id='the graph',
        style= {'height':'90vh', 'width':'100vw'},
        figure=fig
    )
])


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




