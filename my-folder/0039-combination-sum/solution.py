class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # handle constraints
        if len(set(candidates)) != len(candidates):
            return "Candidates are not distinct"
        if not 1 <= len(candidates) <= 30:
            return "Please enter at least 1 candidate and no more than 30 candidates"
        if not 1<= target <= 40:
            return "Please enter a target between 1 and 40"
        
        # set up candidates and result list
        candidates.sort()
        result = []

        # backtracking
        def backtrack(start, combo, total):
            if total == target:
                result.append(combo[:])
                return

            for i in range(start, len(candidates)):
                if total + candidates[i] > target: # pruning step
                    break 
                combo.append(candidates[i])
                backtrack(i, combo, total + candidates[i]) # recursive step
                combo.pop()
            
        backtrack(0, [], 0)
            
        return result
