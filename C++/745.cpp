class WordFilter {
private:
    unordered_map<string, int> m;
public:
    WordFilter(vector<string>& words) {
        for(int i = 0; i < words.size(); i++) {
            string s = words[i];
            for(int p = 0; p < s.size(); p++) {
                for(int q = s.size()-1; q >= 0; q--) {
                    string s1 = s.substr(0, p+1);
                    string s2 = s.substr(q);
                    s1 += "&";
                    s1 += s2;
                    m[s1] = i;
                }
            }
        }
    }
    int f(string pref, string suff) {
        
        string s = pref + "&" + suff;
        if(m.find(s) != m.end()) return m[s];
        return -1;
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(pref,suff);
 */