
string = str(input("Enter String :").strip())
index = int(input("Enter Number :"))


def remove(string, index):
    for A in range(len(string)):
        if A == index:
            string = string.replace(string[index], "")
            return (string)
    if index < 0:
        print("Please Enter Positive Number")
        if string == "":
            # we use this condition to the user to do not leave it empty
            print(f"you shouldn't enter non empty string..  ")
        elif index > len(string):
            # we use this condition to print this message for user when he input bigger index than string
            print("out of range please enter index to remove from your string :")
    else:
        print(
            f"your string after removing the number:{remove(string,index).upper()}")
