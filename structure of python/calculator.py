from ast import Break


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y


while  True:
  print("choise any number")
  choice=input("1=add,2=subtract,3=multiply,4=divide")
  if choice in("1,2,3,4"):
     
      num1=int(input("enter ypur frist num:"))
     
      num2=int(input("enter your second num:"))
      if(choice=="1"):
        
        print(num1,"+",num2,"=",add(num1,num2))
      elif(choice=="2"):
       
        print(num1,"-",num2,"=",sub(num1,num2))
      elif(choice=="3"):
       
       print(num1,"*",num2,"=",mult(num1,num2))
      elif(choice=="4"):
       
       print(num1,"/",num2,"=",div(num1,num2))
    
      
  else:
       print("invalid input")



### anouther calc:

#from ast import operator
#print("*" *50) 
#print("please 'use numbers''' only")
#print("*" *50) 
#num1=float(input("please enter your frist num:"))
#operator=input("enter operator:")
#num2=float(input("please enter your soucend num:"))
#if operator=="+":
   # print(num1+num2)

#elif operator=="-" :
 #   print(num1-num2)

#elif operator=="*":
#    print(num1*num2)

#elif operator=="/":
 #   print(num1/num2)
#else:
  #  print("please chouse number")
