# Get Your 
#API: https://cutt.ly/cuttly-api
# #pip install cuttpy
from cuttpy import Cuttpy 
api_key = 'YOUR_API_KEY'
cuttly = Cuttpy (api_key)
resp = cuttly.shorten("http://www.clcoding.com") 
print (resp.shortened_url) 
#clcoding.com