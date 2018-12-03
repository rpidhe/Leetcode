class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s3_len = len(s3)
        s1_len = len(s1)
        s2_len = len(s2)
        if s3_len != s1_len + s2_len:
            return False

        cache = [[]]*(s1_len+1)
        for i in range(s1_len+1):
            cache[i] = [None]*(s2_len+1)
        def seach(i,j):
            if cache[i][j] != None:
                return cache[i][j]

            k = i + j
            if k==s3_len:
                cache[i][j] = False
                return True
            if i == s1_len:
                while j < s2_len:
                    if s3[k] != s2[j]:
                        cache[i][j] = False
                        return False
                    k += 1
                    j += 1
                cache[i][j] = True
                return True
            if j == s2_len:
                while i < s1_len:
                    if s3[k] != s1[i]:
                        cache[i][j] = False
                        return False
                    k += 1
                    i += 1
                cache[i][j] = True
                return True

            if s3[k] == s1[i] and s3[k] == s2[j]:
                cache[i][j] = seach(i+1,j) or seach(i,j+1)
                return cache[i][j]
            elif s3[k] == s1[i]:
                cache[i][j] = seach( i + 1, j)
                return cache[i][j]
            elif s3[k] == s2[j]:
                cache[i][j] = seach(i, j+1)
                return cache[i][j]
            else:
                cache[i][j] = False
                return False
        return seach(0,0)

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
            s1 = stringToString(line)
            line = next(lines)
            s2 = stringToString(line)
            line = next(lines)
            s3 = stringToString(line)

            ret = Solution().isInterleave(s1, s2, s3)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()