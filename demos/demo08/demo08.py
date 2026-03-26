import pandas as pd
import requests # for making RESTful API requests
import json # for converting strings in JSON format to python dictionaries and lists
import yaml # for converting yaml-structured text into python dictionaries and lists
import os # for basic operating system functions, like compiling paths

def construct_rentcast_json_filename(zipcode):
    return f'rentcast_{zipcode}.json'

def get_rentcast_data_for_zipcode(zipcode):
    # Make GET request to rentcast API
    url = f'https://api.rentcast.io/v1/markets?zipCode={zipcode}&dataType=All&historyRange=6'
    headers = {
        'X-Api-Key': CONFIGS['rentcast_api_key'],
        'Accept': 'application/json', 
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    # Save to json
    file_path = construct_rentcast_json_filename(zipcode)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Get rentcast market data for the 5 zipcodes most represented in the eviction case data
zipcodes = df['Tenant ZIP Code'].value_counts().head(1).index.astype('Int64')

for zipcode in zipcodes:
    get_rentcast_data_for_zipcode(zipcode)