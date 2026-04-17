print(len("maheen fatima"))
# print(len(12345)) -> TYPE ERROR -> len() is only for strings

name = "maheen fatima"
#print("u name has " + len(name) + "characters") -> str+int is error
print("ur name has " + str(len(name)) + " characters") 

print("checking types ....")
print(type(len(name)))
print((type(str(len(name)))))

"""
other conversions
int()
str()
float()
"""

print(10+10)
print("10" + "10")
print(int("10") + int("10"))
print(10 + float("10"))

#print(10 + int(name))  ValueError