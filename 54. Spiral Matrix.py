class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        top,left = 0,0
        result = []
        while m > 1 and n > 1:
            for i in range(n-1):
                result.append(matrix[top][i+left])
            for j in range(m - 1):
                result.append(matrix[j+top][left+n-1])
            for  i in range(n-1):
                result.append(matrix[top + m - 1][left + n - i - 1])
            for j in range(m - 1):
                result.append(matrix[top + m - j - 1][left])
            left += 1
            top += 1
            m -= 2
            n -= 2
        if m==1:
            for i in range(n):
                result.append(matrix[top][i+left])
        elif n == 1:
            for j in range(m):
                result.append(matrix[j + top][left + n - 1])
        return result

import json
def stringToInt2dArray(input):
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
            matrix = stringToInt2dArray(line)

            ret = Solution().spiralOrder(matrix)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()