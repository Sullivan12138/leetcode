class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = str(x)
        p = 0
        q = len(y) - 1
        while p < q:
            if y[p] == y[q]:
                p += 1
                q -= 1
            else:
                return False
        return True