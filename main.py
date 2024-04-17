#Team: Brandon Nguyen, Grace Le, Jack Walker
#Current  Test strings:
#float mathresult1 = 5*4.3 + 2.1;
#float mathresult2 = 4.1 + 2*5.5;
#if (mathresult1 >mathresult2):
#print(“I just built some parse trees”)

import re
from tkinter import *

#Mytokens=[("id","mynum"),("op","="),("float","3.4"),("op","+"),("int","6"),
#("op","+"),("float","2.3"),("sep",";")]
inToken = ("empty","empty")
parse_tree_output = ""
def accept_token():
    global inToken
    print(" accept token from the list:"+inToken[1])
    global Mytokens
    print(Mytokens)
    if(len(Mytokens) != 0):
      inToken=Mytokens.pop(0)

def math():
    #print("\n----parent node math, finding children nodes:")
    global parse_tree_output
    parse_tree_output += "\n----parent node math, finding children nodes:" + "\n"
    global inToken
    #print("math has child node (token): multi")
    parse_tree_output += "math has child node (token): multi" + "\n"
    multi()
    #print("\n")
    #print("math has child node (token): +")
    parse_tree_output += "\nmath has child node (token): +" + "\n"
    accept_token()
    #print("math has child node (token): multi")
    parse_tree_output += "\nmath has child node (token): multi" + "\n"
    multi()
def multi():
    global inToken
    global parse_tree_output
    if(inToken[1] == "+" or inToken[0] == ""):
        #print("child node (token):"+inToken[1])
        parse_tree_output += "child node (token):"+inToken[1] + "\n"
        accept_token()
        return
    elif (inToken[0] == "lit"):
        #print("child node (internal): literal")
        #print(" literal has child node (token):"+inToken[1])
        parse_tree_output += "child node (internal): literal" + "\n"
        parse_tree_output += "   literal has child node (token):"+inToken[1] + "\n"
        accept_token()
        if(inToken[0] == "" or len(inToken) == 0):
          return
        if(inToken[1]=="*"):
            #print("child node (token):"+inToken[1])
            parse_tree_output += "child node (token):"+inToken[1] + "\n"
            accept_token()
            #print("child node (internal): multi")
            parse_tree_output += "child node (internal): multi" + "\n"
            multi()
        elif(len(inToken) > 0 and inToken[1] != "+" and inToken[1] != ";"):
            #print("error, you need * or + after the lit in the mult")
            parse_tree_output += "error, you need * or + after the lit in the mult" + "\n"
def math_exp():
    #print("\n----parent node exp, finding children nodes:")
    global parse_tree_output
    global line_number
    parse_tree_output += "\n####Parse tree for line" +  str(line_number-1) + "####" + "\n"
    parse_tree_output += "\n----parent node exp, finding children nodes:" + "\n"
    global inToken
    typeT,token=inToken
    if(token=="int" or token == "float"):
        #print("child node (internal): KeyWord")
        parse_tree_output += "child node (internal): KeyWord" + "\n"
        #print(" KeyWord has child node (token): "+token)
        parse_tree_output += "   KeyWord has child node (token): "+token + "\n"
        accept_token()
    else:
        #print("expect int or float as the first element of the expression!\n")
        parse_tree_output += "expect int, float, if, or print as the first element of the expression!\n" +token + "\n"
        return
    if(inToken[0]=="iden"):
        #print("child node (internal): identifier")
        parse_tree_output += "child node (internal): identifier" + "\n"
        #print(" identifier has child node (token): "+inToken[1])
        parse_tree_output += "   identifier has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect iden as the second element of the expression!")
        parse_tree_output += "expect iden as the second element of the expression!" + "\n"
        return
    if(inToken[1]=="="):
        #print("child node (token): "+inToken[1])
        parse_tree_output += "child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect = as the third element of the expression!")
        parse_tree_output += "expect = as the third element of the expression!" + "\n"
        return
    #print("child node (internal): math")
    parse_tree_output += "child node (internal): math" + "\n"
    math()
    if(inToken[1] == ";"):
      parse_tree_output += "Parent Node exp, child node (token): " + inToken[1] + "\n"
      accept_token()
      parse_tree_output += "Parse Tree Complete!!!" + "\n"
    else:
      parse_tree_output += "Error, expect ; as the last element of the expression" + "\n"
