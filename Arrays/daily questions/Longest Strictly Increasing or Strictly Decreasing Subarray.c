int longestMonotonicSubarray(int* nums, int numsSize) {
    int max=1;
    int inc=1;
    int dec=1;
    for(int i=1;i<numsSize;i++){
        if(nums[i]>nums[i-1]){
             inc+=1;
             dec=1;
             if(inc>max){
                max=inc;
             }
        }
        else if(nums[i]<nums[i-1]){
            dec+=1;
            inc=1;
            if(dec>max){
                max=dec;
            }
        }
        else{
            inc=1;
            dec=1;
        }
    }

    return max;
}