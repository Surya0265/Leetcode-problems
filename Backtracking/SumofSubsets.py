res=[]
def sumofsubsets(start,path,currsum):
      n=len(arr)
      if currsum==target:
              res.append(path[:])
              return
      if currsum>target:
             return
      for i in range(n):
             
             path.append(arr[i])
             sumofsubsets(i+1,path,currsum+arr[i])
             path.pop()
             
      
    


arr=list(map(int,input("enter values:").split()))
target=int(input("enter target:"))
sumofsubsets(0,[],0)

for i in res:
       print(i)