from urllib.parse import urlparse
import tldextract
import socket
import ssl
import OpenSSL

def extract_features_from_url(url: str):
    features = {}

    # Parse the URL
    parsed_url = urlparse(url)
    extracted = tldextract.extract(url)

    # Extract basic features from the URL
    features['length_url'] = len(url)
    features['qty_slash_url'] = url.count('/')
    features['qty_dot_url'] = url.count('.')
    features['qty_hyphen_url'] = url.count('-')
    features['qty_underline_url'] = url.count('_')
    features['qty_questionmark_url'] = url.count('?')
    features['qty_equal_url'] = url.count('=')
    features['qty_at_url'] = url.count('@')
    features['qty_and_url'] = url.count('&')
    features['qty_exclamation_url'] = url.count('!')
    features['qty_space_url'] = url.count(' ')
    features['qty_tilde_url'] = url.count('~')
    features['qty_comma_url'] = url.count(',')
    features['qty_plus_url'] = url.count('+')
    features['qty_asterisk_url'] = url.count('*')
    features['qty_hashtag_url'] = url.count('#')
    features['qty_dollar_url'] = url.count('$')
    features['qty_percent_url'] = url.count('%')

    # Extract domain based features
    features['length_domain'] = len(extracted.domain)
    features['qty_dot_domain'] = extracted.domain.count('.')
    features['qty_hyphen_domain'] = extracted.domain.count('-')
    features['qty_underline_domain'] = extracted.domain.count('_')

    # Extract subdomain based features
    features['length_subdomain'] = len(extracted.subdomain)
    features['qty_dot_subdomain'] = extracted.subdomain.count('.')
    features['qty_hyphen_subdomain'] = extracted.subdomain.count('-')
    features['qty_underline_subdomain'] = extracted.subdomain.count('_')

    # Extract directory based features
    features['length_directory'] = len(parsed_url.path)
    features['qty_slash_directory'] = parsed_url.path.count('/')
    features['qty_dot_directory'] = parsed_url.path.count('.')
    features['qty_hyphen_directory'] = parsed_url.path.count('-')
    features['qty_underline_directory'] = parsed_url.path.count('_')

    # Extract file based features
    features['length_file'] = len(parsed_url.params)
    features['qty_slash_file'] = parsed_url.params.count('/')
    features['qty_dot_file'] = parsed_url.params.count('.')
    features['qty_hyphen_file'] = parsed_url.params.count('-')
    features['qty_underline_file'] = parsed_url.params.count('_')

    # Extract ASN of IP
    ip = socket.gethostbyname(extracted.domain)
    # You need to use an external service to get the ASN of the IP
    # features['asn_ip'] = get_asn(ip)

    # Extract activation and expiration time of the domain
    # You need to use WHOIS data or an external service to get these features
    # features['time_domain_activation'] = get_activation_time(extracted.domain)
    # features['time_domain_expiration'] = get_expiration_time(extracted.domain)

    return features
