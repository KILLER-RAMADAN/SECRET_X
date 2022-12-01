print("*" * 50)
print("please use only numbers!!")
print("*" * 50)

unit=input("please choose gpa unit: distinction ,firstclass ,secondclass ,pass, fail >>(d,f,s,p,a)")
percentage = float(input("please enter your persentage:"))
if percentage >=90 or unit=="d":
    print("distinction")
elif percentage >= 80 or  unit=="f":
    print("first class")
elif percentage >= 70 or  unit=="s":
    print("second class")
elif percentage >= 60 or  unit=="p":
    print("pass")
elif percentage <= 60 or  unit=="a":
    print("fail")
else:
 print("please dont use this program if your gpa less then '60' ")
