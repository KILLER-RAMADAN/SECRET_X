ans = "y"
while ans == "y":
    max = eval(input("ENTER 'NUMBER' PLEASE>>>"))
    if max < 0:
        print(F"PLEASE ENTER POSITIVE NUMBER>>> [{abs(max)}]")
    else:
        even = 0
        odd = 0
        for num in range(0, max+1):
            if num % 2 != 0:
                odd += 1
                print(f"[{num}] is odd.")
            # else:
                # if you want to remove even numbers> delete line[13,14,15,16,18]
                #even += 1
                #print(f"[{num}] is even.")
        print(f"the count of even numbers is: [{odd}]")
        #print(f"the count of odd  numbers is: [{even}]")
        ans = input(
            "do you want to again this process you can press (y or n): ".strip().upper())
        if ans == "n":
            print("THANKS MAN..")
# QUESTION 2:
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


# QUESTION 3:
with open("ahmed ramadan.txt") as f:
    list_body = f.readlines()
# to print the first list..
print(list_body)
# to remove lines in second line...
list_body = [x.strip() for x in list_body]
print(list_body)
f.close()


# another solving for question 3
list = []
with open("ahmed ramadan.txt") as f:
    list_body = f.readlines()
# to print the first list..
print(list_body)
# to remove lines in second ...
for i in list_body:
    list.append(i.strip())
print(list)
f.close()
()

# another solving for question 3

list = []
list_body = open("ahmed ramadan.txt", "r")
f = list_body.readlines()
print(f)
for i in f:
    list.append(i.strip())
print(list)
list_body.close()


list = []
list_body = open("C:\\Users\\ahmed\\Desktop\\ahmed ramadan.txt", "r")
read = list_body.readlines()
print(read)
for i in read:
    list.append(i.strip())
print(list)
list_body.close()

with open("C:\\Users\\ahmed\\Desktop\\ahmed ramadan.txt") as f:
    list_body = f.readlines()
# to print the first list..
print(list_body)
# to remove lines in second line...
list_body = [x.strip() for x in list_body]
print(list_body)
# file after finishing closing by default...
