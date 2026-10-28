# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        b, h = self.is_balanced(root)
        return b
    

    def is_balanced(self, root) -> (bool, height):
        if not root:
            return True, 0

        lb, lh = self.is_balanced(root.left)
        rb, rh = self.is_balanced(root.right)

        return lb and rb and abs(lh - rh) <= 1, 1 + max(lh, rh)



    def get_height(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

            
        