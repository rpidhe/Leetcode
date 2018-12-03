# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            head = None
            pre = None
            while root:
                if head == None:
                    if root.left:
                        head = root.left
                        pre = head
                        if root.right:
                            pre.next = root.right
                            pre = pre.next
                    elif root.right:
                        head = root.right
                        pre = head
                else:
                    if root.left:
                        pre.next = root.left
                        pre = pre.next
                    if root.right:
                        pre.next = root.right
                        pre = pre.next
                root = root.next
            root = head