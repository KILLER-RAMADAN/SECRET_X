# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

from unittest import skipIf


print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)

def say_hello(*peoples):  # n1, n2, n3, n4

  for name in peoples:

    print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

def show_details(*skills):

  print(f" Hello  ahmed Your Skills Is: ")

  for skill in skills:
    print(skill)

show_details( "Html", "CSS", "JS")
show_details( "Html", "CSS", "JS", "Python", "PHP", "MySQL","php")