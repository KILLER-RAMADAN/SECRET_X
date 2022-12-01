# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("C:\\Users\\ahmed\\hello world\\ahmed.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open("C:\\Users\\ahmed\\hello world\\New folder\\funny.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n", "gamed\n"]

myFile = open("C:\\Users\\ahmed\\hello world\\New folder\\funny.txt", "w")
myFile.writelines(myList)

myFile = open("C:\\Users\\ahmed\\hello world\\New folder\\funny.txt", "a")
myFile.write("ahmed ramadan\n")

myFile = open("C:\\Users\\ahmed\\hello world\\New folder\\funny.txt", "a")
myFile.write("mahmoud ramadan\n")

myFile = open("C:\\Users\\ahmed\\hello world\\New folder\\funny.txt", "w")

myFile.write("ahmed ramadan\n"*2000)

# open the file
text_file = open('C:\\Users\\ahmed\\hello world\\ahmed.txt', 'w')

# initialize an empty list
word_list = []
num = eval(input("enter num:"))
# iterate 4 times
for i in range(num):
    print(f"Please enter data >>> your try {i} ")
    line = input()  # take input
    word_list.append(line)  # append to the list
print(word_list)

text_file.writelines(word_list)  # write 4 words to the file

text_file.close()  # don’t forget to close the file
