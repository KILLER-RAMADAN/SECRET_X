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
#import string
#a = string.ascii_lowercase
# number = { 1111111111:"Amal",
#         2222222222:"Mohamed",
#         3333333333:"Khadija",
# #        4444444444:"Abdullah",
#         5555555555:"Rawan" ,
#         6666666666:"Faisel",
#         8888888888: "Layla"}
#choose = int(input("enter number of member: "))
# base=10
# if len(str(choose)) < base or len(str(choose)) >base  or  type(choose) == a:
#    print("this is invalid number")
# elif choose == 1111111111:
#    print(f"her name is :[{number[1111111111]}] and her number is:+20({choose})")
# elif choose == 2222222222:
#   print(f"his name is :[{number[2222222222]}] and his number is :+20({choose})")
# elif choose == 3333333333:
#    print(f"her name is :[{number[3333333333]}] and her number is :+20({choose})")
# elif choose == 4444444444:
#    print(f"his name is :[{number[4444444444]}] and his number is :+20({choose})")
# elif choose == 5555555555:
#    print(f"her name is :[{number[5555555555]}] and her number is :+20({choose})")
# elif choose == 6666666666:
#     print(f"his name is :[{number[6666666666]}] and his number is :+20({choose})")
# elif choose == 8888888888:
#    print(f"her name is :[{number[8888888888]}] and hher number is :+20({choose})")
# else:
#    print("sory, the number is not found")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(another solve of 21)
#import string
# a=string.ascii_lowercase
#choose = int(input("enter number of member: "))
# base=10
# number={2222222222: "Mohamed",
#        3333333333: "Khadija",
#        4444444444: "Abdullah",
#       5555555555: "Rawan",
#       6666666666: "Faisel",
#        8888888888: "Layla"}
# if len(str(choose)) < base or len(str(choose)) > base :
#    print("this is invalid number")
# for chiledkey, bigvalue in number.items():
# if choose==chiledkey:
#   print(f"{bigvalue}")#
# else:
# print("thanks for using our program")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(22>>we use enumerate function)
#a = str(input("enter string:").replace(" ", "").strip())
#for count, i in enumerate(a):
#print(f"index[{count}]<<>> {i}", end=" // ")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(23)
#input = int(input("enter num:"))
#sum = 0
#for i in range(1, input+1):
#    sum = sum+i
#print(sum)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(24)
#from math import *
#num1 = int(input("enter num1:"))
#num2 = int(input("enter num2:"))
#dev = num1/num2
#print(f"'{floor(dev)}'\n'{ceil(dev)}'\n'{round(dev)}'")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(25)
#num1 = int(input("enter num1:"))
#num2 = int(input("enter num2:"))
#if num1 == num2:
#    print("YES")
#else:
#    print("NO Y EALLA")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(26)
#num1 = input("enter num1:")
#num2 = input("enter num2:")
#print(f"{max(num1)}\n{min(num2)}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(27)
#def multi(x, y, z, w):
#    b = int(x*y*z*w)
#    a = str(b)
#    return (a[-2:])
#print(multi(3, 9, 9, 9))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(28)another solving of (27)
#def multi(x, y, z, w):
#    b = int(x*y*z*w)
 #   return (b % 100)
#print(multi(3, 9, 9, 9))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(29)>>to print A\NAB\NABC\NABCD\NABCDE
#n = int(input("enter num of your char:"))
#for i in range(65, n+65):
#    for j in range(65, i+1):
#        print(chr(j), end="")
#    print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(30)
#for i in range(1, 6):
#    for j in range(65, 65+i):
#        print(chr(j), end="")
#    print()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(31)
#def multi(q,e,f,r,t,x, y, z, w):
#    print(f"1.{q,e,f,r,t,x, y, z, w}")
#    a=(q*2,e*2,f*2,r*2,t*2,x*2, y*2, z*2, w*2)
#    b=(q*3,e*3,f*3,r*3,t*3,x*3, y*3, z*3, w*3)
#    c=(q*4,e*4,f*4,r*4,t*4,x*4, y*4, z*4, w*4)
#    d=(q*5,e*5,f*5,r*5,t*5,x*5, y*5, z*5, w*5)
#    print(f"2.{a}\n3.{b}\n4.{c}\n5.{d}")  
#multi(1,2,3,4,5,6,7,8,9)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(32)..
#import string
#while True:
# a=string.ascii_uppercase
# enter=input("enter char or digits:")
# if enter.isalpha() and enter in a:
#    print("ALPHA\nIS CAPITAL")
# elif enter.isdigit():
#    print("IS DIGIT")
# else:
#    print("ALPHA\nIS SMALL")
# #ask=input("do you want continue:")
# if ask=="n":
#    print("thank you")
#    break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>>.(33)
#import string
#while True:
# b=string.ascii_uppercase
 #char=str(input("entre char:".upper()).strip())
