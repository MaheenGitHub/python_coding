"""
program to print 1 to n numbers but if 
divisbe by 3 -> fizz
divisible by 5 -> buzz
by both 3 and 5 -> fizz buzz
"""

num = int(input(("Enter a number: ")))

for i in range(1,num+1) :
    if (i % 3 == 0 and i % 5 ==0):
        print("Fizz Buzz")
    elif( i % 3 == 0) :
        print("Fizz")
    elif (i % 5 == 0 ) :
        print("Buzz")
    else : 
        print(i)