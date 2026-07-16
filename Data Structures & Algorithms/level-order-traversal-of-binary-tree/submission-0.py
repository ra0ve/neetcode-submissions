# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        treeList = []
        if not root:
            return treeList

        level = 0
        queue.append(root)
        while len(queue) > 0:
            temp = []
            print("Level: ", level)
            level += 1
            for x in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            treeList.append(temp)
            

        return treeList