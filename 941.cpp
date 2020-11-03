class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if(A.size() < 3) {
            return false;
        }
        int count = 0;
        for(int i = 0; i < A.size() - 1; i++) {
            if(A[i] == A[i+1]) {
                return false;
            }
            else if(A[i] < A[i+1]) {
                if(count == 2) return false;
                count = 1;
            }
            else {
                if(count == 0) return false;
                count = 2;
            }
        }
        if(count != 2) return false;
        return true;
};