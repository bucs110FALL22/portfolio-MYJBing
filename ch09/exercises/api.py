import json
import requests

#Import 
#API Url

counter = requests.get("https://v2.jokeapi.dev/joke/Any").json()


print(counter)
  


#Retrieve 

import requests 

response = requests.get("https://randomuser.me/api/")
response.text