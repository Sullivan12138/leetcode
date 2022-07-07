class Solution {
public:
    bool isStartWith(string successor, string root) {
        int p, q;
        p = q = 0;
        if(successor.size() < root.size()) return false;
        while(q < root.size()) {
            if(successor[p++] != root[q++]) return false;
        }
        return true;
    }
    string replaceWords(vector<string>& dictionary, string sentence) {
        char* temp = new char[sentence.length() + 1];
        strcpy(temp, sentence.c_str());
        vector<string> roots;
        char *p = strtok(temp, " ");
        while(p) {
            string s = p;
            roots.push_back(s);
            p = strtok(NULL, " ");
        }
        for(int i = 0; i < roots.size(); i++) {
            string str = roots[i];
            int minLength = 101;
            int minIndex = -1;
            for(int j = 0; j < dictionary.size(); j++) {
                if(isStartWith(str, dictionary[j])) {
                    if(minLength > dictionary[j].size()) {
                        minLength = dictionary[j].size();
                        minIndex = j;
                    }
                }
            }
            if(minIndex >= 0) roots[i] = dictionary[minIndex];
        }
        string result = "";
        for(int i = 0; i < roots.size(); i++) {
            result += roots[i];
            if(i != roots.size() - 1) {
                result += " ";
            }
        }
        return result;
    }
};