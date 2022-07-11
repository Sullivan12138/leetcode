class MagicDictionary {
private:
    vector<string> s;
public:
    MagicDictionary() {
    }
    
    void buildDict(vector<string> dictionary) {
        for(int i = 0; i < dictionary.size(); i++) {
            this->s.push_back(dictionary[i]);
        }
    }
    
    bool match(string str1, string str2) {
        if(str1.size() != str2.size()) return false;
        int cnt = 0;
        for(int i = 0; i < str1.size(); i++) {
            if(str1[i] != str2[i]) {
                if(cnt > 0) return false;
                cnt++;
            }
        }
        return (cnt==1);
    }
    bool search(string searchWord) {
        for(int i = 0; i < this->s.size(); i++) {
            if(match(searchWord, this->s[i])) return true;
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
 */