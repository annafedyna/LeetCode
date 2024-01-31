
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque       
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        
        #BFS
        
        depth = 0
        queue = deque(root)
        while len(queue):
            for i in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
    
    
# SOLUTION 2: return 1 + max(maxDepth(root.left), maxDepth(root.right)) ==== DFS