a=int(input("enter the number of items bought:"))
y=0
for i in range(0,a):
     b=input("enter itemname:")
     c=float(input("enter quantity:"))
     d=float(input("enter price:"))
     e=c*d
     print(b,"%d X %d = %d"%(c,d,e))
     y+=e
print("------------------------")
print("total amount:",y)
u=float(input("discount:"))
g=y-u
print("final amount:",g)



