class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector <int> answer(len);
        int product = 1;
        for (int i = 0; i < len; i++) {
            answer[i] = product;
            product *= nums[i];
        }
        int reverseProduct = 1;
        for (int i = len - 1; i >= 0; i--) {
            answer[i] *= reverseProduct;
            reverseProduct *= nums[i];
        }
        return answer;   
    }
};