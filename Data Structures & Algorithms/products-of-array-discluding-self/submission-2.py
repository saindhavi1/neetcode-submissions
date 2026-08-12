class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        
        i = len(nums)-1
        end = 1
        while (i >= 0):
            answer[i] *= end;
            end *= nums[i]
            i-=1;
            
        begin = 1
        i = 0;  
        while (i < len(nums)):
            answer[i]*=begin;
            begin *= nums[i]
            i+=1;
            
        return answer;