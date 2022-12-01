ans = "y"
while ans == "y":
 mta = int(input("enter mta grade :"))
 tma = int(input("enter mta grade :"))
 total = mta+tma
 if mta <= 15 and tma <= 15:
    if mta == 0 and tma == 0:
        print("you are fail..")
    else:
     print(f" your grade is :{total} congratulations ..")
 else:
    print("please enter number from 1 to 30....")
 ans = input("do you want again this process..(y/n) ")
if ans == "n":
 print("thanks")
