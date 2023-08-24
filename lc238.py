class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [0] * len(nums)
        prod = 1
        for i,num in enumerate(nums):
            prod = prod * num
            prefix[i] = prod

        prod = 1  

        for i,num in enumerate(nums):
            prod *= nums[len(nums)-1 -i]
            postfix[len(nums)-1-i] = prod
        

        for i,num in enumerate(nums):
            if i==0:
                output[i] = postfix[i+1]
            elif i==len(nums)-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]
        return output


            

