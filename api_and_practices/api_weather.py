# Get Your API: https://m30.com/weather/api 
# 
import requests 
api_key = "YmVjYjc20DUtMDdhNS00MzRjLT1iZmYtNDAxNzM1MmYyZTk3" 
url = "https://api.m3o.com/v1/weather/Forecast" 
params= {"days":"2","location": "Switzerland"} 
headers = { 'Content-Type': "application/json", 
           'Authorization': "Bearer" + api_key 
           }
response = requests.request("GET", url, headers-headers, params=params)
print (response.json)




#clcoding.com <bound method Response.json of <Response [200]>>