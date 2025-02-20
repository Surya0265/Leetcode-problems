class NumArray:

    def __init__(self, nums: List[int]):

      self.prefixnums=(len(nums)+1)*[0]
      for i in range(len(nums)):
         self.prefixnums[i+1]=self.prefixnums[i]+nums[i]


    def sumRange(self, left: int, right: int) -> int:
          return self.prefixnums[right+1]-self.prefixnums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)