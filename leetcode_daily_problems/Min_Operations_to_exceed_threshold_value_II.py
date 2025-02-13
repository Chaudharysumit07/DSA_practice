Question name: Minimum Operations to Exceed Threshold Value II
Question link:https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

Approach : using minheap

T.C = O(NlogN)   S.C.= O(N)

Solution:

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        countOfOp=0

        while len(nums) >=2 and nums[0] < k:
            x= heapq.heappop(nums)
            y= heapq.heappop(nums)
            val= min(x,y)*2 + max(x,y)
            heapq.heappush(nums,val)
            countOfOp+=1

        return countOfOp

        
