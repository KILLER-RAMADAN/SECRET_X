sample = input("enter char and symbols:")
char = 0
symbols = 0
num = 0
for i in sample:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        num += 1
    else:
        symbols += 1
print(f"your character is {char}\nyour symbols is {symbols}\nyour num is {num} ")

string = str(input("enter string:"))
sum = 0
for i in string:
    if i.isdigit():
        sum = sum+int(i)
    else:
        print(i, end="_")
print(sum, end="")
