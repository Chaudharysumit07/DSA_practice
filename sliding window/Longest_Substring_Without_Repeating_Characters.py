# problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ 
# topic: sliding window

## Brute force solution 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res

# Time complexity: O(n∗m)  Space complexity:  O(m) Where n is the length of the string and  m is the total number of unique characters in the string.

## Sliding Window (Optimal)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

  # Time complexity : O(n)  and Space Complexity: O(m) Where n is the length of the string and  m is the total number of unique characters in the string.
