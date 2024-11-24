#!/usr/bin/env python
# coding: utf-8

# # The Rise of EVs and their Impact on the Environment
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# The rapid increase in electric vehicles (EV) available on the road has offered a very promising solution to global warming efforts around the world. However, understanding the impact of EVs on the environment starts with the full lifecycle starting from the manufacturing to usage on the road and inevitably disposal. This topic is important because it seems that people ar shifting over to EVs for everyday commuting due to the financial benefits and reliefs that may come in the form of gas and maintenance. This paired with the rising concern in the environment and global warming brings it fairly high on the relevance charts.

# ## Project Question
# #### **1. What is the current state of EV adoption around the world, and which geographic regions are experiencing the most significant growth?**
# 
# #### **2. How do greenhouse gas emissions through the lifespan of an EV compare to the traditional gas-powered combustion engine?**
# 
# #### **3. How does the availability of EV charging stations influence the amount of EVs on the road there?**

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# > - Including visuals, such as a bar graph or a heat map, can show sales and growth trends in different regions.
# 
# > - Use a bar chart or pie chart to compare the different stages of the lifespan of the vehicles.
# 
# > - A heat map to show EV stations as well as number of EVs on the road would work great here.
# 
# EVs, being more popular in suburban and major city areas, will have a positive impact on the environment.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# #### Source: **International Energy Agency (IEA)**
# > **Data type:** Downloadable data reports (file)
# 
# > **Description:** Shows annual reports on EVs in general, such as adoption, stock, charging, and emissions impact on the environment.
# 
# > **Relation:** This can be paired with the other sources as they have similar data points. I can merge common/supporting columns after I analyze and clean the data.
# 
# **Link:** https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer
# 
# #### **Source: Our World in Data**
# > **Data type:** Downloadable data reports and API (file and API)
# 
# > **Description:** Shows global EV adoption, environmental impacts, and charging infrastruction
# 
# > **Relation:** Pairing this with the IEA data source will allow me to combine similar points and compare globally.
# 
# **Link:** https://ourworldindata.org/electric-car-sales
# 
# #### **Source: Open Charge Map**
# > **Data type:** API access (API)
# 
# > **Description:** API containing location data for EV charge infrastructure.
# 
# > **Relation:** This can be paired with the other two sources quite well, as this would give a good visual representation. This goes for each of the previous sources as well, but the data sources will be paired with research involving information that can not be easily shown as data to make conclusions.
# 
# **Link:** https://openchargemap.org/site/develop/api#/

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# In[47]:


# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
import requests
import json


# Load data into dataframes
bev_share_df = pd.read_csv('data/bev-share-new-ev.csv')
sales_df = pd.read_csv('data/car-sales.csv')
ev_sales_share_df = pd.read_csv('data/electric-car-sales-share.csv')
ev_sales_df = pd.read_csv('data/electric-car-sales.csv')
ev_stocks_df = pd.read_csv('data/electric-car-stocks.csv')
iea_data_df = pd.read_csv('data/IEA-EV-dataEV salesHistoricalCars.csv')
bev_share_car_sales_df = pd.read_csv('data/share-car-sales-battery-plugin.csv')
ev_share_car_stocks_df = pd.read_csv('data/share-car-stocks-electric.csv')

display(bev_share_df.head())
display(sales_df.head())
display(ev_sales_share_df.head())
display(ev_sales_df.head())
display(ev_stocks_df.head())
display(iea_data_df.head())
display(bev_share_car_sales_df.head())
display(ev_share_car_stocks_df.head())


# # Merging

# In[7]:


# Summary of data
display(bev_share_df.info())
display(sales_df.info())
display(ev_sales_share_df.info())
display(ev_sales_df.info())
display(ev_stocks_df.info())
display(iea_data_df.info())
display(bev_share_car_sales_df.info())
display(ev_share_car_stocks_df.info())


# In[8]:


# Combine dataframes
combined_df = pd.merge(bev_share_df, sales_df, on=['Entity', 'Code', 'Year'], how='outer')

combined_df = pd.merge(combined_df, ev_sales_share_df, on=['Entity', 'Code', 'Year'], how='outer')
combined_df = pd.merge(combined_df, ev_sales_df, on=['Entity', 'Code', 'Year'], how='outer')
combined_df = pd.merge(combined_df, ev_stocks_df, on=['Entity', 'Code', 'Year'], how='outer')
combined_df = pd.merge(combined_df, iea_data_df, left_on=['Entity', 'Year'], right_on=['region', 'year'], how='outer')
combined_df = pd.merge(combined_df, bev_share_car_sales_df, on=['Entity', 'Code', 'Year'], how='outer')
combined_df = pd.merge(combined_df, ev_share_car_stocks_df, on=['Entity', 'Code', 'Year'], how='outer')

