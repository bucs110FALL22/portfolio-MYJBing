import CalendarAPI
import EmailAPI

def main():
  output1=CalendarAPI.CalendarAPI()
  output1.get()
  
  output2=EmailAPI.EmailAPI()
  output2.get()
  
  
main()