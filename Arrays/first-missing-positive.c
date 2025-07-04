int firstMissingPositive(int* nums, int numsSize) {
    for(int i=0;i<numsSize;i++){
        if(nums[i]<0){
            nums[i]=0;
        }
    }
    for(int i=0;i<numsSize;i++){
        int val=abs(nums[i]);
        if(1<=val&&val<=numsSize){
        
          if(nums[val-1]>0){
              nums[val-1]*=-1;
        }
        else if(nums[val-1]==0){
            nums[val-1]=-(numsSize+1);
        }
        }

    }
    for(int i=1;i<numsSize+1;i++){
        if(nums[i-1]>=0){
            return i;
        }
    }
    return numsSize+1;

    
}

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
          while 1<=nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                correct_index=nums[i]-1
                nums[i],nums[correct_index]=nums[correct_index],nums[i]
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1
        