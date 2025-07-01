class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
                if not root:
                 return inf,0,0
            
                la,lb,lc=dfs(root.left)
                ra,rb,rc=dfs(root.right)
                a=1+min(la,lb,lc)+min(ra,rb,rc)
                b=min(la+rb,ra+lb,la+ra)
                c=lb+rb
                return a,b,c
        a,b,c=dfs(root)
        return min(a,b)


