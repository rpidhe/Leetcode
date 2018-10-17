import numpy as np
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # import re
        # pattern = re.compile(p)
        # m = pattern.match(s)
        # return len(m) == len(s)
        self.mem = [None]*(len(s) + 1)
        for i in range(len(self.mem)):
            self.mem[i] = [-1] * (len(p) + 1)
        def match(s, p, i, j):
            if self.mem[i][j] != -1:
                return self.mem[i][j]
            ri = len(s) - i
            rj = len(p) - j
            if rj == 0:
                self.mem[i][j] = ri == 0
                return self.mem[i][j]
            if ri == 0:
                self.mem[i][j] = rj > 1 and p[j+1] == '*' and match(s, p, i, j + 2)
                return self.mem[i][j]
            head_match = s[i] == p[j] or p[j] == '.'
            if rj == 1 or p[j + 1] != "*":
                self.mem[i][j] = head_match and match(s, p, i + 1, j + 1)
                return self.mem[i][j]
            self.mem[i][j] = head_match and match(s, p, i + 1, j) or match(s, p, i, j + 2)
            return self.mem[i][j]

        return match(s,p,0,0)



def stringToString(input):
    import json

    return json.loads(input)


def main():
    while True:
        try:
            s = input()
            p = input()

            ret = Solution().isMatch(s, p)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()