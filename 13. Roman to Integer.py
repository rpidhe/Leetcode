class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            1: 'I',
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        rm = dict(zip(m.values(),m.keys()))
        num = 0
        for i in range(len(s)):
            rmi = rm[s[i]]
            if i < len(s) -1 and rmi < rm[s[i+1]]:
                num -= rmi
            else:
                num += rmi
        return num

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
            ret = Solution().romanToInt(line)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()