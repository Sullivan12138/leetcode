class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int countOdd, countEven;
        countEven = countOdd = 0;
        for (int i : position) {
            if(i % 2 == 0) countEven++;
            else countOdd++;
        }
        return min(countOdd, countEven);
    }
};