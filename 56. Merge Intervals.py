# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda interval:interval.start)
        k = 0
        n = len(intervals)
        merge_intervals = []
        while k < n:
            reach = intervals[k].end
            last = k
            for i in range(k+1,n):
                if intervals[i].start <= reach:
                    if intervals[i].end > reach:
                        reach = intervals[i].end
                    last = i
                else:
                    break
            merge_intervals.append(Interval(intervals[k].start,reach))
            k = last + 1
        return merge_intervals


import json
def stringToInterval(input):
    tokens = json.loads(input)
    return Interval(tokens[0], tokens[1])


def stringToIntervalArray(input):
    intervalArrays = json.loads(input)
    nodes = []
    for intervalArray in intervalArrays:
        nodes.append(stringToInterval(json.dumps(intervalArray)))
    return nodes


def intervalToString(interval):
    return "[{}, {}]".format(interval.start, interval.end)


def intervalArrayToString(intervalArray):
    serializedIntervals = []
    for interval in intervalArray:
        serializedInterval = intervalToString(interval)
        serializedIntervals.append(serializedInterval)
    return "[{}]".format(', '.join(serializedIntervals))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            intervals = stringToIntervalArray(line)

            ret = Solution().merge(intervals)

            out = intervalArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()