import urllib
url = "https://data.messari.io/api/v1/assets/btc/metrics"
print(urllib.request.urlopen(url).read())
