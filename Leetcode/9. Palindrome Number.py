"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

"""

x = 121
s = str(x)

print("My approach using slicing")
rev = s[::-1]
print(rev)
if (s == rev) :
    print(True)
else :
    print(False) 

print("Reverse the number approach")
original = x
reverse = 0 
while x > 0 :
    last_digit = x % 10
    reverse = reverse * 10 + last_digit
    x //= 10

print(reverse)
if (original == reverse ) :
    print(True)
else :
    print(False)

print("Half reverse optimized approach")
half = 0
last_digit = 0
if (x<0) or ( original % 10 == 0 and original != 0 ):
    print(False)
while original > half :
    last_digit = original % 10
    half = half * 10 + last_digit
    original //= 10

print(original)
print(half)
if(original == half or original == half//10) :
    print(True)
else :
    print(False)



"""
problem i submitted on leetcode

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reverse = original[::-1]
        if (original == reverse ):
            return True
        else :
            return False

"""