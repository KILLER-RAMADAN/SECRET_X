from ast import Mod
from operator import mod
import string
print("#" *50)
print("please use ('numbers') only....")
print("#" *50)
num=int(input("please enter your num:")) 
result=num % 2  
if result==0:
 print("your num is even ")
elif result==1:
 print("your num is odd")
else:
    print("you must chouse number")


    if num < 0:
    print("please enter positive num:")
elif result == 0:
    print(f"{num} is even :")
elif result != 2:
    print(f"{num} is odd :")


if num < 0:
    print("please enter positive num:")
elif num == 0:
    print(f"{num} is even :")
elif num != 2:
    print(f"{num} is odd :")

for n in range(num):
    print(n)


if num < 0:
    print("please enter positive num:")
elif num % 2 == 0:
    print(f"{num} is even :")
elif num % 2 !=0:
    print(f"{num} is odd :")

for n in range(num):
    print(n)
