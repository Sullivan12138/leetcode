class Solution:
    def romanToInt(self, s: str) -> int:
        num_i = 0
        num_x = 0
        num_c = 0
        num_m = 0
        num_v = 0
        num_l = 0
        num_d = 0
        n = len(s)
        sum = 0
        for i in range(n):
            if s[i] == 'I':
                num_i += 1
            elif s[i] == 'X':
                sum -= num_i
                num_i = 0
                num_x += 1
            elif s[i] == 'C':
                sum -= 10 * num_x
                num_x = 0 
                num_c += 1
            elif s[i] == 'M':
                sum -= 100 * num_c
                num_c = 0
                num_m += 1
            elif s[i] == 'D':
                sum -= 100 * num_c
                num_c = 0
                num_d += 1
            elif s[i] == 'L':
                sum -= 10 * num_x
                num_x = 0
                num_l += 1
            elif s[i] == 'V':
                sum -= num_i
                num_i = 0
                num_v += 1
            else:
                pass
        sum += 1000 * num_m + 500 * num_d + 100 * num_c + 50 * num_l + 10 * num_x + 5 * num_v + num_i
        return sum
            
        