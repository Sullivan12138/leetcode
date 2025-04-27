MOD = 10**9 + 7
MAX_N = 10**4 + 10
MAX_P = 15  # 最多 15 个质因子

def cal_prime_factor(n):
    cnt = {}
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(2, int(n**0.5 +1)):
            if n % i == 0:
                n = n / i
                flag = 1
                if i in cnt.keys():
                    cnt[i] += 1
                else:
                    cnt[i] = 1
                break
    if n in cnt.keys():
        cnt[n] += 1
    else:
        cnt[n] = 1
    return cnt

class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        c = [[0] * 16 for _ in range(10**4+10 + 15)]
        c[0][0] = 1
        for i in range(1,10**4+10 + 15):
            c[i][0] = 1
            for j in range(1, min(i, 15) + 1):
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

        sum = 1
        for i in range(2, maxValue+1):
            cnt = cal_prime_factor(i)
            x = 1
            for j in cnt.keys():
                x = x * c[n+cnt[j]-1][cnt[j]] % MOD
            sum = (sum + x) % MOD
        return int(sum)


        
        