# if char in b:
 #   print(char.lower())
 #else:
#    print(char.upper())
 #ask=input("do you want to repeat this process:")
# if ask=="n":
 #   print("thanks")
#    break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(34)
#char = str(input("entre string:"))
#pal = ""
#for i in char:
#    pal = pal+i
#print(pal[::-1])
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#word = input("enter char:")
#pal = ""
#for char in range(len(word)-1, -1, -1):
#    pal = pal+word[char]
#print(pal)
#word_list = []
#for char in range(len(word)):
#    word_list.append(word[char])
#word_list.reverse()
#print(word_list)
#if pal == word:
#    print("is plaind room")
#else:
#    print("not a plind room")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#list = []
#Char = str(input("enter string:"))
#pal = ""
#print(Char[::-1])
#for i in Char:
#    list.append(i)
#print(list[::-1])
#if pal == Char:
#    print("tha word that you have entered is a palindrome  ")
#else:
#    print("tha word that you have entered is  not a palindrome")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(35)
#num=str(input("enter num :"))
#n=""
#for i in range(len(num)):
# #   n=n+str(i)
#    print(n)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>(36)
#import string
#num=["a","b","c","d","e"]
#n=""
#for i in num:
# #   n=n+i
# #   print(n)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(37)
#import string
#num=string.ascii_lowercase
#n=""
#for i in num:
#    n=n+i
#    print(n)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(40)
#import string
#num=string.ascii_lowercase
#n=""
#for i in num:
#    n=n+i
#    print(n)
#    if i=="e":
#        break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(41)
#num=int(input("enter num :"))
#n=""
#for i in range(num):
#   n=n+str(i)
#   print(n)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(42)
#num=str(input("enter num:"))
#n=""
#for i in num:
#   n=n+i
#   print(n)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.(43) using real char.
#import string
#a = string.digits
#n = ""
#for i in a:
#    n = n+str(i)
#    print(n)
#    if i == "":
# #       break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.another solution for numbers...(44)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#discount = int(input("enter dis:"))
#sale = int(input("enter sale:"))
#calc1 = 1-(discount/100)
#calc2 = sale/calc1
#print(f"{calc2:.2f}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(winter sale)(45)
#>>>>>>>>>>>>>>>>>>>>>>>.
# def calc(a,b,c):
#    if  a%c==0 and b%c==0 :
#        return("BOTH")
#    elif a%c==0 and b%c==1:
#        return("MEMO")
#    elif a % c == 1 and b % c == 0:
#        return("MOMO")
#    else:
#        return("no one")
# print(calc(23,23,2))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(memo and momo codeforces)(46)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>..
#x = input("enter char:")
#if x == "z":
#    print("a")
#else:
# x = chr(ord(x)+1)
# print(x)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(next alpha bet)(47)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def calc(a, b, c, d):
#    if a+b*c == d:
#        return ("YES")
#    elif a-b+c == d:
#        return ("YES")
#    else:
#        return ("NO")
#print(calc(2, 2, 1, 1))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(Ali Baba and Puzzles)(48)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......
#p = int(input("enter num 1:"))
#c = int(input("enter num 2:"))
#def calc(p, c):
# n = 0
# for i in range(p, c+1):
#     n = n+i
#     if n > 0:
#        return ("YES")
# else:
#     return ("NO")
#print(calc(p, c))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(E. Interval Sweep)(49)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#import string
#a=string.ascii_lowercase
#char=str(input("enter char:"))
#n=""
#if char not in a:
# print("please enter char from A >> Z: ")     
#e#lse:
# for i in a:
#    n=n+i
#    print(n)
 #   if i == char:
#        break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.(50)
#>>>>>>>>>>>>>>>>>>>>.
#import string
#a = string.digits
#n = ""
#for i in a:
#    n = n+str(i)
#    print(n)
#    if i == "":
# #       break
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.another solution for numbers...(51)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#discount = int(input("enter dis:"))
#sale = int(input("enter sale:"))
#calc1 = 1-(discount/100)
#calc2 = sale/calc1
#print(f"{calc2:.2f}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(winter sale)(52)
#>>>>>>>>>>>>>>>>>>>>>>>.
# def calc(a,b,c):
#    if  a%c==0 and b%c==0 :
#        return("BOTH")
#    elif a%c==0 and b%c==1:
#        return("MEMO")
#    elif a % c == 1 and b % c == 0:
#        return("MOMO")
#    else:
#        return("no one")
# print(calc(23,23,2))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(memo and momo codeforces)(53)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>..
#x = input("enter char:")
#if x == "z":
#    print("a")
#else:
# x = chr(ord(x)+1)
# print(x)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(next alpha bet)(54)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def calc(a, b, c, d):
#    if a+b*c == d:
#        return ("YES")
#    elif a-b+c == d:
#        return ("YES")
#    else:
#        return ("NO")
#print(calc(2, 2, 1, 1))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(Ali Baba and Puzzles)(55)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......
#p = int(input("enter num 1:"))
#c = int(input("enter num 2:"))
#def calc(p, c):
# n = 0
# for i in range(p, c+1):
#     n = n+i
#     if n > 0:
#        return ("YES")
# else:
#     return ("NO")
#print(calc(p, c))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(E. Interval Sweep)(56)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#a = input("YES")
#if int(a[1]) % int(a[0]) == 0:
#    print("YES")
#elif int(a[0]) % int(a[1]) == 0:
#    print("YES")
#else:
#    print("NO")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(LUCKY NUM)(57)
#n=int(input("int"))
#k=int(input("long long"))
#a#=int(input())
#def calc(n,k,a):
#    c=n*k/a
# #   if c in range(1,10):
 #       return("int")
