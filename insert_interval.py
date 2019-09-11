# author: YANG CUI
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    # find the stopping index since the intervals list is already sorted
    lastIndex = 0
    while lastIndex < len(intervals) and newInterval[1] >= intervals[lastIndex][0]:
        lastIndex += 1
    # return to the index where we need to last look at
    if lastIndex != 0:
        lastIndex -= 1
    # find the index we need to start looking closely at the intervals
    firstIndex = 0
    while firstIndex < len(intervals) and newInterval[0] > intervals[firstIndex][1]:
        firstIndex += 1
    if firstIndex == len(intervals):
        firstIndex -= 1
    # construct the new resulting union to be inserted
    if firstIndex == lastIndex:
        if firstIndex == 0 and len(intervals) == 1:
            if newInterval[0] > intervals[firstIndex][1]:
                intervalToInsert = [intervals[0], newInterval]
                return intervalToInsert
            elif newInterval[1] < intervals[firstIndex][0]:
                intervalToInsert = [newInterval, intervals[0]]
                return intervalToInsert
            elif newInterval[0] == intervals[firstIndex][1]:
                intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
            else:
                if newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                    intervalToInsert = [newInterval[0], intervals[lastIndex][1]]
                elif newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] <= newInterval[1]:
                    intervalToInsert = [newInterval[0], newInterval[1]]
                elif newInterval[0] >= intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                    intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
                else:
                    intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
        elif firstIndex == 0 and len(intervals) != 1:
            if newInterval[1] <= intervals[firstIndex][0]:
                intervalToInsert = newInterval
                lastIndex = -1
            elif newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                intervalToInsert = [newInterval[0], intervals[lastIndex][1]]
            elif newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] <= newInterval[1]:
                intervalToInsert = [newInterval[0], newInterval[1]]
            elif newInterval[0] >= intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
            else:
                intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
        elif lastIndex == len(intervals) - 1:
            if newInterval[0] > intervals[lastIndex][1]:
                intervalToInsert = newInterval
                firstIndex = len(intervals)
            else:
                if newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                    intervalToInsert = [newInterval[0], intervals[lastIndex][1]]
                elif newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] <= newInterval[1]:
                    intervalToInsert = [newInterval[0], newInterval[1]]
                elif newInterval[0] >= intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                    intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
                else:
                    intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
        else:
            if newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                intervalToInsert = [newInterval[0], intervals[lastIndex][1]]
            elif newInterval[0] < intervals[firstIndex][0] and intervals[lastIndex][1] <= newInterval[1]:
                intervalToInsert = [newInterval[0], newInterval[1]]
            elif newInterval[0] >= intervals[firstIndex][0] and intervals[lastIndex][1] > newInterval[1]:
                intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
            else:
                intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
    else:
        if intervals[firstIndex][0] >= newInterval[0] and intervals[lastIndex][1] <= newInterval[1]:
            intervalToInsert = newInterval
        else:
            if intervals[lastIndex][1] > newInterval[1] and newInterval[0] > intervals[firstIndex][0]:
                intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
            elif intervals[lastIndex][1] <= newInterval[1] and newInterval[0] > intervals[firstIndex][0]:
                intervalToInsert = [intervals[firstIndex][0], newInterval[1]]
            elif intervals[lastIndex][1] > newInterval[1] and newInterval[0] <= intervals[firstIndex][0]:
                intervalToInsert = [newInterval[0], intervals[lastIndex][1]]
            else:
                intervalToInsert = [intervals[firstIndex][0], intervals[lastIndex][1]]
    # copy elements that are unaffected as well as insert the above one
    resultIntervals = []
    for i in range(firstIndex):
        resultIntervals.append(intervals[i])
    resultIntervals.append(intervalToInsert)
    for j in range(lastIndex + 1, len(intervals)):
        resultIntervals.append(intervals[j])
    return resultIntervals
    # print(lastIndex)
    # print(firstIndex)
    # print(intervalToInsert)
    # print(resultIntervals)


# intervals = [[0,7],[8,8],[9,11]]
# newInterval = [4,13]
#
# print(insert(intervals, newInterval))
