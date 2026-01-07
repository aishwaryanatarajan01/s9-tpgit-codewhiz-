a=input("enter password")
if(len(a)<8):
    print("Password Strength:Weak")
elif((len(a>=8) and a.isalpha() and a.isdigit() and a.isupper() and a.islower()) :
    print("Password Strength:medium")
else:
    print("password Strength:strong") 
