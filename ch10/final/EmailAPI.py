#https://emailvalidation.abstractapi.com/v1/?api_key=77996d4338d44e0bab4573fa05811b15&email=youhanjaigirdar2@gmail.com
import requests

class EmailAPI: 
  def __init__(self):
   self.url= 'https://emailvalidation.abstractapi.com/v1/?api_key=77996d4338d44e0bab4573fa05811b15&email=youhanjaigirdar2@gmail.com'

  def get(self):
    self.output2 = requests.get(self.url).json()
    print(self.output2)

  