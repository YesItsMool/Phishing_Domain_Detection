from urllib.parse import urlparse
import tldextract
import aiodns
import whois
import socket
import datetime

async def get_ip_address(domain):
    resolver = aiodns.DNSResolver()
    try:
        result = await resolver.query(domain, 'A')
        if result:
            return result[0].host
        else:
            return None
    except (aiodns.error.DNSError, aiodns.error.AioDnsError):
        return None

async def get_activation_time(domain):
    try:
        w = whois.whois(domain)
        if w.creation_date:
            if isinstance(w.creation_date, list):
                return w.creation_date[0]
            else:
                return w.creation_date
        else:
            return None
    except whois.parser.PywhoisError:
        return None

async def extract_features(url):
    parsed_url = urlparse(url)
    domain = tldextract.extract(url).domain

    features = {}

    try:
        features['asn_ip'] = float(socket.gethostbyname(domain))
    except socket.gaierror:
        features['asn_ip'] = 0.0

    activation_time = await get_activation_time(domain)
    if activation_time:
        features['time_domain_activation'] = activation_time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        features['time_domain_activation'] = 0.0

    features['length_url'] = float(len(url))
    features['qty_dollar_directory'] = float(url.count('$'))
    features['qty_dollar_file'] = float(parsed_url.params.count('$'))
    features['qty_underline_file'] = float(parsed_url.params.count('_'))
    features['qty_equal_file'] = float(parsed_url.params.count('='))
    features['qty_and_file'] = float(parsed_url.params.count('&'))
    features['qty_questionmark_directory'] = float(parsed_url.path.count('?'))
    features['qty_tilde_file'] = float(parsed_url.params.count('~'))
    features['qty_asterisk_file'] = float(parsed_url.params.count('*'))
    features['qty_equal_directory'] = float(parsed_url.path.count('='))
    features['qty_plus_file'] = float(parsed_url.params.count('+'))
    features['qty_comma_file'] = float(parsed_url.params.count(','))
    features['qty_exclamation_directory'] = float(parsed_url.path.count('!'))
    features['qty_slash_file'] = float(parsed_url.params.count('/'))
    features['qty_space_file'] = float(parsed_url.params.count(' '))
    features['qty_and_directory'] = float(parsed_url.path.count('&'))
    features['qty_at_directory'] = float(parsed_url.path.count('@'))
    features['qty_hashtag_directory'] = float(parsed_url.path.count('#'))
    features['qty_asterisk_directory'] = float(parsed_url.path.count('*'))
    features['qty_questionmark_file'] = float(parsed_url.params.count('?'))
    features['qty_hashtag_file'] = float(parsed_url.params.count('#'))
    features['qty_exclamation_file'] = float(parsed_url.params.count('!'))
    features['qty_at_file'] = float(parsed_url.params.count('@'))
    features['qty_comma_directory'] = float(parsed_url.path.count(','))
    features['qty_percent_file'] = float(parsed_url.params.count('%'))
    features['qty_hyphen_file'] = float(parsed_url.params.count('-'))
    features['qty_tilde_directory'] = float(parsed_url.path.count('~'))
    features['qty_underline_directory'] = float(parsed_url.path.count('_'))
    features['qty_space_directory'] = float(parsed_url.path.count(' '))
    features['qty_percent_directory'] = float(parsed_url.path.count('%'))
    features['qty_plus_directory'] = float(parsed_url.path.count('+'))
    features['qty_hyphen_directory'] = float(parsed_url.path.count('-'))
    features['file_length'] = float(len(parsed_url.params))
    features['qty_dot_file'] = float(parsed_url.params.count('.'))
    features['qty_dot_directory'] = float(parsed_url.path.count('.'))
    features['qty_slash_url'] = float(url.count('/'))
    features['qty_slash_directory'] = float(parsed_url.path.count('/'))
    features['directory_length'] = float(len(parsed_url.path))

    return features
