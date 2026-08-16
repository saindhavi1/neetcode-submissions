class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer=[]
        nums.sort()
        j = 1
        k = len(nums)-1
        for i in range(len(nums)-2):
            
            j = i+1
            k = len(nums)-1
            while (j < k):
                if (nums[i]+nums[j]+nums[k] > 0):
                    k-=1
                elif (nums[i]+nums[j]+nums[k] < 0):
                    j+=1
                else:
                    if ([nums[i], nums[j], nums[k]] not in answer):
                        answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return answer