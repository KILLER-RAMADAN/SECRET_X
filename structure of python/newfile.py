ask = "y"
while ask == "y":
    max = eval(input("ENTER 'NUMBER' PLEASE>>>"))
    if max < 0:
        print(F"PLEASE ENTER POSITIVE NUMBER>>> [{abs(max)}]")
    else:
     #double = 0
     single = 0
     for num in range(0, max+1):
        if num % 2 != 0:
            single += 1
            print(f"[{num}] is odd.")
        # else:
            # if you want to remove even numbers> delete lines[7,13,14,15,16,18]
            #double += 1
            #print(f"[{num}] is even.")
     print(f"the count of even numbers is: [{single}]")
     #print(f"the count of odd  numbers is: [{double}]")
     ask = input(
         "do you want to again this process you can press (y or n): ".strip().upper())
     if ask == "n":
        print("THANKS (:")
