import json
import copy
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = []
        for i in range(9):
            row.append([False]*10)
        col = copy.deepcopy(row)
        box = copy.deepcopy(row)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    boxi = (i // 3) * 3 + j // 3
                    row[i][num] = True
                    col[j][num] = True
                    box[boxi][num] = True

        def search(n):
            i = n//9
            j = n%9
            while n < 81 and board[i][j] != '.':
                n += 1
                i = n // 9
                j = n % 9
            if n==81:
                return True
            boxi = (i // 3) * 3 + j // 3
            for v in range(1,10):
                if not row[i][v] and not col[j][v] and not box[boxi][v]:
                    board[i][j]=str(v)
                    row[i][v] = True
                    col[j][v] = True
                    box[boxi][v] = True
                    if search(n+1):
                        return True
                    board[i][j] = '.'
                    row[i][v] = False
                    col[j][v] = False
                    box[boxi][v] = False
            return False
        search(0)


def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
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
            board = stringToChar2dArray(line)

            ret = Solution().solveSudoku(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print("Do not return anything, modify board in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()