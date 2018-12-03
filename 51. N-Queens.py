class Solution(object):


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        state = [None]*n
        results = []
        def legal(state, row,col, n):
            for i in range(row):
                if state[i] == col:
                    return False
                if abs(state[i] - col)==abs(row - i):
                    return False
            return True
        def dfs(row, state,n):
            if row == n:
                result = []
                for i in range(n):
                    line = ['.']*n
                    line[state[i]] = 'Q'
                    result.append("".join(line))
                results.append(result)
                return
            for i in range(n):
                state[row] = i
                if legal(state,row,i,n):
                    dfs(row+1,state,n)
        dfs(0,state,n)
        return results

def stringToInt(input):
    return int(input)

import json
def string2dArrayToString(input):
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
            n = stringToInt(line)

            ret = Solution().solveNQueens(n)

            out = string2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()