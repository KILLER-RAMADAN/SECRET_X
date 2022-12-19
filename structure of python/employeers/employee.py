class employee:
    now=2022
    def __init__(self, name, age, section, is_manager, is_new, country, rating,salary,birthday,gpa,id):
        self.name = name
        self.age = age
        self.section = section
        self.is_manager = is_manager
        self.is_new = is_new
        self.country = country
        self.rating = rating
        self.salary = salary
        self.birthday=birthday
        self.gpa=gpa
        self.id=id



  
    
    
    def get_name(self):
      print(self.name)
    
    def calculate_gpa(self):
      if self.gpa==0:
        print("false")
      elif self.gpa>0:
        print("true")
    def bouns(self):
     if self.age==60:
       self.salary=self.salary+500
       print(self.salary)
      
      
     else:
      print("no increased salary your salary is "+ str(self.salary))
        

em=employee("ahmed",6,"m110",True,False,"egypt",10,20000,2003,3,21510857)
em.get_name()

em.bouns()

# def bouns(self):
# if self.age==60:
#    self.sallary=+500
#     print("your salary is increased>>"+ str(self.sallary+500))
# else:
#     print("no increased salary "+ str(self.sallary+500))


class student:
    energy = 100

    def eat_apple(self):
        self.energy += 10


player1 = student()
player1.eat_apple()
print(player1.energy)
