class Solution:
       def longestConsecutive(self, nums: List[int]) -> int:
           numSet = set(nums)
           counter = 0
           longestConsec = 0

           while counter < len(nums):
               if nums[counter] - 1 not in numSet:
                   startCounter = nums[counter]
                   currentCounter = 1

                   while startCounter + 1 in numSet:
                       currentCounter += 1
                       startCounter += 1

                   longestConsec = max(currentCounter, longestConsec)

               counter += 1

           return longestConsec