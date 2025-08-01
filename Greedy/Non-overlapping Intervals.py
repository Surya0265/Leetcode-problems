class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1] )
        end_time=intervals[0][1]
        res=0
        for start,end in intervals[1:]:
            if start>=end_time:
                end_time=end
            else:
                res+=1
        return res
        