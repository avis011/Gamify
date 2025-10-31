'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def sorted_order(root):
    lst=[]
    sort(root,lst)
    return lst
def sort(root,lst):
    if root is None:
        return
    sort(root.left,lst)
    lst.append(root.val)
    sort(root.right,lst)
