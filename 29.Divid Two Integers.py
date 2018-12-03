class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = 0
        if dividend > 0 and divisor > 0:
            neg = 0
            dividend = -dividend
            divisor = -divisor
        elif dividend > 0:
            neg = 1
            dividend = -dividend
        elif divisor > 0:
            neg = 1
            divisor = -divisor

        binary = []
        p = divisor
        while p & (1 << 31) > 0:
            binary.append(p)
            p <<= 1
        quotient = 0

        def small_eq_search(arr, k):
            l = 0
            h = len(arr) - 1
            while l <= h:
                m = (l+h) >> 1
                if k >= arr[m]:
                    l = m + 1
                else:
                    h = m - 1

            return l - 1

        def big_eq_search(arr, k):
            l = 0
            h = len(arr) - 1
            while l <= h:
                m = (l + h) >> 1
                if k > arr[m]:
                    h = m - 1
                else:
                    l = m + 1

            return h

        big_eq = len(binary)
        while True:
            big_eq = big_eq_search(binary[:big_eq], dividend)
            if big_eq == -1:
                break
            quotient ^= (1 << big_eq)
            dividend -= binary[big_eq]
        if neg:
            quotient = -quotient
        return quotient



def stringToInt(input):
    return int(input)


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
            line = lines.__next__()
            dividend = stringToInt(line)
            line = lines.__next__()
            divisor = stringToInt(line)

            ret = Solution().divide(dividend, divisor)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()