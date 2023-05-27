'''
💡 You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

'''
def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1
    missing = -1

    # Find the duplicate number
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    # Find the missing number
    for num in range(1, n + 1):
        if num not in num_set:
            missing = num
            break

    return [duplicate, missing]

# Test the function
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
