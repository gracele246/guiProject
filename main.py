#Team: Brandon Nguyen, Grace Le, Jack Walker

import re
from tkinter import *

testStrings = ["int A1 = 5;", "float BBB2 = 1034.2","float 	cresult     = 	A1 	+BBB2     *  	BBB2", "if(cresult 	>10):", "print(“TinyPie”)"]

def keywords(input_str):
  #print("<KeyWord, " + input_str + ">")
  return "<KeyWord, " + input_str + ">"

def literals(input_str):
  #print("<lit, " + input_str + ">")
  return "<lit, " + input_str + ">"

def operators(input_str):
  #print("<lit, " + input_str + ">")
  return "<op, " + input_str + ">"

def seperators(input_str):
  #print("<sep, " + input_str + ">")
  return "<sep, " + input_str + ">"

def identifiers(input_str):
  #print("<iden, " + input_str + ">")
  return "<iden, " + input_str + ">"
  
def lexer(input_str): 
  #keywords
  prev_keyword = ""
  input_str = input_str.strip()
  print("Test input string: " + input_str)
  temp = ""
  output = "["
  p = re.search("^if|^else|^int|^float|^string|^double",input_str)
  if(p):
    temp = keywords(p.group())
    input_str = input_str.replace(p.group(),'',1)
    input_str = input_str.strip()
    output += temp + ", "
    print("Check")
    prev_keyword = p.group()
  if(prev_keyword == "if"):
    while input_str != "":
      #seperators
      p = re.search("^\(|^\)|^{|^}|^:|^“|^”|^;$",input_str)
      if(p):
        temp = seperators(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str.strip()
        output += temp + ", "
      #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",input_str)
      if(p):
        temp = identifiers(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
      #operators
      p = re.search("^[=+>*-]",input_str)
      if(p):
        temp = operators(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
      #Identifiers 
      p = re.search("^[A-Za-z]+\d+",input_str)
      if(p):
        temp = identifiers(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
      #literals
      p = re.search("^\d+\.\d+|^\d+|^[A-za-z]+",input_str)
      if(p):
        temp = literals(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
  else:
    while input_str != "":
      #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",input_str)
      if(p):
        temp = identifiers(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
      #operators
      p = re.search("^[=+>*-]",input_str)
      if(p):
        temp = operators(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
    #Identifiers 
      p = re.search("^[A-Za-z]+\d+|^[A-Za-z]+",input_str)
      if(p):
        temp = identifiers(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
        
      #seperators
      p = re.search("^\(|^\)|^{|^}|^:|^“|^”|^;$",input_str)
      if(p):
        temp = seperators(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str.strip()
        output += temp + ", "
      #literals
      p = re.search("^\d+\.\d+|^\d+|^[A-za-z]+",input_str)
      if(p):
        temp = literals(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str = input_str.strip()
        output += temp + ", "
      #p = re.search("^[A-Za-z]+|^[A-Za-z]+\d+",temp)
      #if(p):
        #identifiers(p.group())
        #temp = temp.replace(p.group(),'')
      
  
  output = output[:-2]
  output += "]"
  print("Output <type, token> list: " + output)
  return output
  


#Creating the GUI
root = Tk()
root.title("User GUI")
root.geometry('1000x1000')

firstString = Label(root, text = "Source Code Input:")
firstString.pack()
global line_number 
line_number = 1
global input_list 
input_list = [""]
global output
output = ""
#clear button
def clear():
  my_text.delete(1.0, END)
  my_text2.config(state = "normal")
  my_text2.delete(1.0, END)
  my_text2.config(state = "disabled")
  global line_number
  line_number = 1
  global output
  output = ""
  global input_list
  input_list = [""]
  secondString.configure(text = "Current Processing Line: " + str(line_number))

#splits the lines in the textbox
def start():
  global input_list
  input_list = my_text.get(1.0, END).splitlines()
  
#next button
def get_text():
  global line_number
  global input_list
  if line_number < len(input_list)+1 and input_list != [""]:
    secondString.configure(text = "Current Processing Line: " + str(line_number))
    secondString.pack()
    global output
    lexer_input = input_list[line_number-1]
    output += lexer(lexer_input) + "\n"
    #output += input_list[line_number-1] + "\n"
    line_number += 1
    my_text2.config(state = "normal")
    my_text2.delete(1.0, END)
    my_text2.insert('end',output)
    my_text2.config(state = "disabled")

#quit button
def quit():
  root.destroy()

#formatting
my_text = Text(root , width=60, height=15,font = ("Arial", 16))
my_text.pack(pady=20)

secondString = Label(root, text = "Current Processing Line: " + str(line_number))
secondString.pack() 

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text = "Clear Screen", command = clear)
clear_button.grid(row = 0, column=0)

start_button = Button(button_frame, text = "Start", command = start)
start_button.grid(row = 0, column=1, padx=20)

get_text_button = Button(button_frame, text = "Next Line", command = get_text)
get_text_button.grid(row = 0, column=2, padx=20)

quit_button = Button(button_frame, text = "Quit", command = quit)
quit_button.grid(row = 0, column = 3, padx = 20)

thirdString = Label(root, text = "Source Code Output:")
thirdString.pack(pady = 40)

my_text2 = Text(root , width=60, height=15,font = ("Arial", 16))
my_text2.pack()
my_text2.config(state = "disabled")

root.mainloop()
