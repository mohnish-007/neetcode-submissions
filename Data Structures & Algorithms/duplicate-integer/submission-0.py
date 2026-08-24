class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:
            return False
        a=set()
        output=False
        for i in nums:
            if i in a:
                output=True
            else:
                a.add(i)
        return output