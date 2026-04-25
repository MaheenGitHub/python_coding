"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]

"""
s = "MCMXCIV"

print("My Approach ")
l = list(s)
print(type(l))
print(l)
num = 0 

for i in range(len(l) ) :
    if (l[i] == 'I') :
        num += 1

    if (l[i] == 'V') :
        num += 5
        if(l[i-1] == 'I' and i != 0 ):
            num -= 2

    if (l[i] == 'X') :
        num += 10
        if(l[i-1] == 'I' and i != 0  ):
            num -= 2

    if (l[i] == 'L') :
        num += 50
        if(l[i-1] == 'X' and i != 0  ):
            num -= 20

    if (l[i] == 'C') :
        num += 100
        if(l[i-1] == 'X' and i != 0 ):
            num -= 20

    if (l[i] == 'D') :
        num += 500
        if(l[i-1] == 'C' and i != 0  ):
            num -= 200

    if (l[i] == 'M' ) :
        num += 1000
        if(l[i-1] == 'C'and i != 0 ):
            num -= 200

print(num)

print("Hash map dictionary approach")
roman = {
    'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000
}

total = 0

for i in range(len(s)) :
    if (i+1 < len(s) and roman[s[i]] < roman[s[i+1]]) :
        total -= roman[s[i]]
    else :
        total += roman[s[i]]
print(total)


"""


code i submitted on leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        num = 0

        for i in range(len(l)):
            if l[i] == "I":
                num += 1

            if l[i] == "V":
                num += 5
                if l[i - 1] == "I" and i != 0 :
                    num -= 2

            if l[i] == "X" :
                num += 10
                if l[i - 1] == "I" and i != 0 :
                    num -= 2

            if l[i] == "L":
                num += 50
                if l[i - 1] == "X" and i != 0  :
                    num -= 20

            if l[i] == "C":
                num += 100
                if l[i - 1] == "X" and i != 0 :
                    num -= 20

            if l[i] == "D":
                num += 500
                if l[i - 1] == "C" and i != 0 :
                    num -= 200

            if l[i] == "M":
                num += 1000
                if l[i - 1] == "C" and i != 0  :
                    num -= 200
        return(num)
        
    """