"""
input from user
dont use max()
use split and range

"""
num = input("Enter numbers seperated by comma: ")

nums = num.split(',')

maximum = int(nums[0])

for i in nums :
    if ( int(i) > maximum ) :
        maximum = int(i)

print(f"maximum is: {maximum}")