/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int xor=0;
    int* arr=(int*)malloc(sizeof(int)*2);
    for(int i=0;i<numsSize;i++){
        xor^=nums[i];

    }
    unsigned int diff=1;
    while((xor&diff)==0){
           diff=diff << 1;
    }
    int a=0;
    int b=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]&diff){
            a^=nums[i];
        }
        else{
            b^=nums[i];
        }

    }
    arr[0]=a;
    arr[1]=b;
    *returnSize=2;
    return arr;
    
    
}