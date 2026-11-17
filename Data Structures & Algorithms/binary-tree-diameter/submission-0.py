# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        acc = [0]
        self.height(root, acc)
        return acc[0]

    def height(self, root: Optional[TreeNode], acc: list[int]) -> int:
        if not root:
            return 0

        hleft = self.height(root.left, acc)
        hright = self.height(root.right, acc)
        h = max(hleft, hright) 
        acc[0] = max(acc[0], hleft + hright)

        return h + 1
        

        
        

        