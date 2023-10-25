from Url_Features import *


def extract_features(url):
    url_features = []

    i = hostname_length(url)
    url_features.append(i)

    i = urlpath_length(url)
    url_features.append(i)
    
    i = having_ip_address(url)
    url_features.append(i)
    
    i = shortening_service(url)
    url_features.append(i)

    i = get_counts(url)
    url_features = url_features + i

    i = digit_count(url)
    url_features.append(i)

    i = letter_count(url)
    url_features.append(i)

    return url_features

 