"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""
haystack = "mississippi"
needle = "issip"

left = 0 

for right in range (len(haystack)) :
    if haystack[right]  == needle[left] :
        left += 1

    else :
        left = 0 

    if (left == len(needle)) :
            break    
             

first_occurence  = -1

if (left != 0) :
    first_occurence = right - len(needle) + 1

print(first_occurence)

    
print("below is wrong bzx Python ka loop manually peeche nahi jata jaise C++ ya Java mein jata hai.")
l = 0
desired = []
bool = False

for right in range(len(haystack)) :

    if(desired == needle) :
        bool = True
        print(l-right)
    if l < len(needle) :
        if (haystack[right] == needle[l]) :
            desired.append(needle[l])
            l += 1
            print(desired)
        else :
            l = 0
            if right != 0 : 
                right -= 1
                
            desired.clear()

if (bool == False) :
    print("-1")

        
print("sliding window technique")
bool = False

if len(needle ) <= len(haystack) :

    for i in range (len(haystack)):
        if haystack[i : i + len(needle)] == needle :
            bool = True
            print(i)
    
if bool == False :
    print("-1")