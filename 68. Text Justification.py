class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        lens = [len(word) for word in words]
        i = 0
        while True:
            line = []
            total_len = 0
            first = 0
            while i < len(words) and total_len + lens[i] + first <= maxWidth:
                line.append(words[i])
                total_len += lens[i] + first
                first = 1
                i+=1

            if i == len(words) or len(line) == 1:
                line_txt = ' '.join(line)
                line_txt += (maxWidth-len(line_txt))*' '
                lines.append(line_txt)
                if i == len(words):
                    break
            else:
                space_num = len(line) - 1
                total_len -= space_num
                spaces = maxWidth - total_len
                base_space = spaces // space_num
                left = spaces % space_num
                line_txt = line[0]
                for j in range(0,space_num):
                    if j < left:
                        pad = ' '*(base_space + 1)
                    else:
                        pad = ' '*base_space
                    line_txt += pad + line[j+1]
                assert len(line_txt) == maxWidth
                lines.append(line_txt)
        return lines

import json
def stringToStringArray(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            words = stringToStringArray(line)
            line = lines.__next__()
            maxWidth = stringToInt(line)

            ret = Solution().fullJustify(words, maxWidth)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()