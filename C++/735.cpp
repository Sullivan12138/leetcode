class Solution {
public:
    void collide(stack<int>& s, int x) {
        if(s.empty()) s.push(x);
        else {
            if(s.top() > 0 && x < 0) {
                int temp = 0 - x;
                if(s.top() > temp) return;
                else if(s.top() < temp) {
                    s.pop();
                    collide(s, x);
                }
                else s.pop();
            }
            else s.push(x);   
        }
    } 
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s;
        vector<int> res;
        for(int i = 0; i < asteroids.size(); i++) {
            collide(s, asteroids[i]);
        }
        while(!s.empty()) {
            res.push_back(s.top());
            s.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};