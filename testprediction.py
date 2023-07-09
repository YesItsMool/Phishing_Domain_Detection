import pandas as pd
import numpy as np
import requests
import json

# Load the dataset
df = pd.read_csv('dataset_full.csv')

# Define the features to be used for prediction
features_to_use = ['asn_ip', 'time_domain_activation', 'length_url',
       'qty_dollar_directory', 'qty_dollar_file', 'qty_underline_file',
       'qty_equal_file', 'qty_and_file', 'qty_questionmark_directory',
       'qty_tilde_file', 'qty_asterisk_file', 'qty_equal_directory',
       'qty_plus_file', 'qty_comma_file', 'qty_exclamation_directory',
       'qty_slash_file', 'qty_space_file', 'qty_and_directory',
       'qty_at_directory', 'qty_hashtag_directory', 'qty_asterisk_directory',
       'qty_questionmark_file', 'qty_hashtag_file', 'qty_exclamation_file',
       'qty_at_file', 'qty_comma_directory', 'qty_percent_file',
       'qty_hyphen_file', 'qty_tilde_directory', 'qty_underline_directory',
       'qty_space_directory', 'qty_percent_directory', 'qty_plus_directory',
       'qty_hyphen_directory', 'file_length', 'qty_dot_file',
       'qty_dot_directory', 'qty_slash_url', 'qty_slash_directory',
       'directory_length']

# Select a random row from the dataset
random_row = df[features_to_use].sample(n=1)

# Convert the selected row to a dictionary
features = random_row.to_dict(orient='records')[0]

# Define the URL of the /predict endpoint
url = 'http://localhost:8000/predict'

# Send a POST request to the /predict endpoint
response = requests.post(url, json=features)
# Print the response
print(response.json())