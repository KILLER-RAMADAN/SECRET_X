# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

ans = "y"
while ans == "y":
   age = int(input("Please Write Your Age?").strip())

   unit = input(
       "Please Choose Time Unit: Months, Weeks, Days, hours, scoends, minutes (m/w/d/h/s/i) :").strip().lower()
   months = age * 12
   weeks = months * 4
   days = age * 365
   hours = days*24
   minutes = hours * 60
   scoends = minutes*60

   if unit == 'months' or unit == 'm':

    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months.")

   elif unit == 'weeks' or unit == 'w':

    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks.")

   elif unit == 'days' or unit == 'd':

    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} Days.")

   elif unit == "hours" or unit == 'h':

    print("You Choosed The Unit hours")
    print(f"You Lived For {hours:,} hours.")

   elif unit == 'scoends' or unit == 's':

    print("You Choosed The Unit scoends")
    print(f"You Lived For {scoends:,} scoends.")

   elif unit == 'minutes' or unit == 'i':

    print("You Choosed The Unit minutes")
    print(f"You Lived For {minutes:,} minutes.")

   else:
       print("please choose any of this (m/w/d/h/s/i) : ")
       continue
   ans = input(
       "do you want to again this process you can press (y or n): ".strip().upper())
   if ans == "n":
     print("THANKS FOR USING OUR PROGRAM: ")
