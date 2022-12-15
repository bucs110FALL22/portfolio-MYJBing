class StringUtility:
  def __init__(self, string):
    self.string = string

  # String Function
  def __str__(self):
    return self.string


  def __str__(self):
        """Returns the string itself, unchanged."""
        return self.string

  def vowels(self):
      """Counts the number of vowels in the string"""
      count = 0
      for i in self.string:
        if(i=="a" or i=="e"or i=="i" or i=="o" or i=="u"):
          count = count + 1
        if (count >=5):
          return "many"
     
      return str(count)
  
  def bothEnds(self):
      """Returns a string made of the first 2 and last 2 chars of the original string"""
    
      size = len(self.string)
      if (size <= 2):
        return ""
      else:
        stng = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
        return stng
  
  def fixStart(self):
      """Returns a string where the first character have been changed to '*'"""
      if len(self.string)>=1:
         first_char = self.string[0]
         return first_char+self.string[1:].replace(first_char,"*")
      else:
        return ""
  
  def asciiSum(self):
      """Returns the sum of the ASCII values of everything in the string."""
  
      str = 0
      for i in range(len(self.string)):
          str = str + ord(self.string[i])
      return str
    
  #ord function returns the character's equivalent integer value.
  
  def cipher(self):
        """Returns an encoded string. """
        
        upper = 65
        lower = 97
        alpha = 26
        list = ""
  
        for j in self.string:
          if j == " ":
            list = list+j
          elif j.isupper():
            list = list+chr((ord(j)+len(self.string)-upper)%alpha+upper)
          else:
            list = list+chr((ord(j)+len(self.string)-lower)%alpha+lower)
        return list




  


