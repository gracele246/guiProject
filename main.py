import re
from tkinter import *

testStrings = ["int A1 = 5;", "float BBB2 = 1034.2","float 	cresult     = 	A1 	+BBB2     *  	BBB2", "if(cresult 	>10):", "print(“TinyPie”)"]

root = Tk()

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
  
if __name__ == '__main__':
  print("Hello World")