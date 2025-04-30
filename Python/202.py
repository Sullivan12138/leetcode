def get_next(n):
    sum = 0
    s = str(n)
    for i in s:
        sum += int(i) ** 2
    return sum

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast_num = get_next(n)
        slow_num = n
        while fast_num != 1 and fast_num != slow_num:
            fast_num = get_next(get_next(fast_num))
            slow_num = get_next(slow_num)
        return fast_num == 1