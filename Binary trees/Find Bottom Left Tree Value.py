# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
         q=deque([root])
         while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.right:
                 q.append(node.right)
                if node.left:
                 q.append(node.left)
         return node.val

        