def if_exp():
    #print("\n----parent node exp, finding children nodes:")
    global parse_tree_output
    global line_number
    parse_tree_output += "\n####Parse tree for line" +  str(line_number-1) + "####" + "\n"
    parse_tree_output += "\n----parent node exp, finding children nodes:" + "\n"
    global inToken
    typeT,token=inToken
    if(token=="if"):
      #print("child node (internal): KeyWord")
      parse_tree_output += "child node (internal): identifier" + "\n"
      #print(" KeyWord has child node (token): "+token)
      parse_tree_output += "   identifier has child node (token): "+token + "\n"
      accept_token()
    else:
      #print("expect int or float as the first element of the expression!\n")
      parse_tree_output += "expect if as the first element of the expression!\n" +token + "\n"
      return
    if(inToken[1]=="("):
        #print("child node (internal): operator")
        parse_tree_output += "child node (internal): operator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   operator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect ( as the second element of the expression!")
        parse_tree_output += "expect ( as the second element of the expression!" + "\n"
        return
    comparison_expr()
    if(inToken[1] == ")"):
        #print("child node (internal): operator")
        parse_tree_output += "child node (internal): operator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   operator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect ) as the second element of the expression!")
        parse_tree_output += "expect ) as the second element of the expression!" + "\n"
        return
    if(inToken[1] == ":"):
        #print("child node (internal): separator")
        parse_tree_output += "child node (internal): separator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   separator has child node (token): "+inToken[1] + "\n"
        accept_token()
        #print("Parse Tree Complete!!!")
        parse_tree_output += "Parse Tree Complete!!!" + "\n"
        
    else:
        #print("expect : as the final element of the expression!")
        parse_tree_output += "expect : as the final element of the expression!" + "\n"
        return
    
def comparison_expr():
    global parse_tree_output
    global inToken
    typeT,token=inToken
    if(inToken[1] == ")"):
       return
    elif(inToken[0] == "iden"):
        #print("child node (internal): identifier")
        parse_tree_output += "child node (internal): identifier" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   identifier has child node (token): "+inToken[1] + "\n"
        accept_token()
    elif(inToken[1] == ">"):
        #print("child node (internal): operator")
        parse_tree_output += "child node (internal): operator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   operator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect > as the second element of the expression!")
        parse_tree_output += "expect > as the second element of the expression!" + "\n"
        return
    comparison_expr()

def print_exp():
    #print("\n----parent node exp, finding children nodes:")
    global parse_tree_output
    global line_number
    parse_tree_output += "\n####Parse tree for line" +  str(line_number-1) + "####" + "\n"
    parse_tree_output += "\n----parent node exp, finding children nodes:" + "\n"
    global inToken
    typeT,token=inToken
    if(token=="print"):
      #print("child node (internal): identifier")
      parse_tree_output += "child node (internal): identifier" + "\n"
      #print(" KeyWord has child node (token): "+token)
      parse_tree_output += "   identifier has child node (token): "+token + "\n"
      accept_token()
    else:
      #print("expect print as the first element of the expression!\n")
      parse_tree_output += "expect print as the first element of the expression!\n" +token + "\n"
      return
    if(inToken[1]=="("):
        #print("child node (internal): operator")
        parse_tree_output += "child node (internal): operator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   operator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect ( as the second element of the expression!")
        parse_tree_output += "expect ( as the second element of the expression!" + "\n"
        return
    if(inToken[1]=="“"):
        #print("child node (internal): separator")
        parse_tree_output += "child node (internal): separator" + "\n"
        #print(" separator has child node (token): "+inToken[1])
        parse_tree_output += "   separator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect “ as the third element of the expression!")
        parse_tree_output += "expect “ as the third element of the expression!" + "\n"
        return 
    if(inToken[0]=="lit"):
        #print("child node (internal): literal")
        parse_tree_output += "child node (internal): literal" + "\n"
        #print(" literal has child node (token): "+inToken[1])
        parse_tree_output += "   literal has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect literal after quotes!")
        parse_tree_output += "expect literal after quotes!" + "\n"
        return 
    if(inToken[1]=="”"):
        #print("child node (internal): separator")
        parse_tree_output += "child node (internal): separator" + "\n"
        #print(" separator has child node (token): "+inToken[1])
        parse_tree_output += "   separator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect “ after string in expression!")
        parse_tree_output += "expect “ after string in expression!" + "\n"
        return
    if(inToken[1] == ")"):
        #print("child node (internal): operator")
        parse_tree_output += "child node (internal): operator" + "\n"
        #print(" operator has child node (token): "+inToken[1])
        parse_tree_output += "   operator has child node (token): "+inToken[1] + "\n"
        accept_token()
    else:
        #print("expect ) as the second element of the expression!")
        parse_tree_output += "expect ) as the second element of the expression!" + "\n"
        return
    if(inToken[1] == ";"):
        parse_tree_output += "child node (token): " + inToken[1] + "\n"
        accept_token()
    parse_tree_output += "Parse Tree Complete!!!" + "\n"
    return

  
