#string = str(input("enter string :"))
#index = int(input("enter second num :"))
# def remove(string,index):
#   a=string[:index]
#   b=string[index+1:]
# return a+b
# if index>len(string):
#    print("please enter num == to your string ")
# else:
#    print(f" your string after editing is:{remove(string,index)}")

#string = str(input("enter string :").strip())
#index = int(input("enter second num :"))
# def remove(string, index):
# for j in range(len(string)):
#    if j == index:
#     string = string.replace(string[index],"")
# return(string)
# if string=="":
#    print(f"enter string please.. ")
# elif index> len(string):
#    print("out of range:")
# else:
#    print(f" your string after editing is:{remove(string,index).upper()}")

ans = "y"
while ans == "y":
    string = str(input("enter string:".upper()).strip())
    integer = int(input("enter your index to remove from your string:".upper()))

    def modify_string(string, integer):
        a = string[: integer]
        b = string[integer + 1:]
        return a + b
    if string == "":
        print(f">>>do not use spaces enter string please..".upper())
    elif integer > len(string):
        print(
            f">>>your index is out of the range please enter index equal to your string:[{string.upper()}]".upper())
    else:
        print(
            f"YOUR STRING AFTER EDITING IS:[{modify_string(string.upper(), integer)}] ")
    ans = input(
        "do you want to again this process you can press (y or n): ".strip().upper())
    if ans == "n":
        print("THANKS BUT DONT USE THIS PROGRAM AGAIN..")
ans = "y"
while ans == "y":
 string = str(input("enter string please:".upper()).strip())
 index = int(input("enter num to remove from your string:".upper()))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
 def remove(string, index):
  for j in range(len(string)):
    if j == index:
     string = string.replace(string[index], "")
  return (string)
 if string == "":
   print(f"you shouldn't enter non empty string..  ")
 elif index > len(string):
   print("out of range please enter index to remove from your string :")
 else:
   print(f"your string after editing is:{remove(string,index).upper()}")
 ans = input("you can repeat this process  (y or n): ".strip().upper())
 if ans == "n":
     print("THANKS MAN..")


while True:
 string = str(input("enter string :"))
 index = int(input("enter second num :"))

 def remove(string, index):
  for j in range(len(string)):
    if j == index:
     string = string.replace(string[index], "")
  return (string)
 if string == "":
   print(f"you shouldn't enter non empty string..  ")
 elif index > len(string):
   print("out of range please enter index to remove from your string :")
 elif index<0:
   print("please enter positive num ")
 else:
   print(
       f"your string after removing the number:{remove(string,index).upper()}")
   ans = input("you can repeat this process  (y or n): ".strip().upper())
 if ans == "n":
   print("THANKS MAN..")
   break
