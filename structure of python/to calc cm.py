print("#"*50)
print("please enter only numbers:")
print("#"*50)
length = float(input("Enter the length in Centimeters: "))
if length < 0:
    print("Length should be positive!!")
else:
    inch = length / 2.54
    print(f"the 'length' is:{length} or 'inches' ={inch}")
    
    
    

