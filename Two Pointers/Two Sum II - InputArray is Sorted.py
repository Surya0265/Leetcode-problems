class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        arr=[]
        right=len(numbers)-1
        while(left<right):
              if(numbers[left]+numbers[right]<target):
                left=left+1
              elif(numbers[left]+numbers[right]>target):
                right-=1
              else:
                arr.append(left+1)
                arr.append(right+1)
                break
        return arr
    
        