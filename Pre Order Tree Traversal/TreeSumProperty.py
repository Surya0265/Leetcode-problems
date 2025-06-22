from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None


def insert(arr):
    if not arr:
         return None
    root=Node(arr[0])
    i=1
    q=deque([root])
    while(i<len(arr) and (q)):
           
                 node=q.popleft()
                 node.left=Node(arr[i])
                 q.append(node.left)
                 i+=1
                 if i<len(arr):
                     node.right=Node(arr[i])
                     q.append(node.right)
                     i+=1
    return root
                 


def check(root):
     if not root or root.right is None and root.left is None:
           return True
     else:
           ld=root.left.data if root.left else 0
           rd=root.right.data if root.right else 0
           if root.data==ld+rd:
                 return check(root.left) and check(root.right)
           else:
                 return False




root=None
n=int(input())
arr=list(map(int,input().split()))
root=insert(arr)
if check(root):
       print('yes')
else:
      print('no')