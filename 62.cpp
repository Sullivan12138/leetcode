class Solution {
public:
    int uniquePaths(int m, int n) {
        int a[101][101] = {0};
        a[0][0] = 1;
        for(int i = 0; i < m; i ++) {
            for(int j = 0; j < n; j++) {
                a[i][j] += ((i-1) >= 0) ? a[i-1][j] : 0;
                a[i][j] += ((j-1) >= 0) ? a[i][j-1] : 0;
            }
        }
        return a[m-1][n-1];
    }
};