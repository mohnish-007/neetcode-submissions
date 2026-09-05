class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:
            return False
        a=set()
        
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False