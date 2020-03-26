import requests

def get_root_https(short_url: str):
    return requests.head('https://' + short_url).headers['location']

def get_root_http(short_url: str):
    return requests.head('http://' + short_url).headers['location']