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