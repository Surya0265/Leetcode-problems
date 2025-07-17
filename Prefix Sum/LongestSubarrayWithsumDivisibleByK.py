# Python Program to find the longest subarray with sum
# divisible by k by iterating over all subarrays

def longestSubarrayDivK(arr, k):
  
       
        res=0
        sum=0
        prefix={}
        for i in range(len(arr)):
            sum=(sum+arr[i])%k
            if sum==0:
                res=i+1
            elif sum in prefix:
                 res=max(res,i-prefix[sum])
            else:
                prefix[sum]=1
        return res

if __name__ == "__main__":
    arr = [2, 7, 6, 1, 4, 5]
    k = 3

    print(longestSubarrayDivK(arr, k))