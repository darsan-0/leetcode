class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        vector <int> vec;
        int ans = 0;
        for (int i = 0 ; i < nums.size(); i++){
            for (int j = i + 1 ; j < nums.size(); j++){
                if (nums[i] == nums[j]){
                    vec.push_back(nums[i]);
                }
            }
        }
        for(int val : vec){
            ans ^= val;
        }

        return ans;
    }
};
