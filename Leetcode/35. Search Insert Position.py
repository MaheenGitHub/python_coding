"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""
nums = [1,3,5,6]
target = 2



print("My Approach")
for i in range(len(nums)) :
    if(nums[i] == target )  or nums[i] > target :
        print(i)
        break

    else :
        if i  == len(nums)-1 :
            print(i+1)

print("My modified logic")
bool = False
for i in range(len(nums)) :
    if nums[i] >= target :
        print(i)
        bool =True
        break
if bool == False :
    print(len(nums))

print("sorted -> binary search -> O(log n)")

low = 0
high = len(nums) - 1

while(low <= high ):
    mids = (low + high) // 2
    if nums[mids] == target :
        # return i
        print("return",i)
        break
    elif nums[mids] < target :
        low = mids + 1
    else :
        high = mids - 1
print(low)

print("python cheetcode using bisect left")
import bisect
print(bisect.bisect_left(nums, target))


"""
code i ubmitted on leetcode exactly

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)) :
            if nums[i] == target or nums[i] > target:
                return i
            
            else :
                if i == len(nums)-1 :
                    return i+1

"""