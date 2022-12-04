# def hello():
#base = int(input("enter base of tri:"))
#height=int(input("enter height:"))
#x = (base * height) / 2
# return x
# print(hello())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1
#base = int(input("enter num:"))
#height = int(input("enter num:"))
# def tri_area(base, height):
# x = (base * height) / 2
# return int(x)
# print(tri_area(base,height))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2
#hours=int(input("enter hours"))
# def how_many_seconds(hours):
#    hours=hours*60*60
#    return hours
# print(how_many_seconds(hours))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>3

# def next_edge():
#side1=int(input("enter side 1:"))
#side2 = int(input("enter side 2:"))
# s=(side1+side2)-1
# return s
# print(next_edge())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>4

# def string_int():
#    txt=str(input("enter txt:"))
#    txt_converted=int(txt)
#    return txt_converted
# print(string_int())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>5

# def calculate_exponent():
#    num=int(input("enter num: "))
#    exp=int(input("enter exponent"))
#    n=num**exp
#    return n
# print(calculate_exponent())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>6
# def addition():
#    num=int(input("enter num:"))
#    N=num+1
#    return(N)
# print(addition())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>7
# def squaed():
#    a=int(input("enter frist num:"))
#    a=int(input("enter second num:"))
#    return a*a
# print(squaed())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>8
# def sum_polygon():
#    n = int(input("enter sum_polygon: "))
#    sum = (n - 2) * 180
#    return sum
# print(sum_polygon())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>9
# def cubes(a):
# return a ** 3
# print(cubes(3))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>10

# def football_points(wins,draws,losses):
#    a = wins*3+draws*1+losses*0
#    return (a)
# print(football_points(3,4,2))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>11
# def convert():
#    minutes=int(input("enter minutes:"))
#    a=minutes *60
#    return (a)
# print(convert())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>12
# def circuit_power():
#    voltage=int(input("enter voltage:"))
#    current = int(input("enter current:"))
#    a=voltage*current
#    return a
# print(circuit_power())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>13
# def convert():
#   hours=int(input("enter hours:"))
#    minutes=int(input("enter minutes"))
#   a=hours*60*60+minutes*60
#   return (a)
# print(convert())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>14
# def animals():
#    chickens = int(input("enter how many leg of chickens"))
#    cows= int(input("enter how many leg of cows"))
#    pigs = int(input("enter how many leg of pigs"))
#    a=chickens*2+cows*4+pigs*4
#    return a
# print(animals())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>15
# def calc_age():
#    age=int(input("enter age:"))
#    a=age*365
#    return a
# print(calc_age())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>16(find the missing character )
#import string
#a = string.ascii_lowercase
#string = str(input("enter string:"))
#for i in a:
#    if i not in string:
#        print(f"[{i}] is_missing_kay")
#else:
#    print("all missing letters is found...")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>17 ( another solving to find the missing character)
#import string
#def find_missing_letter_in(givin_letter):
# alpha = string.ascii_lowercase
# start = alpha.index(givin_letter[0])
# for l in alpha[start:]:
#     if l not in givin_letter:
#         return l
#print(find_missing_letter_in("abcdefgi"))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>18 (reverse numbers)
#import string
#list = []
#digit =str(input("enter numbers:/"))
# for i in digit:
#    list.append(i)
# print(list[::-1])
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>19(another solving of reverse numbers)
# def convert():
#   numbers=int(input("enter numbers:"))
#   return [int(num) for num in str(numbers)[::-1]]
# print(convert())
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>20(remove index from string)
# def modify_string():
#    character = str(input(">>>please insert string:".upper()).strip())
#    num = int(input("enter your index to remove from your string:".upper()))
#    s = character[: num]  # we make slicing from (0 to num)
#    # then increased the num by (1) because the character not include the end in num..
#    i = character[num + 1:]
#    return s + i  # then return s & i and concatenate them.
# print(modify_string())
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>21