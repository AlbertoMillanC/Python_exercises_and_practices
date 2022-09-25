# api dayli news

#Daily News API 
# # Get Your API: https://www.voicerss.org/api/ 
import requests 
api_key ="Your API Key" 
api_url= "http://api.voicerss.org/"
Text= "Hi from Medium.com" 
response = requests.get(api_url + "?key=" + api_key + "&hl=en-us&v=Amy&src=" + Text)      

# Download the voice file 
with open ("audio.mp3", "wb") as file:                                                                                                                                    file.write(response.content)
