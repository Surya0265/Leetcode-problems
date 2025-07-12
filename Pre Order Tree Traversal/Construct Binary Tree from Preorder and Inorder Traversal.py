# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index=0
        in_order={val:i for i,val in enumerate(inorder)}
        def helper(left,right):
            if left>right:
                return None
            root_val=preorder[self.pre_index]
            self.pre_index+1
            root=TreeNode(root_val)
            self.pre_index+=1
            idx=in_order[root_val]
            root.left=helper(left,idx-1)
            root.right=helper(idx+1,right)
            return root
        return helper(0,len(inorder)-1)