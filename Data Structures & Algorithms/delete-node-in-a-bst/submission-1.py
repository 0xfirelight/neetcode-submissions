# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root, key)
    
    def delete(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # we have the value here (key == val)
            # 2 case, leaf node and node leaf node
    
            # case 1: no child nodes, can just return nothing
            if not root.right and not root.left:
                return None
    
            # case 2: some children
            if not root.right:
                return root.left
            if not root.left:
                return root.right
    
            min_right =  self.find_min(root.right)
            root.val, min_right.val = min_right.val, root.val
            root.right = self.delete(root.right, key)
            return root
    
        return root

    def find_min(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        while root and root.left:
            root = root.left
        return root


        