import requests

# https://developers.google.com/youtube/v3/docs/search/list

params = {
    'part': 'snippet',
    'key': 'AIzaSyC8ZPXfbiZUEQ7hMJKsDhxhpAUHWCfsI7s',

    'location': '52.3159376, 4.7432175',  # Amsterdam Airport Schiphol 's coords
    'locationRadius': '1km',
    'publishedAfter': '2012-01-01T00:00:00+01:00',
    'publishedBefore': '2013-01-01T00:00:00+01:00',
    'type': 'video'
}

res = requests.get(
    "https://www.googleapis.com/youtube/v3/search", params=params).json()

print(res['pageInfo']['totalResults'])  # 0
