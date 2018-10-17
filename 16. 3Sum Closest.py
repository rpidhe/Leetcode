class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        m = 8888888
        ans = None
        for k in range(len(nums) - 2):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums) - 1
            d = 0
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    i += 1
                    if m > target - s:
                        m = target - s
                        ans = s
                elif s > target:
                    j -= 1
                    if m < s - target:
                        m = s - target
                        ans = s
                else:
                    return target
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
            target = int(input())
            nums = [int(x) for x in line.strip().split(',')]
            ret = Solution().threeSumClosest(nums,target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()