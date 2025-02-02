bool check(int* nums, int numsSize) {
    int count=0;
    for(int i=0;i<numsSize-1;i++){
        if(nums[i]>nums[i+1]){
                 count+=1;
        }
    }
    if(nums[numsSize-1]>nums[0]){
        count++;
    }
    if(count<=1){
        return true;
    }
    return false;
    
}