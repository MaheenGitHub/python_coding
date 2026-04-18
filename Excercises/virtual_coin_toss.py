import random

"""
0 -> tail
1 -> head
"""

toss = random.randint(0,1)

if (toss ==1) :
    print("Head")
else :
    print("Tail")