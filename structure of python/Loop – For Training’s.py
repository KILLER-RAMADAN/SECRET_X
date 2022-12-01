# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

myRange = range(0, 100)

for number in myRange:

  print(f"#{number+1}")

# Dictionary

mySkills = {
  "Html": "90%",
  "Css": "60%",
  "PHP": "70%",
  "JS": "80%",
  "Python": "90%",
  "MySQL": "60%"
}

print(mySkills['JS'])
print(mySkills.get("Python"))

for mainkays, mainvalue in mySkills.items():

  #print(skill)

  print(f"My Progress in Lang {mainkays} Is: {mainvalue}")