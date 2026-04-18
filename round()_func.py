# round (number , no. of digits)
# no. of digits upto wch u want to round off the number -> optional ->by default 0

print("rounding int")
print(round(7))     #returns int
print(round(7,2))   #returns int
print("no effect on int when no. of digis to round of ie either zero or +ve")
print(round(674,2)) 

print("when no.of digit is -ve ")
print(round(674,-1)) # last digit is zeor and second last mn lus one if >5  (closest multiple of 10)
print(round(674,-2)) # last 2 digits zero -> plus oe in thir last if > 5 (closest multipl of 100)
print(round(674,-3)) # 0674 -> '0'674 -> '0'000 -> '1'000 (closest multiple of 1000)

print("rounding float")
print(round(2.666666, 2))

print("int or float return")
print(round(2.666666))    
print(type(round(2.666666))   )     #returns int
print(round(2.66666,0))     #returns float
print(type(round(2.666666 , 0))   )
print("nearest even digit in case of 0.5 -> tie breaking")
print(round(7.5))
print(round(6.5))

print("rounding negatives")
print(round(-1.5))

print("decimal number and negative no. of digits to be round off")
print(round(674.1012 , -1))
