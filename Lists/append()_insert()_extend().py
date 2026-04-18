"""
three ways to add in a list

1. append(element) -> add only one element at the end of the list

2. insert(index , element) -> insert one elemnt at any specific index

3. extend([list]) -> multiple items at the end

"""
num = [3,2,5,4]
print(num)

print("append 1 elemnt at last")
num.append(6)
#print(num.append(6)) # None -> no return type
print(num)

#Use append() if you want to add one item. If you append a list, it becomes a nested list: [1, 2, [3, 4]].
num.append([5,6,7])

print("insert 1 element at sp index" )
num.insert(2,7) # the existing 2nd index is right shifted and not discarded
print(num)

print("Extend mulitple elements (list) at the end")
num.extend([45,46,47])
print(num)