class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1={}
        m2={}
        m3={}
        res=[[],[]]
        m4={}
        print(res)
        for i in range(len(nums1)):
            if nums1[i] not in m1:
                m1[nums1[i]]=1
        for i in range(len(nums2)):
          if nums2[i] not in m2:
                m2[nums2[i]]=1
        for v in m1:
            if v in m2:
                m3[v]=1
        for i in range(len(nums1)):
            if nums1[i] not in m3:
                if nums1[i] not in m4:
                 res[0].append(nums1[i])
                 m4[nums1[i]]=1
        for i in range(len(nums2)):
          if nums2[i] not in m3:
                 if nums2[i] not in m4:
                  res[1].append(nums2[i])
                  m4[nums2[i]]=1
        return res
        
        