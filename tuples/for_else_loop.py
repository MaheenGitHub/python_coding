"""
totaly different from if else where only one block is executed (either if or else)

syntax

for var_name in sequnce :
    statement(s)
else :
    statement(s)


"""

print("else block will be executed only if for loop is completed succesfully")

nums = [0,1,2,3]
for i in nums :
    print(i)
else :
    print("all numbers printed successfully")

print("if for loop is breaked then esle wont be excuted")

for i in nums:
    print(i)
    if i == 2 :
        break
else :
    print("nope bcz break statement")

print("if for loop is continued then esle would be excuted")

for i in nums:
    print(i)
    if i == 2 :
        continue
else :
    print("yup bcz conitnue statement")