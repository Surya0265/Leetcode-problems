def min_max(arr,low,high):
    if(low==high):
          return arr[low],arr[high]
    if(low+1==high):
           if(arr[low]<arr[high]):
                 return arr[low],arr[high]  
           else:
                 return arr[high],arr[low]
    mid=(low+high)//2
    min1,max1=min_max(arr,low,mid)  
    min2,max2=min_max(arr,mid+1,high)
    return min(min1,min2),max(max1,max2)



arr=[2,6,2,8,3,1]
minx,maxx=min_max(arr,0,len(arr)-1)
print(minx)
print("\n")
print(maxx)