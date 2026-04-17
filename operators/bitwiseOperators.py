#bitwise -> bits -> binary

"""
&   (bitwise and)
|   (bitwise or)
^   (XOR)
~   (complemet / not)
<<  (left shift)
>>  (right shift)
"""

print("bitwise AND &")
a = 5            # 0101
b = 4            # 0100
print (a & b)    # 0100 -> 4 (only 1 & 1 is 1 )

print("bitwise OR |")
print (a | b)     # 0101 -> 5

print("bitwise XOR ^ ")
print(a ^ b)      #0001 -> 1 (one when both different )

print("bitwise negation ~ ")
print(~(a))       # -6  -> -ve sign (a+1) 

""" important: we can  not store negative members in memory directly. instead we use two's complement"""

#2's complemet = 1's complement (simpley reversing the bits ) + 1

"""
negation of 5 
0101 -> negation -> 1010

but ~5 = -6
HOW?????

-6 -> -ve number cant be directly stored in memory -> 2's completmwnt

6 -> 0110 -> 1's complement -> 1001 -> +1 -> 1010 == negation of 5
"""

print("left shift <<")
print(a << 2)   # 20 ( x<<n = a*2**n) where n =2 here 

"""
leftshift a by 2 bits (5 -> 0101 -> << -> 0101"00" -> added 2 zeros in the end)
no bits discarded, no bits lost , BITS GAINED
"""

print("right shift >> ")
print(a >> 2)      # 1 (x >> n = x/2**n)
"""
(5 -> 0101 -> "00"01  )
bits are dscarded / lost
"""