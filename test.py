import urllib.request
response = urllib.request.urlopen("http://www.tax.sh.gov.cn/pub/")
print(response.read())