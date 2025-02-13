import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations=0

        while(nums[0]<k):
              min_v=heapq.heappop(nums)
              max_v=heapq.heappop(nums)
              new=(min_v*2)+max_v
              heapq.heappush(nums,new)
              operations+=1
        return operations



        