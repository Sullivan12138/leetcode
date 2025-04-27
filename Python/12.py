class Solution:
    def intToRoman(self, num: int) -> str:
        nn = []
        while num >= 10:
            x = num % 10
            nn.append(x)
            num = int(num / 10)
        nn.append(num)
        nn2 = []
        n = len(nn)
        res = ""
        for i in range(n):
            j = n-1-i
            x = nn[j]
            if x == 4:
                if j == 2:
                    str_x = "CD"
                elif j == 1:
                    str_x = "XL"
                else:
                    str_x = "IV"
            elif x == 9:
                if j == 2:
                    str_x = "CM"
                elif j == 1:
                    str_x = "XC"
                else:
                    str_x = "IX"
            elif 1 < x and x < 4:
                if j == 2:
                    str_x = "C" * x
                elif j == 1:
                    str_x = "X" * x
                elif j == 0:
                    str_x = "I" * x
                else:
                    str_x = "M" * x
            elif 5 < x and x < 9:
                if j == 2:
                    str_x = "D" + "C" * (x-5)
                elif j == 1:
                    str_x = "L" + "X" * (x-5)
                else:
                    str_x = "V" + "I" * (x-5)
            elif x == 1:
                if j == 2:
                    str_x = "C"
                elif j == 1:
                    str_x = "X"
                elif j == 0:
                    str_x = "I"
                else:
                    str_x = "M"
            elif x != 0:
                if j == 2:
                    str_x = "D"
                elif j == 1:
                    str_x = "L"
                else:
                    str_x = "V"
            else:
                continue
            res += str_x 
        return res