import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price):', 0.0, 50000, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximityl.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
income_level = st.radio(
    "Select Income Level:",
    ['Low ', 'Medium', 'High']
)

# Filter the DataFrame based on selections
if income_level == 'Low(<2.5)':
    filtered_df = df[df['median_income'<= 2.5]]
elif income_level =='Medium(>2.5 & <4.5)':
    filtered_df  = df[(df['median_income'] > 2.5) & (df['median_income']< 4.5)]
else:
    filtered_df = df[df[df['median_income'> 4.5]]]

df = df[df.median_house_value >= price_filter]

df = df[df.ocean_proximity.isin(location_filter)]

if income_level == '(Low<2.5)':
    filtered_df = df[df['median_income'] <=2.5]
elif income_level == 'Medium(>2.5 & <4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else: 
    filtered_df = df[df['median_income'>4.5]]

st.map(df)