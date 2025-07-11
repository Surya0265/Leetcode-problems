class Solution:

    def __init__(self, w: List[int]):
        self.prefixsums=[]
        prefix=0
        for i in w:
            prefix+=i
            self.prefixsums.append(prefix)
        self.total=prefix


        

    def pickIndex(self) -> int:
        low=0
        high=len(self.prefixsums)-1
        target=random.randint(1,self.total)
        while(low<high):
            mid=(low+high)//2
            if self.prefixsums[mid]<target:
                low=mid+1
            else:
                high=mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()