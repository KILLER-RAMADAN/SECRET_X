ans = "y"
while ans == "y":
 n = int(input("Enter how many values:"))
 even = 0
 odd = 0
 pos = 0
 neg = 0
 for i in range(n):
    x = eval(input("Enter values:"))
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
 print("Even:", even)
 print("Odd:", odd)
 print("Positive:", pos)
 print("Negative:", neg)
 ans = input("do you want to again this process you can press (y or n): ")
 if ans == "n":
     print("THANKS MAN..")


#num=eval(input("enter num:"))

#for i in range (num,num+12,2):
  #  if i%2==0:
   #     print(f"[{i}] is even")
   # else:
    #    print(f"[{i}] is odd")
x = eval(input("Enter a number:"))
print("The list of the 6 consecutive odd numbers is:")
for i in range(x, x+12, 2):
    if i % 2 == 0:
        print(i)
    else:
        print(i)
