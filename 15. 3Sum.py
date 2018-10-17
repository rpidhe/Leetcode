class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        triples = []
        if len(nums) < 3:
            return []
        for k in range(len(nums) - 2):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums) - 1
            d = 0
            while i < j:
                s = nums[i] + nums[j]
                if s < -nums[k]:
                    i += 1
                elif s > -nums[k]:
                    j -= 1
                else:
                    triples.append(sorted((nums[k],nums[i], nums[j])))
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i+=1
                    j-=1
        return triples


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
            nums = [int(x) for x in line.strip().split(',')]
            ret = Solution().threeSum(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()