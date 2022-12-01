num1=int(input("enter first num :"))
opp=input("enter operation:")
num2=int(input("enter second num :"))
def max_num(num1,num2):
    if opp=="+":
        return num1+num2
    elif opp=="-":
        return num1-num2
    elif opp == "*":
        return num1*num2
    elif opp == "/":
        return num1/num2
print(max_num(num1,num2))