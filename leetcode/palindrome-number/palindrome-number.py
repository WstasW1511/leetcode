class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = str(x)
        if str(x) == d[::-1]:
            return True
        else:
            return False
        