combined_df.info()
combined_df.head()


# # Cleaning

# #### The first step taken for cleaning was to combine all the dataframes on common values, and remove duplicate columns. The next step I took was to rename all of the columns to more consistent and readable values.

# In[31]:


# combined_df.drop(columns=['region', 'year', 'Electric cars sold_y'], inplace=True)  UNCOMMENT IF RUNNING FROM SCRATCH

combined_df.rename(columns={
    'Entity': 'Region',
    'Code': 'Region Code',
    'Battery-electric as a share of electric cars sold': 'BEV Shares',
    'Electric cars sold_x': 'EVs Sold',
    'Non-electric car sales': 'Non-EV Sales',
    'Share of new cars that are electric': 'New Car EV Shares',
    'Electric car stocks': 'EV Stocks',
    'category': 'Category',
    'parameter': 'Parameter',
    'mode': 'Mode',
    'powertrain': 'Powertrain',
    'unit': 'Unit',
    'value': 'Value',
    'Plug-in hybrid as a share of cars sold': 'All Car EV Shares',
    'Battery-electric as a share of cars sold': 'All Car BEV Shares',
    'Share of car stocks that are electric': 'EV Stock Shares',
}, inplace=True)

combined_df.sample(10)


# #### The final step for cleaning was to identify the columns with null values and fill/drop them. I filled columns with continuous/numerical/categorical values following different methods based on the data. I dropepd the columns with missing Regions as that is not something that can really be filled based on the nature of this dataset - separated by region and year. I also dropped the row with global totals as that was causing some skews and abnormalities in my visuals.

# In[41]:


# Fill missing values
combined_df['BEV Shares'].fillna(combined_df['BEV Shares'].mean(), inplace=True)
combined_df['EVs Sold'].fillna(combined_df['EVs Sold'].mean(), inplace=True)
combined_df['Non-EV Sales'].fillna(combined_df['Non-EV Sales'].mean(), inplace=True)
combined_df['New Car EV Shares'].fillna(combined_df['Non-EV Sales'].mean(), inplace=True)
combined_df['EV Stocks'].fillna(combined_df['EV Stocks'].mean(), inplace=True)
combined_df['Value'].fillna(combined_df['Value'].mean(), inplace=True)
combined_df['All Car EV Shares'].fillna(combined_df['All Car EV Shares'].mean(), inplace=True)
combined_df['All Car BEV Shares'].fillna(combined_df['All Car BEV Shares'].mean(), inplace=True)
combined_df['EV Stock Shares'].fillna(combined_df['EV Stock Shares'].mean(), inplace=True)

combined_df['Category'].fillna(combined_df['Category'].mode()[0], inplace=True)
combined_df['Parameter'].fillna(combined_df['Parameter'].mode()[0], inplace=True)
combined_df['Mode'].fillna(combined_df['Mode'].mode()[0], inplace=True)
combined_df['Powertrain'].fillna(combined_df['Powertrain'].mode()[0], inplace=True)
combined_df['Unit'].fillna(combined_df['Unit'].mode()[0], inplace=True)

# Drop rows
combined_df.dropna(subset=['Region', 'Region Code'], inplace=True)
combined_df = combined_df[combined_df['Region'] != 'World']

missing_values = combined_df.isnull().sum()
missing_values

combined_df.sample(10, random_state=2)


# # Visualizations

# In[135]:


# Total Sales by Region Data
total_sales_region = combined_df.groupby('Region')['EVs Sold'].sum().reset_index()
average_bev_shares = combined_df.groupby('Region')['BEV Shares'].mean().reset_index()
scatter_data = combined_df.groupby(['Year', 'Region'])['EVs Sold'].sum().reset_index()

# Create subplots: 2 rows and 2 columns
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "bar"}, {"type": "choropleth"}],
           [{"type": "scatter"}, {"type": "pie"}]],
    subplot_titles=("Average BEV Shares by Region", 
                    "Total EV Sales by Region", 
                    "EVs Sold vs Non-EV Sales by Region", 
                    "Share of EV Stocks by Region")
)

# Bar Chart
bar_trace = go.Bar(
    x=average_bev_shares['Region'], 
    y=average_bev_shares['BEV Shares'],  
    hoverinfo='x+y',
    marker=dict(color='blue'),
)

fig.add_trace(bar_trace, row=1, col=1)

