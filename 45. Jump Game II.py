class Solution:
    # O(n^2)
    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mstep = [None]*len(nums)
        mstep[0] = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if mstep[j] is None:
                    continue
                if i - j <= nums[j]:
                    if mstep[i] is None or mstep[i] > mstep[j]+1:
                        mstep[i] = mstep[j]+1
        return mstep[-1]
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mstep = [None]*len(nums)
        mstep[0] = 0
        pre = -1
        same_max_id = 0
        for i in range(1,len(nums)):
            if pre != -1 and nums[pre] >= i - pre:
                mstep[i] = mstep[i-1]
                if nums[same_max_id] - nums[i] < i - same_max_id:
                    same_max_id = i
            else:
                mstep[i] = mstep[i-1] + 1
                pre = same_max_id
                same_max_id = i
        return mstep[-1]

import json
def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line);

            ret = Solution().jump(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()