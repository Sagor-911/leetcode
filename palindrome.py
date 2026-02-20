# 9. Palindrome Number - Easy

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        r = len(x) - 1
        for i in range(len(x)//2):
            if x[i] != x[r]:
                return False
        return True
    
palindrome = Solution()
print(palindrome.isPalindrome(22))