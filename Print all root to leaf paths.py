'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
'''
def rootToLeafPaths(root):
    res=[]
    curr=[]
    helper(root,res,curr)
    return res
def helper(root,res,curr):
    if root is None:
        return
    curr.append(root.data)
    if isLeaf(root):
        res.append(curr[:])
    helper(root.left,res,curr)
    helper(root.right,res,curr)
    curr.pop()
