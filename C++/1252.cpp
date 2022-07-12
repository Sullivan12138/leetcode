class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        int MAXM = 52;
        int b[MAXM], c[MAXM];
        memset(b, 0, MAXM*sizeof(int));
        memset(c, 0, MAXM*sizeof(int));
        for(int i = 0; i < indices.size(); i++) {
            int row = indices[i][0];
            int column = indices[i][1];
            b[row] += 1;
            c[column] += 1;
        }
        int cnt = 0;
        int x1, x2, y1, y2;
        x1=x2=y1=y2=0;
        for(int i = 0; i < m; i++) {
            if(b[i] % 2 == 0) x1++;
            else x2++;
        }
        for(int i = 0; i < n; i++) {
            if(c[i] % 2 == 0) y1++;
            else y2++;
        }
        cnt = x2*n+y2*m-2*x2*y2;
        return cnt;
    }
};
// 高阶写法
class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        long cnt_row = 0, cnt_col = 0;
        for(auto &rc: indices){
            cnt_row ^= (1l << rc[0]); // 取反
            cnt_col ^= (1l << rc[1]);
        }
        int x = __builtin_popcountl(cnt_row); // 1 的数量
        int y = __builtin_popcountl(cnt_col);
        return x * n + y * m - 2 * x * y;
    }
};