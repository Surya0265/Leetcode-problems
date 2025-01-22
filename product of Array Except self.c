
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* answer=(int*)malloc(numsSize*sizeof(int));
    *returnSize=numsSize;
    int prefix=1;
    int suffix=1;
    for(int i=0;i<numsSize;i++){
        answer[i]=prefix;
        prefix*=nums[i];
    }
    for(int i=numsSize-1;i>=0;i--){
        answer[i]*=suffix;
        suffix*=nums[i];
    }
    return answer;
    
}