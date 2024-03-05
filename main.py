import re
from tkinter import *

testStrings = ["int A1 = 5;", "float BBB2 = 1034.2","float 	cresult     = 	A1 	+BBB2     *  	BBB2", "if(cresult 	>10):", "print(“TinyPie”)"]

root = Tk()
root.title("User GUI")
root.geometry('1000x1000')

firstString = Label(root, text = "Source Code Input:")
firstString.pack()

#clear button
def clear():
  my_text.delete(1.0, 2.0)

#next button
def get_text():
  #for i in range(1, END):
  my_label.config(text=my_text.get(1.0, 2.0))
  clear()
  
  
my_text = Text(root , width=60, height=20,font = ("Arial", 16))
my_text.pack(pady=20)

secondString = Label(root, text = "Current Processing Line:")
secondString.pack() 

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text = "Clear Screen", command = clear)
clear_button.grid(row = 0, column=0)

get_text_button = Button(button_frame, text = "Next Line", command = get_text)
get_text_button.grid(row = 0, column=1, padx=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()

def keywords(string):
  #print("<KeyWord, " + string + ">")
  return "<KeyWord, " + string + ">"

def literals(string):
  #print("<lit, " + string + ">")
  return "<lit, " + string + ">"

def operators(string):
  #print("<lit, " + string + ">")
  return "<op, " + string + ">"

def seperators(string):
  #print("<sep, " + string + ">")
  return "<sep, " + string + ">"

def identifiers(string):
  #print("<iden, " + string + ">")
  return "<iden, " + string + ">"
  
def lexer(string): 
  #keywords
  prev_keyword = ""
  string = string.strip()
  print("Test input string: " + string)
  temp = ""
  output = "["
  p = re.search("^if|^else|^int|^float",string)
  if(p):
    temp = keywords(p.group())
    string = string.replace(p.group(),'',1)
    string = string.strip()
    output += temp + ", "
    prev_keyword = p.group()
  if(prev_keyword == "if"):
    while string != "":
      #seperators
      p = re.search("^\(|^\)|^{|^}|^:|^“|^”|^;$",string)
      if(p):
        temp = seperators(p.group())
        string = string.replace(p.group(),'',1)
        string.strip()
        output += temp + ", "
      #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",string)
      if(p):
        temp = identifiers(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
      #operators
      p = re.search("^[=+>*-]",string)
      if(p):
        temp = operators(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
      #literals
      p = re.search("^\d+\.\d+|^\d+|^[A-za-z]+",string)
      if(p):
        temp = literals(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
  else:
    while string != "":
      #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",string)
      if(p):
        temp = identifiers(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
      #operators
      p = re.search("^[=+>*-]",string)
      if(p):
        temp = operators(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
    #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",string)
      if(p):
        temp = identifiers(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
        
      #seperators
      p = re.search("^\(|^\)|^{|^}|^:|^“|^”|^;$",string)
      if(p):
        temp = seperators(p.group())
        string = string.replace(p.group(),'',1)
        string.strip()
        output += temp + ", "
      #literals
      p = re.search("^\d+\.\d+|^\d+|^[A-za-z]+",string)
      if(p):
        temp = literals(p.group())
        string = string.replace(p.group(),'',1)
        string = string.strip()
        output += temp + ", "
      #p = re.search("^[A-Za-z]+|^[A-Za-z]+\d+",temp)
      #if(p):
        #identifiers(p.group())
        #temp = temp.replace(p.group(),'')
      
  
  output = output[:-2]
  output += "]"
  print("Output <type, token> list: " + output)
  