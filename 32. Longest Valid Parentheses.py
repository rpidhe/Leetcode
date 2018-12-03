class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        right_max = [0]*len(s)
        for i in range(len(s)):
            while i < len(s) and s[i] == "(":
                i += 1

            if i == len(s):
                break
            if i == 0:
                continue
            pre_left = i - right_max[i-1] - 1
            if pre_left >= 0 and  s[pre_left] == "(":
                right_max[i] = right_max[i-1]+2
                if pre_left > 0:
                    right_max[i] += right_max[pre_left - 1]
        m = 0
        for c in right_max:
            if m < c:
                m = c
        return m



def stringToString(input):
    import json

    return json.loads(input)


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
            s = stringToString(line);

            ret = Solution().longestValidParentheses(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()