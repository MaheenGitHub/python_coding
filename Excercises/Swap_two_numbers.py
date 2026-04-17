a = input("Enter value of a ") # a= 1
b = input("Enter value of b ") # b= 2

a,b= b,a

print("a= " + a) # a= 2
print("b= " + b) # b= 1
#no type error becasue a,b variables are string as input() returns string

#using temp
print()
print("Temp variable logic")
temp = a 
a = b
b = temp 
print("a= " + a) # a= 1
print("b= " + b) # b= 2