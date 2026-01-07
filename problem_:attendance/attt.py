a=int(input("Total classes:"))
b=int(input("Classes Attended:"))
if a>0:
    c=(b/a)*100
    print("attendance percentage:",c,"%")
    if(c>=75):
        print("status eligible")
    else:
        print("Status:Noteligible")
        e=0.75*a
        z=e-b
        print("Additional classes required:",z)
else:
    print("invalid total class")