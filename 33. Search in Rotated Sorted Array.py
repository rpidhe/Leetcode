import json
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        rotated = True
        while l <= h:
            mid = (l+h)>>1
            if nums[mid] == target:
                return mid
            elif not rotated:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid - 1
            elif nums[mid] < nums[l]:
                if nums[mid] > target:
                    h = mid - 1
                    rotated = True
                else:
                    if target <= nums[h]:
                        l = mid + 1
                        rotated = False
                    else:
                        h = mid - 1
                        rotated = True
            else:
                if nums[mid] < target:
                    l = mid + 1
                    rotated = True
                else:
                    if target >= nums[l]:
                        h = mid - 1
                        rotated = False
                    else:
                        l = mid + 1
                        rotated = True
        return -1


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
            line = next(lines)
            target = int(line);

            ret = Solution().search(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()