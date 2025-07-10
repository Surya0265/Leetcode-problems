# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=[root]
        res=[]
        while queue:
             current_level=[]
             for i in range(len(queue)):
              node=queue.pop(0)
              current_level.append(node.val)
              if node.left:
                 queue.append(node.left)
              if  node.right:
                queue.append(node.right)     
             res.insert(0,current_level)  
        return res