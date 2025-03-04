def partition(arr,low,high):
        i=low-1
        pivot=arr[high]
        for j in range(low,high):
                 if arr[j]<pivot:
                         i+=1
                         swap(arr,i,j)
        swap(arr,i+1,high)
        return i+1

def swap(arr,i,j):
        arr[i],arr[j]=arr[j],arr[i]







def quicksort(arr,low,high):
         if low<high:
                 
                 pi=partition(arr,low,high)
                 quicksort(arr,low,pi-1)
                 quicksort(arr,pi+1,high)



arr=[9,7,3,4,2,1]
quicksort(arr,0,len(arr)-1)
print(arr)
