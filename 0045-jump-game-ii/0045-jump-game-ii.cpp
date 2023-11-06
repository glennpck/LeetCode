class Solution {
public:
    int jump(vector<int>& nums) {
        
      for(int i = 1; i < nums.size(); i++)
      {
        nums[i] = max(nums[i] + i, nums[i-1]);
      }

      int index = 0;
      int j = 0;

      while(index < nums.size() - 1)
      {
        j++;
        index = nums[index];
      }

      return j;
    }
};