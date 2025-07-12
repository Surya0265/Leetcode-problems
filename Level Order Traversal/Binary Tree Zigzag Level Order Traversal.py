# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        res=[]
        c=0
        if not root:
            return []
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                
                node=q.popleft()
                
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if c==0:
                res.append(level)
                c=1
            else:
                level.reverse()
                res.append(level)
                c=0


            
        return res

        