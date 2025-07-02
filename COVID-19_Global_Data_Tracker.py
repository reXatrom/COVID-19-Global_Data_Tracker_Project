# 📦 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style='darkgrid')


# 📂 Step 2: Load Data
df = pd.read_csv('owid-covid-data.csv')
df.head()


# Step 3: Data Exploration
df.info()
df.isnull().sum().sort_values(ascending=False)


# Step 4: Data Cleaning
df['date'] = pd.to_datetime(df['date'])
countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)].dropna(subset=['total_cases', 'total_deaths'])
df_countries.fillna(0, inplace=True)


# Step 5: Exploratory Data Analysis
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_countries[df_countries['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)
plt.title('Total Cases Over Time')
plt.legend()
plt.show()



# Step 6: Vaccination Progress
plt.figure(figsize=(12, 6))
for country in countries:
    data = df_countries[df_countries['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)
plt.title('Vaccination Progress Over Time')
plt.legend()
plt.show()


# Step 7: Choropleth Map
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date]
map_data = latest_df[['iso_code', 'location', 'total_cases']].dropna()
fig = px.choropleth(map_data, locations='iso_code', color='total_cases',
                    hover_name='location', color_continuous_scale='OrRd',
                    title=f'Total COVID-19 Cases by Country on {latest_date.date()}')
fig.show()
