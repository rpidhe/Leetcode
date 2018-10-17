import json
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = ListNode(-1)
        new_head.next = head
        ll = 0
        p = new_head
        while p.next:
            p = p.next
            ll+=1
        m = ll//k
        q = new_head
        p = head
        while m:
            q.next = None
            for i in range(k):
                r = p.next
                p.next = q.next
                q.next = p
                p = r
            for i in range(k):
                q = q.next
            q.next = p
            m-=1
        return new_head.next

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToInt(input):
    return int(input)


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            head = stringToListNode(line)
            line = lines.__next__()
            k = stringToInt(line)

            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()