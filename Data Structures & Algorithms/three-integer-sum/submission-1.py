class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)):

            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    inputArr = [nums[i], nums[left], nums[right]]
                    if inputArr not in answer:
                        answer.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1

        return answer