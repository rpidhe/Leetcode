class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_arr = [0]*len(triangle)
        for arr in triangle:
            for i in range(len(arr)-1,-1,-1):
                if i == 0:
                    min_arr[i] = min_arr[i] + arr[i]
                elif i == len(arr) - 1:
                    min_arr[i] = min_arr[i-1] + arr[i]
                else:
                    min_arr[i] = min(min_arr[i-1]+arr[i],min_arr[i]+arr[i])
        min_sum = min_arr[0]
        for a in min_arr:
            if min_sum > a:
                min_sum = a
        return min_sum
import json
def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            triangle = stringToInt2dArray(line)

            ret = Solution().minimumTotal(triangle)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()