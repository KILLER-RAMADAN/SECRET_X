from turtle import distance
print("please use N/Y to continiue:")
z = " "
while z != "n":
  s = float(input("please enter speed:"))
  t = float(input("please enter time:"))
  distance = s*t
  if s >= 0 and t >= 0:
      print(distance)
  else:
      print("please use positive num:")
  z = input("do you want to countinue")
else:
 print("good bye")
