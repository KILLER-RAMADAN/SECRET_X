# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("C:\\Users\\ahmed\\hello world\\ahmed.txt", "r")


print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

print(myFile.read())
print(myFile.read(5))

print(myFile.readline(5))
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

  print(line)

  if line.startswith("01-"):

    break

# Close The File

myFile.close()


def main():
    days = int(input("enter num of days:"))
    create_line = open("sama.txt", "w")
    for i in range(1, days+1):
        name = str(input("enter the employee name:"))
        sales = float(input(f" enter salary for {name}:"))
        id = input(f"enter {name} id:")
        create_line.write(name+"\n")
        create_line.write("salary is:\n")
        create_line.write((str(sales)+"\n"))
        create_line.write("the id is:\n")
        create_line.write((str(id)+"\n"))
    create_line.close()


main()

# name1 = input('Friend  # 1: ')
# name2=input('Friend #2: ')
#myfile=open('sama.txt', 'w')
#myfile.write(name1 + '\n')
#myfile.write(name2 + '\n')
# myfile.close()
