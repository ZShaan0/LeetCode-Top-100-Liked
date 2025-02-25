class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not 1 <= n <= 8:
            raise ValueError("n must be between 1 and 8 inclusive.")

        result = []

        def backtrack(combo: str, open_count: int, close_count: int):
            if len(combo) == 2 * n:
                result.append(combo)
                return

            if open_count < n:
                backtrack(combo + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(combo + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result

