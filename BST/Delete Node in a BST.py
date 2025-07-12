# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def getSuccessor(curr):
            
            curr = curr.right
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
          
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
               
                succ = getSuccessor(root)
                root.val = succ.val
               
                root.right = self.deleteNode(root.right, succ.val)

        return root
