import pandas as pd

# Load the dataset
df = pd.read_csv('dataset_full.csv')

# Select the required features
features = df[['asn_ip','time_domain_activation', 'length_url','qty_dollar_directory', 'qty_dollar_file', 'qty_underline_file','qty_equal_file', 'qty_and_file', 'qty_questionmark_directory','qty_tilde_file', 'qty_asterisk_file', 'qty_equal_directory','qty_plus_file', 'qty_comma_file', 'qty_exclamation_directory','qty_slash_file', 'qty_space_file', 'qty_and_directory','qty_at_directory', 'qty_hashtag_directory', 'qty_asterisk_directory','qty_questionmark_file', 'qty_hashtag_file', 'qty_exclamation_file','qty_at_file', 'qty_comma_directory', 'qty_percent_file','qty_hyphen_file', 'qty_tilde_directory', 'qty_underline_directory','qty_space_directory', 'qty_percent_directory', 'qty_plus_directory','qty_hyphen_directory', 'file_length', 'qty_dot_file','qty_dot_directory', 'qty_slash_url', 'qty_slash_directory','directory_length']]

# Save the processed dataset to a new CSV file
features.to_csv('processed_dataset.csv', index=False)
