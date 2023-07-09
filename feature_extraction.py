from urllib.parse import urlparse
import tldextract
import socket
import whois

def get_activation_time(domain):
    try:
        w = whois.whois(domain)
        if w.creation_date:
            return w.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return None
    except whois.parser.PywhoisError:
        return None

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None
def extract_features(url):
    parsed_url = urlparse(url)
    domain = tldextract.extract(url).domain

    features = {}

    features['asn_ip'] = socket.gethostbyname(domain)  # You can add your logic to get ASN of IP
    features['time_domain_activation'] = get_activation_time(domain)
    features['length_url'] = len(url)
    features['qty_dollar_directory'] = url.count('$')
    features['qty_dollar_file'] = parsed_url.params.count('$')
    features['qty_underline_file'] = parsed_url.params.count('_')
    features['qty_equal_file'] = parsed_url.params.count('=')
    features['qty_and_file'] = parsed_url.params.count('&')
    features['qty_questionmark_directory'] = parsed_url.path.count('?')
    features['qty_tilde_file'] = parsed_url.params.count('~')
    features['qty_asterisk_file'] = parsed_url.params.count('*')
    features['qty_equal_directory'] = parsed_url.path.count('=')
    features['qty_plus_file'] = parsed_url.params.count('+')
    features['qty_comma_file'] = parsed_url.params.count(',')
    features['qty_exclamation_directory'] = parsed_url.path.count('!')
    features['qty_slash_file'] = parsed_url.params.count('/')
    features['qty_space_file'] = parsed_url.params.count(' ')
    features['qty_and_directory'] = parsed_url.path.count('&')
    features['qty_at_directory'] = parsed_url.path.count('@')
    features['qty_hashtag_directory'] = parsed_url.path.count('#')
    features['qty_asterisk_directory'] = parsed_url.path.count('*')
    features['qty_questionmark_file'] = parsed_url.params.count('?')
    features['qty_hashtag_file'] = parsed_url.params.count('#')
    features['qty_exclamation_file'] = parsed_url.params.count('!')
    features['qty_at_file'] = parsed_url.params.count('@')
    features['qty_comma_directory'] = parsed_url.path.count(',')
    features['qty_percent_file'] = parsed_url.params.count('%')
    features['qty_hyphen_file'] = parsed_url.params.count('-')
    features['qty_tilde_directory'] = parsed_url.path.count('~')
    features['qty_underline_directory'] = parsed_url.path.count('_')
    features['qty_space_directory'] = parsed_url.path.count(' ')
    features['qty_percent_directory'] = parsed_url.path.count('%')
    features['qty_plus_directory'] = parsed_url.path.count('+')
    features['qty_hyphen_directory'] = parsed_url.path.count('-')
    features['file_length'] = len(parsed_url.params)
    features['qty_dot_file'] = parsed_url.params.count('.')
    features['qty_dot_directory'] = parsed_url.path.count('.')
    features['qty_slash_url'] = url.count('/')
    features['qty_slash_directory'] = parsed_url.path.count('/')
    features['directory_length'] = len(parsed_url.path)
    return features
