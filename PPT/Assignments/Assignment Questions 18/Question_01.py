'''
💡 **Merge Intervals**

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

**Example 1:**
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

**Constraints:**

- `1 <= intervals.length <= 10000`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10000`
'''
def merge(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = []  # Result list to store merged intervals

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:  # Non-overlapping interval
            merged.append(interval)
        else:  # Overlapping interval, merge with the previous interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals)) 
 
intervals = [[1, 4], [4, 5]]
print(merge(intervals))  
