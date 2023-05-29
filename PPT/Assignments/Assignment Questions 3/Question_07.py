'''You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]'''

def findMissingRanges(nums, lower, upper):
    missing_ranges = []
    prev = lower - 1
    
    for num in nums + [upper + 1]:
        if prev + 1 <= num - 1:
            missing_ranges.append(getRange(prev + 1, num - 1))
        prev = num
    
    return missing_ranges

def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

# Test the function
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)
