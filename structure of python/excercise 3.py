ans = "y"
max = 1
num = int(input("enter num:"))
for int in range(max, num+1):
    n = eval(input(f"guess number '{int}' please enter your guess :"))
    if n < num:
        print("too low try again")
    elif n > num:
        print("too high try again")
    elif n == num:
        print("congratulations you won a fucken prize..")
    ans = input("want to again this process you can press (N to STOP or Y to continue..): ")
    if ans == "n":
        print("THANKS MAN FOR USING OUR FUCKING PROGRAM..")
        break
