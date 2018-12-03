class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [0]*(rowIndex + 1)
        row[0] = 1
        for i in range(rowIndex + 1):
            row[i] = 1
            pre = row[0]
            for j in range(1,i):
                tmp = row[j]
                row[j] = pre + row[j]
                pre = tmp
        return  row



import json
def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            rowIndex = int(line);

            ret = Solution().getRow(rowIndex)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()