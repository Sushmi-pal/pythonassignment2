class valid:
  def __init__(self,text):
    self.text = str(text)
  def val(self):
    for i in range(0,len(self.text)-1,2):
      if ((self.text[i]== '{') and (self.text[i+1]=='}')) or ((self.text[i]== '(') and (self.text[i+1]==')')) or ((self.text[i]== '[') and (self.text[i+1]==']')):
        if (i==len(self.text)-2):
          print("valid")
      else:
        print('invalid')
        break
s=valid('[](){}')
s.val()