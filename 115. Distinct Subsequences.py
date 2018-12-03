class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_t = len(t);len_s = len(s)
        if len_s == 0:
            return 0
        count = [[]]*len_t
        for i in range(len_t):
            count[i] = [0]*len_s

        for i in range(len_t):
            for j in range(len_s):
                if j > 0:
                    count[i][j] = count[i][j-1]
                if t[i] == s[j]:
                    if i > 0 and j > 0:
                        count[i][j] += count[i-1][j-1]
                    elif i == 0:
                        count[i][j] += 1
        count = [] * len_t
        for i in range(len_t):
            for j in range(len_s):
                if t[i] == s[j]:
                    if i > 0 and j > 0:
                        count[i] += count[i-1]
                    elif i == 0:
                        count[i] += 1

        return count[len_t-1]
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
            line = next(lines)
            t = stringToString(line);

            ret = Solution().numDistinct(s, t)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()