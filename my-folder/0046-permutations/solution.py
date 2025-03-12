class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #handle constraints
        if len(set(nums)) != len(nums):
            raise ValueError("Numbers are not unique")
        if not 1 <= len(nums) <= 6:
            raise ValueError("Enter a list of between 1 and 6 numbers")
        for num in nums:
            if not -10 <= num <= 10:
                raise ValueError("All numbers must be between -10 and 10")
        
        result = []

        #backtracking
        def backtrack(permutation: list, used: set):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    backtrack(permutation + [num], used)
                    used.remove(num)
        
        backtrack([], set())

        return result
        
        
