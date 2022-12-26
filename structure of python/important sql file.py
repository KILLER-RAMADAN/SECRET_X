import sqlite3
database = sqlite3.connect("costumers.db")
print("Connected To Database Successfully")
cr = database.cursor()
cr.execute("create table moeny (user_id integer,name text,human_number integer)")
users_list = ["Ahmed", "Sayed", "Mahmoud", "Ali",
              "Kamel", "Ibrahim", "Enas", "eman", "hamada", "gamal"]
for key, user in enumerate(users_list):
   cr.execute(
       f"insert into moeny (user_id , name ,human_number)values({key+1},'{user}',{key+1})")
cr.execute("update moeny set user_id=4, name='Ali',human_number= 4 where user_id=4")
cr.execute("select * from moeny")
results = cr.fetchall()
for row in results:
    print(f"User_ID => {row[0]},", end=" ")
    print(f"Username => {row[1]}", end=" => ")
    print(f"human_number=>{row[2]}")
#  print(f"your databse has {len(results)} rows.")
database.commit()
database.close()
