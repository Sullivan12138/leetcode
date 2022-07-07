class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i = 0; i < nums.size()-2;) {
            int k = nums.size()-1;
            for(int j = i+1; j < nums.size()-1;) {
                while(k > j && nums[i] + nums[j] + nums[k] > 0) k--;
                if(k <= j) break;
                if(nums[i] + nums[j] + nums[k] == 0) {
                    result.push_back(vector<int>({nums[i], nums[j], nums[k]}));
                    k--;
                }
                j++;
                while(j < nums.size()-1 && nums[j] == nums[j-1]) j++;
            }
            i++;
            while(i < nums.size()-2&&nums[i] == nums[i-1]) i++;
        }
        return result;
    }
};