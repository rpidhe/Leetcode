class Solution:
    def __init__(self):
        max_size = 200
        ncr = [[]] * max_size
        for i in range(max_size):
            ncr[i] = [None] * max_size
        ncr[0][0] = 1
        for i in range(max_size):
            ncr[i][i] = ncr[i][0] = 1
        for i in range(1, max_size):
            for j in range(1, i):
                ncr[i][j] = ncr[i - 1][j - 1] + ncr[i - 1][j]

        self.ncr = ncr

    def uniquePaths(self, m, n):
           """
           :type m: int
           :type n: int
           :rtype: int
           """
           # c(n,r) = c(n-1,r-1) + c(n-1,r)

           return self.ncr[m+n-2][n-1]


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
            m = int(line);
            line = next(lines)
            n = int(line);

            ret = Solution().uniquePaths(m, n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()