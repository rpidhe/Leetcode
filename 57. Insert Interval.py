# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import json
class Solution(object):
    def insert(self, intervals: list, newInterval: Interval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return [newInterval]
        def search_s(start,intervals):
            l = 0
            h = len(intervals) - 1
            while l <= h:
                m = (l + h) >> 1
                if intervals[m].end >= start:
                    h = m - 1
                else:
                    l = m + 1
            return h
        def search_b(end, intervals):
            l = 0
            h = len(intervals) - 1
            while l <= h:
                m = (l + h) >> 1
                if intervals[m].start <= end:
                    l = m + 1
                else:
                    h = m - 1
            return l
        l = search_s(newInterval.start,intervals) + 1
        h = search_b(newInterval.end,intervals) - 1
        start = newInterval.start
        if l < len(intervals) and newInterval.start > intervals[l].start:
            start = intervals[l].start
        end = newInterval.end
        if h >= 0 and newInterval.end < intervals[h].end:
            end = intervals[h].end

        return intervals[:l] + [Interval(start,end)] + intervals[h+1:]


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
            line = lines.__next__()
            newInterval = stringToInterval(line)

            ret = Solution().insert(intervals, newInterval)

            out = intervalArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()