# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            # getting length of q so we go through 1 level at a time
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    #adding current node to level
                    level.append(node.val)
                    #adding children
                    q.append(node.left)
                    q.append(node.right)
            #make sure level is non empty
            if level:
                res.append(level)
        return res

        