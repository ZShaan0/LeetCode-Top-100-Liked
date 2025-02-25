class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        if not 0 <= len(digits) <= 4:
            raise ValueError("Please enter a number between 0 and 4 digits long.")

        for digit in digits:
            if int(digit) not in range(2,10):
                raise ValueError("Please ensure the digits are in the range 2 to 9 inclusive.")

        digit_mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return

            letters = digit_mapping[digits[index]]
            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")

        return result

