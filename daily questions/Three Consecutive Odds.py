class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        c=0
        for i in range(0,len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                  c=1
                  break
        if c==1:
            return True
        else:
            return False

        