class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        int f[102][51][51];
        for(int k = 0; k < 102; k++) {
            for(int i = 0; i < 51; i++) {
                for(int j = 0; j < 51; j++) {
                    f[k][i][j] = -10000;
                }
            }
        }
        f[2][1][1] = grid[0][0];
        for(int k = 3; k <= 2*n; k++) {
            for(int i = 1; i <= n; i++) {
                for(int j = i; j <= n; j++) {
                    if(k-i-1< 0 || k-j-1<0 || k-i-1>= n || j-j-1>=n) continue; 
                    if(grid[i-1][k-i-1] == -1 || grid[j-1][k-j-1] == -1) continue;
                    int state[4];
                    state[0] = f[k-1][i-1][j];
                    state[1] = f[k-1][i][j-1];
                    state[2] = f[k-1][i][j];
                    state[3] = f[k-1][i-1][j-1];
                    int maxState = max(max(state[0],state[1]), max(state[2],state[3]));
                    if(i != j) maxState += (grid[i-1][k-i-1] + grid[j-1][k-j-1]);
                    else maxState += grid[i-1][k-i-1];
                    f[k][i][j] = maxState;
                }
            }
        }
        return max(f[2*n][n][n], 0);
    }
};