# status.py
#!/usr/bin/env python3
import smart_open


import urllib3

http = urllib3.PoolManager()
url = 'http://www.pythonchallenge.com/pc/def/zip.html'
resp = http.request('GET', url)
print(resp.status)
print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.read())