#    elif c>2147483647:
#        return("long long")
#    elif c not in range(1,10):
 #       return("double")
#print(calc(n,k,a))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...(ginus)(58)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
#x=int(input())
#if x<0:
#    print("-1")
#elif x==0:
#    print("-1")
#elif x==1:
#    print("-1")
#f#or i in range(1,x+1):
#    if i%2==0:
#        print(i) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(even num)(59)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
#y = int(input())
#even = 0
#odd = 0
#pos = 0
#neg = 0
#for i in range(y):
#    x = eval(input())
#    if x > 0:
#        pos += 1
#    elif x < 0:
#        neg += 1
#    if x % 2 == 0:
#        even += 1
#    else:
#        odd += 1
#print("Even:", even)
#print("Odd:", odd)
#print("Positive:", pos)
#print("Negative:", neg)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(C. Even, Odd, Positive and Negative)(60)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#trais = int(input())
#password = int(input())
#while password != 1999:
#    trais -= 1
#    print("Wrong")
#    password = int(input())
#    if trais == 0:
# #       break
#else:
#    print("Correct")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(D. Fixed Password)(61)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#list = []
#y = int(input())
#for i in range(y):
 #  x = int(input())
#   list.append(x)
#print(list)
#print(max(list))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(max)(62)
#>>>>>>>>>>>>>>>>>>>>>.
#x=int(input())
#for i in range(1,13):
#    n=x * i
#    print(f"{ x } * {i * 1} = {n}")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..(F. Multiplication table)(63)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#while True:
 #N=eval(input())
 #if N==2:
 #  break
 #n=1
 #for i in range(1,N+1):
 #   n=n*i
 #print(f'{n}')
 #break
 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(64)(G. Factorial)
 #>>>>>>>>>>>>>>>>>>>>...
#from cmath import sqrt
# def second_degree(a,b,c,x):
#    if x>1:
#        print("should x ==1 ")
#
#    else:
#        v=(b**2)-(4*a*c)
#        d=(-b-sqrt(v))/(2*a)
#        x =(-b+sqrt(v))/(2*a)
#        print(f"the first solution is '{x}'\nthe second solution is '{d}'")
# second_degree(5,5,6,1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(65)(second degree equation)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def total_overs(balls):
##   calc = divmod(balls, 6)
 #  return calc
##print(total_overs(5))
#print(15 % 6)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.(66)(Cricket Balls to Overs!)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def int_to_str(num1):
#    x = str(num1)
#    return (f'"{x}"')
#def str_to_int(num2):
#    b = int(num2)
#    return (b)
#print(int_to_str(29848))
#print(str_to_int("7"))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(67)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def format_date(data):
#    print(f'"{data[-4:]}{data[-7:-5]}{data[-10:-8]}"')
#format_date("12/31/2019")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(68)(Date Format)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def top_note(dictionary):
#  top_note = max(dictionary['notes'])
#  return {"name": dictionary['name'], "top_note": top_note}
#print(top_note({"name": "Max", "notes": [1, 4, 6]}))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(69)(Get Students with Names and Top Notes)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#from curses.ascii import isalpha
#import string
#a=string.ascii_lowercase
#char=str(input("enter char:"))
#for ch in a:
#    if ch ==char:
#        x=chr(ord(ch)+1)
#        print(x)
 #       break#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.(70)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#while True:
 #import string
 #all_char=string.ascii_lowercase
 #space=""
 #choose=str(input("entre char :"))
 #for char in all_char:
 #   space=space+char
 #   print(space)
 #   if char==choose:
  #      break
 #ask=input("do you want go on: ") 
 #if ask=="y":
 #    continue
 #else:
 #    break  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.(71)
#mail=str(input("enter meil:"))
#password=input("enter your pass:")
#print("#"*50)
#for i in mail:
#    if i.isalpha():
 #       print(i.replace(i,"*"),end="")
  #  elif i.isdigit():
  #      print(i,end="")
 #   else:
 #       print(i,end="")
#print(" =>your mail")
#for i in password:
 #   print(i.replace(i,"*"),end="")
#print(" =>your password")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>(72)(password script)
