class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MIN = -2**31
        MAX = 2**31 - 1
        is_prefix = 1
        is_sign = 1
        is_positive = 1
        is_pre_zero = 1
        str_n = ""
        n = 0
        for i in range(len(s)):
            if is_prefix == 1 and s[i] == ' ':
                if is_pre_zero == 1 and is_sign == 1:
                    continue
                else:
                    return 0
            elif is_prefix == 1 and (s[i] == '-' or s[i] == '+'):
                if is_sign == 0:
                    break
                else:
                    is_sign = 0
                if s[i] == '-':
                    is_positive = 0
                continue
            elif is_prefix == 1 and s[i] == '0':
                is_pre_zero = 0
                is_sign = 0
                continue
            elif is_prefix == 1 and s[i] <= '9' and s[i] >= '1':
                is_prefix = 0
                str_n += s[i]
            elif is_prefix == 1:
                return 0
            elif is_prefix == 0 and s[i] <= '9' and s[i] >= '0':
                str_n += s[i]
            else:
                break
            n = int(str_n)
            if is_positive == 0:
                n = -n
            if n > MAX:
                n = MAX
                break
            if n < MIN:
                n = MIN
                break
        return n
