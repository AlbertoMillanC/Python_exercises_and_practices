#IP Geolocation API

# Get Your API: abstractapi.com/api/ip-geolocation-api
import requests as req 
import json
api_key= "YOUR_API_KEY"
api_url= 'https://ipgeolocation.abstractapi.com/v1/?api_key='
ip = input("Enter IP: ") 
response = req.get(api_url + api_key + '&ip_address=' + ip) 
data = json.loads(response.text) 
print(data) 

#clcoding.com