import math
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i + 1 for i in range(n)]
        tk = k
        tn = n
        while len(res) < n:
            width = math.factorial(tn - 1)
            idx = (tk - 1) // width
            res.append(str(nums.pop(idx)))
            tn -= 1
            tk -= idx * width
        return "".join(res)

    def getPermuationOrder(self,n,permutation):
        base = [1]*(n+1)
        for i in range(1,n+1):
            base[i] = base[i-1]*i
        used = [False]*n
        order = 0
        for i in range(n):
            used[permutation[i] - 1] = True
            k = 0
            for j in range(permutation[i]-1):
                if not used[j]:
                    k += 1
            order += k * base[n - i - 1]
        return order
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
            n = int(line)
            line = next(lines)
            k = int(line)

            ret = Solution().getPermutation(n, k)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()