"""

calcuate sum of positive numbers till n , enterd by user

exit if user enter any negative number or zero
"""

n = int(input("Enter positive number for or 0 for exit: "))

sum = 0 
while n != 0 :
    sum += n     
    n = int(input("Enter positive number for dum or <=0 for exit: "))
print(sum)
