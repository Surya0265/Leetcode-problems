/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
     *returnSize=n+1;
     int* arr=(int*)malloc((*returnSize)*sizeof(int));
     int offset=1;
     arr[0]=0;
     for(int i=1;i<=n;i++){
        if(offset*2==i){
            offset=i;
        }
        arr[i]=1+arr[i-offset];
     }
    return arr;
}