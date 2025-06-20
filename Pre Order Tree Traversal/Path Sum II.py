# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        path=[]
        def dfs(node,path,currsum):
            if not node:
                return
            else:
                path.append(node.val)
                currsum+=node.val
                if not node.right and not node.left and currsum==targetSum:
                      res.append(path[:])
            dfs(node.left,path,currsum)
            dfs(node.right,path,currsum)
            path.pop()
        dfs(root,[],0)
        return res