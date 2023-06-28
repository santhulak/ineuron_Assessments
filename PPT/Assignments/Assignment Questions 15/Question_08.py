'''Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

!https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```'''
def trap(height):
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                water += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1

    return water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  

height = [4, 2, 0, 3, 2, 5]
print(trap(height))  
