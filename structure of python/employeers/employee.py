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



    def  calculate_age(self):
      return employee.now-self.birthday
    
    
    def get_name(self):
      return self.__name
    
    def calculate_gpa(self):
      if self.gpa==0:
        print("false")
      elif self.gpa>0:
        print("true")
        
      

# def bouns(self):
# if self.age==60:
#    self.sallary=+500
#     print("your salary is increased>>"+ str(self.sallary+500))
# else:
#     print("no increased salary "+ str(self.sallary+500))
