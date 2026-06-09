class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //create hashmap for count
        unordered_map<int, int> count;
        //create vector of vectors for frequence of numbers
        vector<vector<int>> freq(nums.size() + 1);

        //count the frequency for all elements in num
        for(int n: nums){
            count[n] = 1 + count[n];
        }
        //loop through count and put the frequency in the frequency map
        for(const auto& entry: count){
            freq[entry.second].push_back(entry.first);
        }
        vector<int> res;
        for(int i = freq.size() - 1; i > 0;--i){
            for(int n: freq[i]){
                res.push_back(n);
                if (res.size()==k){
                    return res;
                }
            }
        }
        return res;
    }
};
