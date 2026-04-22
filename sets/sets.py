my_set = {"curly" , 2 , 2 , 4.5 , True}
print("unodered set: " , my_set)

print("no indexing , no slicing ")
# print(my_set[2])   # Error

print("immutable")
# my_set[2] = 3      # Error

dup_set = {1, True, 1}
print("True is 1 and False is 0 so: " , dup_set)

empy_set = {}
print("datatype of an empty set {} is: " , type(empy_set) )

empty = set()
print("dattype when using set() function: ", type(empty) )
