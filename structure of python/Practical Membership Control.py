from ast import Delete
import string
from tkinter.tix import ExFileSelectBox

admins=['ahmed',"osama","mahmoud","sameh","rana"]

login=input("please enter your name:").strip().lower()

  
if login in admins:
  print(f"hello {login} wlcome back")
  print("#" *80)
  quation = input ("do you want to \"ubdate\" your name or \"delete\" or \"add\" (u/d/a) ?").lower()
  print("#" *80)
if quation =="ubdate" or quation=="u":

  thenewname=input("type your new name:")

  admins[admins.index( login )]=thenewname
 
  print( " hello "  +  thenewname )
  print(admins)

elif quation =="delete" or quation=="d":

  Deletename=input("please enter your name to delete:").lower()
 
  admins.remove(login)
 
  print( Deletename  + " is deleted ")

elif quation =="add" or quation=="a":

 addname=input("please enter your name to add:").lower()
 
 admins.append(str(addname))
 
print( addname  + " is inserted ")
print(admins) 




 