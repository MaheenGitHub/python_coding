"""
three method of Removing Elements

1. remove() ->Removes the first occurrence of a specific value

2. pop() -> removes and returns the element at a given index

3. clear() -> Removes all elements from the list
"""


num = [1,2,3,4,5,3,6,3]
print(num)

num.remove(3)
#print(num.remove(3))   ERROR
print("remove(n) only first occurence is removed")
print(num)

print("pop() will remove and return the value of last idex")
print("removed value is " , num.pop())
print(num)


num.clear()
print("clear() the list")
print(num)
