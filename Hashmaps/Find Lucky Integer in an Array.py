class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m={}
        for i in range(len(arr)):
               if arr[i] not in m:
                    m[arr[i]]=1
               else:
                    m[arr[i]]+=1
        maxi=-1
        maxiv=-1
        for i in m:
            if m[i]==i:
                 if m[i]>maxi:
                     maxi=m[i]
                     maxiv=i
        return maxiv
        