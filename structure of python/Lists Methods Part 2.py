# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4, 5]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

# to add numbers to list.....
number_list = []
n = int(input("Enter the list size \n"))
for i in range(1, n+1):
    print(f" you have try{i}")
    item = int(input())
    number_list.append(item)
print("User list is:", number_list)

# to add strings to list....
string_list = []
n = int(input("Enter the list size "))
for i in range(1, n+1):
    print(f" you have try{i}")
    item = str(input())
    string_list.append(item)
print("User list is:", string_list)

# another solving......
ans = "y"
string_list = []
while ans == "y":
    n = str(input("Enter the list size \n "))
    string_list.append(n)
    print("User list is:", string_list)
    ans = input("do you want to countinue you can press (y or n): ")
print(f"YOUR LIST IS:{string_list}")
print("THANKS")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
integer_list = []
square_list = []
n = abs(int(input("Enter the list size: \n ")))
for n in range(1, n+1):
    integer_list.append(n)
    square_list.append(n*n)
    print("User list  before square:", integer_list)
    print("User list  after square:", square_list)
    ans = input("do you want to countinue you can press (y or n): ")
    if ans == "n":
        break
print(f"YOUR LIST before square :{integer_list}", sep="")
print(f"YOUR LIST after square  :{square_list}", sep="")
print("THANK YOU FOR USING OUR 'program':")

ans = "y"
list1 = []
list2 = []
while ans == "y":
    num = int(input("enter range:"))
    for i in range(1, num+1):
        print(f" you have try{i}")
        item = eval(input("enter something else:"))
        list1.append(item)
        list2.append(item*item)
    ans = input("do you want add something else to list : (y or n):")
print(f" list 1 = {list} ")
print(f" the square of list 1 is = {list2} ")
