import json


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.get_next("",0,n)

    def get_next(self,pre,unmatch_count,left):
        if left == 0:
            pre += ")"*unmatch_count
            return [pre]
        all = []
        if unmatch_count:
            all.extend(self.get_next(pre + ")",unmatch_count - 1,left))
        all.extend(self.get_next(pre + "(", unmatch_count + 1, left - 1))
        return all

def stringToInt(input):
    return int(input)


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            n = stringToInt(line)

            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()