def parser():
    global Mytokens
    global inToken
    global parse_tree_output
    inToken=Mytokens.pop(0)
    if(inToken[1] == "int" or inToken[1] == "float"):
      math_exp()
    elif(inToken[1] == "if"):
      if_exp()
    elif(inToken[1] == "print"):
      print_exp()
    return
testStrings = ["int A1 = 5;", "float BBB2 = 1034.2","float 	cresult     = 	A1 	+BBB2     *  	BBB2", "if(cresult 	>10):", "print(“TinyPie”)"]
Mytokens = []
def keywords(input_str):
  #print("<KeyWord, " + input_str + ">")
  global Mytokens
  Mytokens.append( ("KeyWord", input_str))
  return "<KeyWord, " + input_str + ">"

def literals(input_str):
  #print("<lit, " + input_str + ">")
  global Mytokens
  Mytokens.append( ("lit", input_str))
  return "<lit, " + input_str + ">"

def operators(input_str):
  #print("<lit, " + input_str + ">")
  global Mytokens
  Mytokens.append( ("op", input_str))
  return "<op, " + input_str + ">"

def seperators(input_str):
  #print("<sep, " + input_str + ">")
  global Mytokens
  Mytokens.append( ("sep", input_str))
  return "<sep, " + input_str + ">"

def identifiers(input_str):
  #print("<iden, " + input_str + ">")
  global Mytokens
  Mytokens.append( ("iden", input_str))
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
        
      #separators
      p = re.search("^\(|^\)|^{|^}|^:|^“|^”|^;$",input_str)
      if(p):
        temp = seperators(p.group())
        input_str = input_str.replace(p.group(),'',1)
        input_str.strip()
        output += temp + ", "
        prev_keyword = p.group()

      #Multi word strings
      if prev_keyword == "“":
        temp = ""
        while input_str != "" and input_str[0:1] != "”":
          p = re.search("^[A-za-z]+\d+|^\d+\.\d+|^\d+|^[A-za-z]+",input_str)
          temp += p.group() + " "
          input_str = input_str.replace(p.group(),'',1)
          input_str = input_str.strip()
        temp = temp[:-1]
        print("CHECK: '" + temp + "'")
        temp = literals(temp)
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
  #print("Output <type, token> list: " + output)
  return output
  


#Creating the GUI
root = Tk()
root.title("User GUI")
root.geometry('1000x1000')

firstString = Label(root, text = "Source Code Input:")
firstString.grid(row=0)
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

  my_text3.config(state = "normal")
  my_text3.delete(1.0, END)
  my_text3.config(state = "disabled")

  global line_number
  line_number = 1
  global output
  output = ""
  global input_list
  input_list = [""]
  global parse_tree_output
  parse_tree_output = ""
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
    secondString.grid()
    global output
    lexer_input = input_list[line_number-1]
    output += lexer(lexer_input) + "\n"
    #output += input_list[line_number-1] + "\n"
    line_number += 1
    my_text2.config(state = "normal")
    my_text2.delete(1.0, END)
    my_text2.insert('end',output)
    my_text2.config(state = "disabled")
    
    global Mytokens
    global inToken
    global parse_tree_output
    parser()
    my_text3.config(state = "normal")
    my_text3.delete(1.0, END)
    my_text3.insert('end',parse_tree_output)
    my_text3.config(state = "disabled")

#quit button
def quit():
  root.destroy()

#formatting
my_text = Text(root , width=60, height=15,font = ("Arial", 16))
my_text.grid(row = 1)

secondString = Label(root, text = "Current Processing Line: " + str(line_number))
secondString.grid(row = 2)

button_frame = Frame(root)
button_frame.grid()

clear_button = Button(button_frame, text = "Clear Screen", command = clear)
clear_button.grid(row = 1, column=0, )

start_button = Button(button_frame, text = "Start", command = start)
start_button.grid(row = 1, column=1, padx=20)

get_text_button = Button(button_frame, text = "Next Line", command = get_text)
get_text_button.grid(row = 1, column=2, padx=20)

quit_button = Button(button_frame, text = "Quit", command = quit)
quit_button.grid(row = 1, column = 3, padx = 20)

thirdString = Label(root, text = "Source Code Output:")
thirdString.grid(row = 0, column = 4)

my_text2 = Text(root , width=60, height=15,font = ("Arial", 16))
my_text2.grid(padx = 30, row = 1, column = 4)
my_text2.config(state = "disabled")

fourthString = Label(root, text = "Parse tree:")
fourthString.grid(row = 2, column = 4)

my_text3 = Text(root , width=60, height=15,font = ("Arial", 16))
my_text3.grid(padx = 30, row = 3, column = 4)
my_text3.config(state = "disabled")

root.mainloop()