# Choropleth Map
map_trace = go.Choropleth(
    locations=total_sales_region['Region'],
    locationmode='country names',
    z=total_sales_region['EVs Sold'],
    colorbar=dict(
        title='Total EVs Sold',
        thickness=15,
        len=0.8,
        x=1.05,
        y=0.5,
        xanchor='left',
        yanchor='middle'
    ),
    hoverinfo='location+z',
    colorscale='Viridis',
)

fig.add_trace(map_trace, row=1, col=2)

# Scatter Chart for EV Sales vs Non-EV Sales
scatter_trace = go.Scatter(
    x=combined_df['EVs Sold'], 
    y=combined_df['Non-EV Sales'], 
    mode='markers',
    marker=dict(
        color='red',
        size=7),
    text=combined_df.apply(lambda row: f"Region: {row['Region']}<br>EVs Sold: {row['EVs Sold']}<br>Non-EV Sales: {row['Non-EV Sales']}", axis=1),
    hoverinfo='text'
)

fig.add_trace(scatter_trace, row=2, col=1)

# Pie Chart for Share of EV Stocks
pie_trace = go.Pie(
    labels=combined_df['Region'], 
    values=combined_df['EV Stocks'],
    hole=0.4,
    textinfo='none',
    hoverinfo='label+value+percent',
    showlegend=False,
)

fig.add_trace(pie_trace, row=2, col=2)

# Annotations
fig.add_annotation(
    text="This bar chart illustrates the average BEV shares by region.<br>As seen, the more developed countries have a higher value for this.",
    x=0, y=0.5,
    showarrow=False,
    font=dict(size=12),
    xref="paper", yref="paper",
    align="center",
)

fig.add_annotation(
    text="This map shows total EV sales by region. Lighter colors indicate higher sales.",
    x=1.02, y=1.075,
    showarrow=False,
    font=dict(size=12),
    xref="paper", yref="paper",
    align="center",
)

fig.add_annotation(
    text="This scatter plot depicts the relationship between EV sales and non-EV<br>sales across regions. Many countries are seen in the bottom<br>corner aside from China and the USA.",
    x=0, y=-0.12,
    showarrow=False,
    font=dict(size=12),
    xref="paper", yref="paper",
    align="center",
)

fig.add_annotation(
    text="This pie chart shows the share of EV stocks by region. As seen<br>here, China has a large majority in terms of Share of EV Stocks.",
    x=1, y=-0.1,
    showarrow=False,
    font=dict(size=12),
    xref="paper", yref="paper",
    align="center",
)


# Update layout
fig.update_layout(
    height=800, 
    width=1200,
    title_text="Electric Vehicle Sales Visualizations", 
    title_font_size=24,
    font=dict(size=12),
    showlegend=False,
    legend=dict(
        x=0.9, 
        y=0.5, 
        traceorder='normal', 
        orientation='v',
        title=dict(text='Regions')
    )
)

# Show the complete figure
fig.show()


# # Checkpoint 3 - Machine Learning
# 
# ### Machine Learning Plan
# 
# #### Type of Machine Learning Model
# I plan to use supervised learning models for this project, specifically:
# - regression models if the intended outcome is to predict something like sales or prices
# - classification models if the intended outcome is to predict something like failure or success or assigning categories, such as BEV or PHEV
# 
# Possible candidates include:
# - linear regression, decision trees, or random forest
# - logistic regression, fandom forest, or gradient boosting machines
# 
# #### Anticipated Challenges
# - Insufficient data, solved by adding more data
# - Imbalanced data, solved by gathering varied data
# - Data quality issues, perform EDA to prevent this
# - Feature engineering, use something like scikit-learn to select features
# 
# 
# ### Machine Learning Implementation Process
# 
# #### Ask
# What specific predictions is this machine learning model intended to address?
# What features of the datasets are most relevant, and how will they be used to train the model?
# 
# #### Prepare
# Conduct EDA to explore relationships, detect outliers, and also identify the key variables in the dataset.
# Visualize feature distributions, correlations, and the trends.
# 
# #### Process
# Split the dataset into train, validation, and test sets.
# Clean the data. Depending on the situation, imputation or removing a row altogether may be needed.
# Scale and normalize the data using scikit-learn libraries, such as StandardScaler or MinMaxScaler.
# Use encoding.
# 
# #### Analyze
# Test multiple algorithms/models and compare results.
# Cross-validate to evaluate the models' performance.
# 
# #### Evaluate
# Compare the models based on metrics depending on the model:
# - regression - MSE, R^2
# - classification - accuracy, precision, f1 score
# 
# #### Share
# Summarize findings in a dashboard, possibly made with PowerBI, otherwise using Matplotlib or Streamlit.
# Communicate the key metrics and findings clearly.

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[136]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


# In[ ]:




