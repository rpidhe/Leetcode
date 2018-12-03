import json


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = []
        for i in range(len(s)+1):
            match.append([None]*(len(p)+1))
        def sub_match(i,j):
            if match[i][j] is not None:
                return match[i][j]

            if i == len(s):
                while j < len(p) and p[j] == '*':
                    j += 1
                if j == len(p):
                    match[i][j] = True
                    return True
                else:
                    match[i][j] = False
                    return False
            if j == len(p):
                match[i][j] = False
                return False
            if s[i] == p[j] or p[j] == "?":
                match[i][j] = sub_match(i+1,j+1)
                return match[i][j]
            elif p[j] == "*":
                match[i][j] = sub_match(i+1,j) or sub_match(i,j+1)
                return match[i][j]
            else:
                match[i][j] = False
                return False

        return sub_match(0,0)

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
            p = stringToString(line);

            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()