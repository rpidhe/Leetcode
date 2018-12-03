import json
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        h = len(nums) - 1
        p = h - 1
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1

        if p < 0:
            nums.reverse()
            return
        q = h
        while nums[q] <= nums[p]:
            q -= 1
        tmp = nums[p]
        nums[p] = nums[q]
        nums[q] = tmp
        p += 1
        while p < h:
            tmp = nums[p]
            nums[p] = nums[h]
            nums[h] = tmp
            p += 1
            h -= 1



def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print("Do not return anything, modify nums in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()