class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            if len(nums1)>len(nums2):
                     nums1,nums2=nums2,nums1
            n=len(nums1)
            m=len(nums2)
            low=0
            high=n
            while(low<=high):
                  partitionA=(low+high)//2
                  partitionB=(n+m+1)//2-partitionA
                  if partitionA!=0:
                             maxleftA=nums1[partitionA-1]
                  else:
                      maxleftA=float('-inf')
                  if partitionA!=n:
                       minRightA=nums1[partitionA]
                  else:
                      minRightA=float('inf')
                  if partitionB!=0:
                             maxleftB=nums2[partitionB-1]
                  else:
                      maxleftB=float('-inf')
                  if partitionB!=m:
                       minRightB=nums2[partitionB]
                  else:
                      minRightB=float('inf')
                  if maxleftA<=minRightB and maxleftB<=minRightA:
                      if(n+m)%2==0:
                        return (max(maxleftA,maxleftB)+min(minRightA,minRightB))/2.0
                      else:
                        return max(maxleftA,maxleftB)
                  if maxleftA>minRightB:
                            high=partitionA-1
                  else:
                            low=partitionA+1