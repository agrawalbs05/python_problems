# Meeting Rooms
# Tags : N252, Blind75, Intervals(Room), Easy

def can_attend_all_meetings(intervals):
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlap between consecutive meetings
    for i in range(1, len(intervals)):
        # If the current meeting starts before the previous one ends, return False
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(can_attend_all_meetings(intervals))  # Output: False

