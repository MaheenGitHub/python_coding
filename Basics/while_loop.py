"""
no do-while loop in python

while condition/expression :
    stetemnt(s)
    terminating condition/SENTINEL VALUE

unlike for loop , we use while when we dont know how many times the lop will be executed

"""

print("print counting 1-5")
count = 0
while count <= 5 :
    print(count)
    count += 1

print("while with lists")
name = ["m" , "a" , "h"]
while name :
    print(name) 
    name.pop()

print

print("while ka else only when while successfully executed or condition becones false")
# else wont be executed when breaked while 
count = 1
while count <= 5 :
    if count == 3 :
        break        
    print(count)
    count += 1
else :
    print("ELSEE wont be executed")

count = 1 
while count < 1 :
    print(count)
    count += 1
else :
    print("in else block")

print("out from whille eLse bloack")

print("for menu etc")

n = int(input("Enter  num (-1 to quit)"))

while n != -1 :
    print(n)
    n = int(input("Enter  num (-1 to quit): "))

else :
    print("in else bloc after -1")