"""
calcualte average height  from list of heights

constraints :-
user input
no built in functons like sum() , len()
output should be a whoule number (round)

use range (5) -> 0,1,2,3,4
"""

heights =input("enter heights seperaed by comma: ")
height = heights.split(',')

total = 0
count = 0
for i in height :
    total += int(i)
    count += 1

avg_height = total/count
print("average height is: " , round(avg_height))
