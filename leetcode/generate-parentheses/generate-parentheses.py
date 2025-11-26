class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def check(left, right, _str):
            if left == n and right == n:
                return ans.append(_str)
            if left < n:
                check(left + 1, right, _str + "(")
            if right < left:
                check(left, right + 1, _str + ")")

        check(0, 0, '')

        return ans