class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = {
            1:'I',
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        roman = []
        k = 1
        while num:
            i = num % 10
            if i == 0:
                pass
            elif i <=3:
                roman.append(m[k]*i)
            elif i <= 5:
                roman.append(m[k]*(5-i) + m[5*k])
            elif i <= 8:
                roman.append(m[5*k] + m[k]*(i-5))
            else:
                roman.append(m[k] + m[10*k])
            k*=10
            num//=10

        return "".join(reversed(roman))

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    while True:
        try:
            line = input()
            num = int(line)

            ret = Solution().intToRoman(num)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()