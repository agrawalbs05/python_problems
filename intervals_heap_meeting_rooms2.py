# Meeting Rooms 2: find the minimum number of days required to schedule all meetings without any conflicts
# Tags: N253, Blind75, Bit manipulation, Heap, Medium

# nums = [3,0,1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]

def minMeetingRooms(self, intervals: List[Interval]) -> int:
    intervals.sort(key=lambda x: x.start)
    min_heap = []

    for interval in intervals:
        if min_heap and min_heap[0] <= interval.start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, interval.end)

    return len(min_heap)

intervals = [(0,40),(5,10),(15,20)]
Output: 2
#Explanation:
#day1: (0,40)
#day2: (5,10),(15,20)