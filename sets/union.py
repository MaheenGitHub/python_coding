set1 = {1,2,3,4,5}
set2 = { 4,5,6,7,8}


# (set1 U set2) - (set1 ^ set2) sematic diff

set1.union(set2)
set3 = set1 | set2

print("set1: ", set1)
print("set2: ",set2)
print("set3 is set1 | set2: ",set3)
print("set 1 U set 2: ", set1.union(set2) )

my_list = [44,55,66]
set1.union(my_list)
print("added list by union: " , set1.union(my_list)
)
set1.union(set2)
print("union update of two sets: ", set1)

# set4 = set1 | my_list     #ERROR bcz | must have set as operands, un like union


print("union update")
set1.update(my_list)
print("after udating: " , set1)

set1 |= set2
print(set1)