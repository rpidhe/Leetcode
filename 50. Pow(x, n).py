class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        if n < 0:
            x = 1/x
            n = -n
        p = x
        while n:
            if n%2 == 1:
                ans = ans*p
            p = p*p
            n//=2
        return ans
def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    while True:
        try:
            line = input()
            x,n = line.strip().split()
            x = float(x)
            n = int(n)
            ret = Solution().myPow(x,n)
            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()