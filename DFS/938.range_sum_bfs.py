
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
   
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    sum = 0
    if root is not None and low <= root.val <= high:
        sum += root.val
        
    if root.left and root.right:
        return sum + rangeSumBST(root.right, low, high) + rangeSumBST(root.left, low, high)
    elif root.right: 
        return sum + rangeSumBST(root.right, low, high)
    elif root.left:
        return sum + rangeSumBST(root.left, low, high)
    else: return sum

print(rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15))