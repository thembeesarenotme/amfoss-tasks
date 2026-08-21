class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringx=str(x)
        rev=stringx[::-1]
        if stringx==rev:
            return True
        return False
