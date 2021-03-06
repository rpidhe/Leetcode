# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if postorder == []:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        in_indx = 0
        while inorder[in_indx] != root_val:
            in_indx += 1
        root.left = self.buildTree(inorder[:in_indx],postorder[0:in_indx])
        root.right = self.buildTree(inorder[in_indx+1:],postorder[in_indx:-1])
        return root


import json

def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            preorder = stringToIntegerList(line);
            line = next(lines)
            inorder = stringToIntegerList(line);

            ret = Solution().buildTree(preorder, inorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()