"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew={}
        def dfs(node):
            if not node:
                return None
            if node in oldtonew:
                return oldtonew[node]
            copy=Node(node.val)
            oldtonew[node]=copy
            for nei in node.neighbors:
               copy.neighbors.append(dfs(nei))
            return copy
        
        c=dfs(node)
        if c==None:
            return None
        return c
            
    
        