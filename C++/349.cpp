class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        map<int, int> mp;
        vector<int> v;
        for(int i = 0; i < len1; i++) {
            mp[nums1[i]] = 1;
        }
        for(int j = 0; j < len2; j++) {
            if(mp[nums2[j]] == 1) {
                mp[nums2[j]]++;
                v.push_back(nums2[j]);
            }
        }
        return v;
    }
};