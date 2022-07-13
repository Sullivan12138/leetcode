class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rNum = dNum = 0
        r = [False] * len(senate)
        d = [False] * len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                r[i] = True
                rNum += 1
            else:
                d[i] = True
                dNum += 1
        rCount = dCount = 0
        while(rNum !=0 and dNum != 0):
            p = 0
            while(p < len(senate)):
                if(senate[p] == "R" and r[p] is True):
                    if(dCount != 0):
                        dCount -= 1
                        rNum -= 1
                        r[p] = False
                    else:
                        rCount += 1
                elif(senate[p] == "D" and d[p] is True):
                    if(rCount != 0):
                        rCount -= 1
                        dNum -= 1
                        d[p] = False
                    else:
                        dCount += 1
                p += 1
        if(rNum == 0):
            return "Dire"
        else:
            return "Radiant"   
