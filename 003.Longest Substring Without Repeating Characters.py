
## method 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ''
        tep = ''
        for i in s:
            if i not in tep:
                tep += i
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            if len (tep) > len(ans):
                ans = tep
        return len(ans)


## method 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        left, max_len = 0, 0
        hashtable = {}

        for right in range(len(s)):
            cur_char = s[right]
            if cur_char in hashtable:
                if hashtable[cur_char] + 1 >= left:
                    left = hashtable[cur_char] + 1

            hashtable[cur_char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
