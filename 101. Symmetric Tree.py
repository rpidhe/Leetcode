# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import json
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        Q = [(root,0)]
        def isSym(Q,level):
            i = 0;j = len(Q) - 1
            level_size = (1<<level)
            while i <= j:
                if Q[i][0].val != Q[j][0].val or Q[i][1] != level_size - 1 - Q[j][1]:
                    return False
                i += 1;j -= 1
            return True
        level = 0
        while Q != []:
            if not isSym(Q,level):
                return False
            temp = Q
            Q = []
            for n in temp:
                if n[0].left is not None:
                    Q.append((n[0].left,2*n[1]))
                if n[0].right is not None:
                    Q.append((n[0].right,2*n[1] + 1))
            level += 1
        return True
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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
            root = stringToTreeNode(line);

            ret = Solution().isSymmetric(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()