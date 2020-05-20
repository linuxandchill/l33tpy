class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output_arr = []
        backtrack(output_arr, "", 0, 0, n)
        return output_arr

    def backtrack(arr, currstring, op, close, maximum):
        if len(currstring) == (maximum*2):
            arr.push(currestring)
            return arr

        if op < maximum:
            backtrack(arr, currentstring + "(", op + 1, maximum)
        if close < op:
            backtrack(arr, currentstring + ")", close + 1, maximum)

        
        
        