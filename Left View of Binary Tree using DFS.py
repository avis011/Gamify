'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def left_view(root):
    result=[]
    helper(root,1,result)
    return result
def helper(root,level,result):
    if root is None:
        return 
    if level>len(result):
        result.append(root.val)
    
    helper(root.left,level+1,result)
    helper(root.right,level+1,result)
