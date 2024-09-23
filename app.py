import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('California housing data(1990) ')
df = pd.read_csv('housing/housing.csv')

price_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)

# Create a multiselect
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),  # options
    df.ocean_proximity.unique())  # defaults

# Create a radio button
income_level = st.sidebar.radio(
    'Choose income level:', 
    ['Low', 'Medium', 'High']
)

if income_level == 'Low':
    df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    df = df[df['median_income'] >= 4.5]

df = df[df.median_house_value >= price_filter]


df = df[df.ocean_proximity.isin(location_filter)]

st.map(df)

st.subheader('Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
ax.hist(df['median_house_value'], bins=30)
ax.set_title('Histogram of Median House Value', fontsize=16)
ax.set_xlabel('Median House Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
st.pyplot(fig)
