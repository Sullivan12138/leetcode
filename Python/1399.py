class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = [0] * n
        for i in range(n):
            str_n = str(i+1)
            for j in range(len(str_n)):
                sum[i] += int(str_n[j])
        dict = {}
        for i in range(n):
            if sum[i] in dict:
                dict[sum[i]] += 1
            else:
                dict[sum[i]] = 1
        max = 0
        max_cnt = 0
        for k in dict.keys():
            if dict[k] > max:
                max = dict[k]
                max_cnt = 1
            elif dict[k] == max:
                max_cnt += 1
            else:
                pass
        return max_cnt

        