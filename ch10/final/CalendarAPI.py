import requests

class CalendarAPI :
  def __init__(self):
      self.url=     "https://timezone.abstractapi.com/v1/current_time/?api_key=cde20104d2fe47d6afc49ac7a481b87f&location=Oxford, United Kingdom"
    
  def get(self):
    self.output1 = requests.get(self.url).json()
    

    for key,value in self.output1.items():
       print(key,':',value)   
  
#keys=self.output1.keys()
#print(keys)  'Displays Keys if needed'



