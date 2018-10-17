# Definition for singly-linked list.
import json


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        ll = self.mergeKLists(lists[:mid])
        rl = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(ll,rl)

    def mergeTwoLists(self,list1,list2):
        p = list1;q = list2
        h = ListNode(-1)
        m = h
        while p and q:
            if p.val < q.val:
                m.next = p
                p = p.next
            else:
                m.next = q
                q = q.next
            m = m.next
        while p:
            m.next = p
            p = p.next
            m = m.next
        while q:
            m.next = q
            q = q.next
            m = m.next
        return h.next



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


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


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
            lists = stringToListNodeArray(line)
            ret = Solution().mergeKLists(lists)
            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()