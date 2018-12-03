class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        lenw = len(words[0])
        n = len(s)
        count = {}
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

        for i in range(lenw):
            for j in range(i,n,lenw):


def stringToString(input):
    return input[1:-1].decode('string_escape')

import json
def stringToStringArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            s = stringToString(line)
            line = lines.__next__()
            words = stringToStringArray(line)

            ret = Solution().findSubstring(s, words)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()