from employee import employee
ans = "y"
while ans == "y":
    e1 = employee("ahmed", 22, "elzero", True, False,
                  "egypt", 10, 1500, 1999, 0, 23779940)
    e2 = employee("islam", 24, "igec", False, False,
                  "sudan", 9.0, 500, 1979, 0, 83373374)
    e3 = employee("mahmoud", 19, "igec", False, False,
                  "usa", 8.0, 600, 1988, 0, 36377525)
    string = str(input("enter employee name :"))
    if string == "e1":
        print(f"employee name : {e1.name}, age: {e1.age}, is manager: {e1.is_manager}, working in: {e1.section}, is new employee :{e1.is_new}, country is:{e1.country}, rating is: {e1.rating}, salary is {e1.salary}, your birthday is: {e1.calculate_age()} your gpa is {e1.calculate_gpa()} your id is {e1.id} ")
    elif string == "e2":
        print(f"employee name : {e2.name}, age: {e2.age}, is manager: {e2.is_manager}, working in: {e2.section}, is new employee :{e2.is_new}, country is:{e2.country}, rating is: {e2.rating},salary is {e2.salary}, your birthday is: {e2.calculate_age()} your gpa is {e2.calculate_gpa()} your id is {e2.id}  ")
    elif string == "e3":
        print(f"employee name : {e3.name}, age: {e3.age}, is manager: {e3.is_manager}, working in: {e3.section}, is new employee :{e3.is_new}, country is:{e3.country}, rating is: {e3.rating},salary is {e3.salary}, your birthday is: {e3.calculate_age()} your gpa is {e3.calculate_gpa()} your id is {e3.id} ")
    ans = input("do you want to again this process you can press (y or n): ")
    if ans == "n":
        print("THANKS MAN..")
print(e1.calculate_gpa())
