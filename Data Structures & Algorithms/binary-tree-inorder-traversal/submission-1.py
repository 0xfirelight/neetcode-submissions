# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.walk(root, [])
        
    def walk(self, root: Optional[TreeNode], acc: List[int]) -> List[int]:
        if not root:
            return acc

        self.walk(root.left, acc)
        acc.append(root.val)
        self.walk(root.right, acc)

        return acc