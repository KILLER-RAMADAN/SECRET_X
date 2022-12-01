# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"] # 0>>9 ,, 1>>10

# print(len(myF))  # List Length [10]

f = 0

while f < 10:  # f < 10

  print(f"#{str(f+1).zfill(2)} {myF[f]}") # zfill() function alwyas run with strings only.......

  f += 1  # f = f + 1

else:

  print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])