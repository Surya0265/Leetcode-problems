'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        res=[]
        if not root:
            return []
        q=deque([(root,0)])
        m={}
        while q:
            size=len(q)
            for i in range(size):
                node,line=q.popleft()
                m[line]=node.data
                if node.left:
                    q.append((node.left,line-1))
                if node.right:
                    q.append((node.right,line+1))
        for key in sorted(m):
              res.append(m[key])
        return res