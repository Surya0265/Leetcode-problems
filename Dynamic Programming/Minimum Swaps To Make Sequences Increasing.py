class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep=[float('inf')]*len(nums1)
        swap=[float('inf')]*len(nums1)
        swap[0]=1
        keep[0]=0
        for i in range(1,len(nums1)):
            if nums1[i-1]<nums1[i] and nums2[i-1]<nums2[i]:
                keep[i]=keep[i-1]
                swap[i]=swap[i-1]+1
            if nums1[i-1]<nums2[i] and nums2[i-1]<nums1[i]:
                keep[i]=min(keep[i],swap[i-1])
                swap[i]=min(swap[i],keep[i-1]+1)
        return min(keep[-1],swap[-1])

        