def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """

    if not intervals:
        return 0
    
    start_timings = sorted([i[0] for i in intervals])
    end_timings = sorted([i[1] for i in intervals])
    used_rooms, start_ptr, end_ptr = 0, 0, 0

    while start_ptr < len(intervals):
        if(start_timings[start_ptr]>=end_timings[end_ptr]):
            used_rooms -= 1
            end_ptr += 1
        used_rooms += 1
        start_ptr += 1

    return used_rooms

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print(minMeetingRooms(intervals))