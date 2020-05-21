class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthsmallest(root, k):
    holder = []
    while True:
        while root:
            holder.append(root)
            root = root.left
        if holder == []:
            return 
        k = k - 1
        current = holder.pop()
        if k == 0:
            return current.val
        root = current.right

node = TreeNode()
kthsmallest(node, k = 1)
    