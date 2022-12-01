# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

mainPassword = "osama@123"

inputPassword = input("Write Your Password: ").lower()

while inputPassword != mainPassword:  # True

    tries -= 1  # tries = tries - 1

    print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

    inputPassword = input("Write Your Password: ")

    if tries == 0:

        print("All Tries Is Finished.")

        break
else:

    print("Correct Password")


####################################################################
# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

#tries = 4

#mainPassword = "ahmed@123"

#inputPassword = input("Write Your Password: ")

# while inputPassword != mainPassword:  # True

# tries -= 1  # tries = tries - 1

   # print(f"Wrong Password you 'have' {tries} 'chances' ")

   # inputPassword = input("Write Your Password: ")

    # if tries == 0:

    # print("All Tries Is Finished.")

    # break
# else:

   # print("Correct Password")


trais = 4
password = str(input("enter your password:"))
while password != "ahmed":
    trais -= 1
    print(f"you have {trais} chance")
    password = str(input("enter your password again:"))
    if trais == 0:
        print("please enter password again after 30 sec..")
        break
else:
    print("correct pass")
    print("thanks for remember your pass")
