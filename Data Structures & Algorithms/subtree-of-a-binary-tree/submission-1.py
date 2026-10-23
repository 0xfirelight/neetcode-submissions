# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if self.is_same_tree(node, subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False


    def is_same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False

        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)