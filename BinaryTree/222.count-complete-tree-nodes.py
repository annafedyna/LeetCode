
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: [TreeNode]) -> int:
        """
        Count the number of nodes in a complete binary tree.
        Parameters:
        - root (TreeNode): The root of the binary tree.
        Returns:
        - int: The number of nodes in the binary tree.
        """
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        if not root:
            return 0

        if get_left_height(root) == get_right_height(root):
            return 2**get_left_height(root) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


s = Solution()
tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(s.countNodes(tree))
