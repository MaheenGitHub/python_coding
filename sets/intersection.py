set1 = {1,2,3,4,5}
set2 = { 4,5,6,7,8}

print("interxetion: ", set1.intersection(set2))

print("intersction by operatr: ", set1 & set2) 
# both operand should be set

print("intersction update")
set1.intersection_update(set2)
print("set1 updated : " , set1)