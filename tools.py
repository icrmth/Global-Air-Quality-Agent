import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('global_air_pollution_dataset.csv')
df_clean = df.dropna(subset=['Country', 'City'])

def get_city_profile(city_name: str) -> dict:
  """
    Fetches the current Air Quality Index (AQI) and pollutant profile for a specific city.
    Use this tool when a user asks for the air quality of a single city.
    
    Args:
        city_name (str): The name of the city to look up.
    """
  #clean user input
  search_city = city_name.strip().lower()
  #find the matching city data in df_clean
  city_data = df_clean[df_clean.City.str.lower() == search_city]
  #if city is not found, return error
  if city_data.empty:
    return {"error" : f"Could not find data for '{city_name}'. Please check the spelling."}
  #return city_data, iloc[0] grabs the first matching row, to_dict() turns it into JSON-like format
  return city_data.iloc[0].to_dict()

def plot_city_graph(city_name):
  #clean user input
  search_city = city_name.strip().lower()
  city_data = df_clean[df_clean.City.str.lower() == search_city]
  if city_data.empty:
    return None
  
  pollutants = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
  value = city_data.iloc[0][pollutants].values

  fig, ax = plt.subplots(figsize=(8,6))
  colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] 
  ax.bar(pollutants, value, color=colors)
    
  ax.set_title(f"Air Quality Profile for {city_name.title()}")
  ax.set_ylabel('AQI Value')
  ax.set_xlabel('Pollutant')

  return fig

def compare_cities(city1: str, city2: str) -> dict:
  """
    Compares the Air Quality Index (AQI) and pollutant profiles of two different cities.
    Use this tool when a user asks to compare or find the difference in air quality between two specific cities.
    
    Args:
        city1 (str): The name of the first city.
        city2 (str): The name of the second city.
    """
  search_city1 = city1.strip().lower()
  city1_data = df_clean[df_clean.City.str.lower() == search_city1]
  if city1_data.empty:
    return {"error" : f"Could not find data for '{city1}'. Please check the spelling."}

  search_city2 = city2.strip().lower()
  city2_data = df_clean[df_clean.City.str.lower() == search_city2]
  if city2_data.empty:
    return {"error" : f"Could not find data for '{city2}'. Please check the spelling."}
  
  return city1_data.iloc[0].to_dict(), city2_data.iloc[0].to_dict()

def plot_compare_cities(city1, city2):
  search_city1 = city1.strip().lower()
  city1_data = df_clean[df_clean.City.str.lower() == search_city1]
  if city1_data.empty:
    return {"error" : f"Could not find data for '{city1}'. Please check the spelling."}

  search_city2 = city2.strip().lower()
  city2_data = df_clean[df_clean.City.str.lower() == search_city2]
  if city2_data.empty:
    return {"error" : f"Could not find data for '{city2}'. Please check the spelling."}
  
  pollutants = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
  value1 = city1_data.iloc[0][pollutants].values
  value2 = city2_data.iloc[0][pollutants].values
  fig, ax = plt.subplots(figsize=(8,6))

  # Create an array of numbers for the X locations (0, 1, 2, 3)
  x = np.arange(len(pollutants)) 
  width = 0.35

  ax.bar(x - width/2, value1, width, label = city1.title(), color='#1f77b4')
  ax.bar(x + width/2, value2, width, label = city2.title(), color='#ff7f0e')
  
  ax.set_xticks(x)
  ax.set_xticklabels(pollutants)

  ax.set_title(f"Comparing Air Quality of {city1.title()} and {city2.title()}")
  ax.set_ylabel('AQI Value')
  ax.set_xlabel('Pollutant')
  ax.legend()
  plt.tight_layout()
  
  return fig

def get_worst_cities(country_name: str, top_n:int =5):
  """
    Finds the most polluted cities in a specific country based on their overall AQI value.
    Use this tool when a user asks for the worst, most polluted, or highest AQI cities in a given country.
    
    Args:
        country_name (str): The name of the country to search within.
        top_n (int, optional): The number of top worst cities to return. Defaults to 5.
    """
  search_country = country_name.strip().lower()
  search_cities = df_clean[df_clean.Country.str.lower() == search_country]
  if search_cities.empty:
    return {"error" : f"Could not find data for '{country_name}'. Please check the spelling."}

  # Sort the data to find the WORST cities
  # We sort by 'AQI Value'. ascending=False puts the biggest numbers at the top
  sort_cities = search_cities.sort_values(by= 'AQI Value', ascending=False)

  # Get top n cities
  top_cities = sort_cities.head(top_n)

  return {"worst_citites": top_cities.to_dict(orient='records')}

def get_best_cities(country_name: str, top_n: int=5):
  """
    Finds the least polluted cities in a specific country based on their overall AQI value.
    Use this tool when a user asks for the best, least polluted, or lowest AQI cities in a given country.
    
    Args:
        country_name (str): The name of the country to search within.
        top_n (int, optional): The number of top best cities to return. Defaults to 5.
    """
  search_country = country_name.strip().lower()
  search_cities = df_clean[df_clean.Country.str.lower() == search_country]
  if search_cities.empty:
    return {"error" : f"Could not find data for '{country_name}'. Please check the spelling."}
  # Logically the same as above, ascending=True to put the lower values to the top
  sort_cities = search_cities.sort_values(by= 'AQI Value', ascending=True)
  top_cities = sort_cities.head(top_n)

  return {"worst_citites": top_cities.to_dict(orient='records')}

def plot_worst_cities(country_name, top_n=5):
  search_country = country_name.strip().lower()
  search_cities = df_clean[df_clean.Country.str.lower() == search_country]
  if search_cities.empty:
    return {"error" : f"Could not find data for '{country_name}'. Please check the spelling."}
  sort_cities = search_cities.sort_values(by= 'AQI Value', ascending=False)
  top_cities = sort_cities.head(top_n)

  fig, ax = plt.subplots(figsize=(10,6))
  ax.barh(top_cities['City'], top_cities['AQI Value'], color='#1f77b4')
  ax.invert_yaxis()

  ax.set_title(f"Top {top_n} Worst Air Quality Cities in {country_name.title()}")
  ax.set_ylabel('City Names')
  ax.set_xlabel('AQI Value')
  plt.tight_layout()
  
  return fig

def plot_best_cities(country_name, top_n=5):
  search_country = country_name.strip().lower()
  search_cities = df_clean[df_clean.Country.str.lower() == search_country]
  if search_cities.empty:
    return {"error" : f"Could not find data for '{country_name}'. Please check the spelling."}
  sort_cities = search_cities.sort_values(by= 'AQI Value', ascending=True)
  top_cities = sort_cities.head(top_n)

  fig, ax = plt.subplots(figsize=(10,6))
  ax.barh(top_cities['City'], top_cities['AQI Value'], color='#1f77b4')
  ax.invert_yaxis()

  ax.set_title(f"Top {top_n} Worst Air Quality Cities in {country_name.title()}")
  ax.set_ylabel('City Names')
  ax.set_xlabel('AQI Value')
  plt.tight_layout()
  
  return fig