class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        con = []
        longest = 0
        longest_s = s[0]
        for i in range(0,len(s)):
            n = len(s)
            new_con = []
            if con:
                cur_longest = i - con[0] + 1
                if cur_longest > len(longest_s):
                    longest_s = s[con[0]:i+1]
            else:
                cur_longest = 1
                if cur_longest > len(longest_s):
                    longest_s = s[i]
            for j in con:
                if i < n - 1 and j > 0 and s[i+1] == s[j-1]:
                    new_con.append(j - 1)
            if i < n - 1:
                if s[i] == s[i+1]:
                    new_con.append(i)
                new_con.append(i+1)
            con = new_con
        return  longest_s

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    while True:
        try:
            s = input()
            ret = Solution().longestPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()