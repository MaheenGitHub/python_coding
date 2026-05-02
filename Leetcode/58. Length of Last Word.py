"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

s = "Hello my world "

print("My Approach")
length = len(s) - 1
last = []

while length <= len(s)-1 :
    if s[length] != " " :
        last.append(s[length])

    else :
        if len(last) != 0 :
           break

    if length == 0 :
        break
    else : 
        length -= 1

print(len(last))


print("python cheetcode using split()")
splitted = s.split()
print(splitted)
print(len(splitted[-1]))

"""
code i submittend on leetcode

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s) - 1
        last = []

        while length <= len(s)-1 :
            if (s[length] != " ") :
                last.append(s[length])
            
            else :
                if (len(last) != 0) :
                    return len(last)
            if length == 0 :
                return len(last)
            else :
                length -= 1
        
        return len(last)

"""