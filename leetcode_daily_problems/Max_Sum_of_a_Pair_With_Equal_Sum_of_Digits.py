# date 12 feb 2025
# Question link : https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

# my solution : Time Complexity = O(N log M)  where N is the number of elements in nums and where M is the max value in nums ; Space Complexity : O(N)

class Solution:
    def sumOfDigits(self, num: int) -> int:
        sod = 0
        while num > 0:
            sod += num % 10
            num //= 10  # Fix: Integer division
        return sod


    def findTwoLargest(self, array,num):
        myList=[]
        if num > array[0] :
            if array[0] >array[1]:
                myList.append(num)
                myList.append(array[0])
            else:
                myList.append(num)
                myList.append(array[1])
        else:
            if num > array[1]:
                myList.append(num)
                myList.append(array[0])
            else:
                myList.append(array[1])
                myList.append(array[0])
        return myList

    def maximumSum(self, nums: List[int]) -> int:
        digSumDict = {}

        # print("Processing input numbers...")
        for num in nums:
            sod = self.sumOfDigits(num)
            # print(f"Number: {num}, Sum of Digits: {sod}")

            if sod not in digSumDict:
                digSumDict[sod] = [num]
            else:
                if len(digSumDict[sod]) < 2:
                    digSumDict[sod].append(num)  # Fix: Use append()
                else:
                    twonumarray = self.findTwoLargest(digSumDict[sod],num)
                    # print(f"twonumarray: {twonumarray}")
                    digSumDict[sod] = twonumarray
        max_sum = -1
        # print("\nChecking maximum sum pairs...")

        for arrays in digSumDict.values():
            # print(f"arrays: {arrays}")
            if len(arrays) >1:
                sumtot=0
                for num in arrays:
                    sumtot+=num
                # print(f"Sumtotal: {sumtot}")
                max_sum=max(sumtot,max_sum)

        # print(f"Maximum sum of any two numbers with the same digit sum: {max_sum}\n")
        return max_sum
