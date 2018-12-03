class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tdict = [0]*256
        tcount = 0
        for c in t:
            tdict[ord(c)] += 1
            if tdict[ord(c)] == 1:
                tcount += 1
        left = 0
        right = 0
        min_size = len(s)+1
        wdict=[0]*256
        min_win = (0,-1)
        cur = 0
        while right < len(s):
            index = ord(s[right])
            if tdict[index] > 0:
                wdict[index] += 1
                if wdict[index] == tdict[index]:
                    cur += 1
                    if cur == tcount:
                        while left <= right and cur == tcount:
                            if right - left + 1 < min_size:
                                min_win = (left,right)
                                min_size = right - left + 1
                            index_left = ord(s[left])
                            if tdict[index_left] > 0:
                                wdict[index_left] -= 1
                                if wdict[index_left] == tdict[index_left] - 1:
                                    cur -= 1
                            left+=1
            right += 1
        return s[min_win[0]:min_win[1]+1]



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
            s = stringToString(line)
            line = next(lines)
            t = stringToString(line)

            ret = Solution().minWindow(s, t)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()