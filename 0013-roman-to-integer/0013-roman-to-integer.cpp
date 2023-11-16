class Solution {
public:
    int romanToInt(string s) {
        int val = 0;
        map<char, int> r;
        r['I'] = 1;
        r['V'] = 5;
        r['X'] = 10;
        r['L'] = 50;
        r['C'] = 100;
        r['D'] = 500;
        r['M'] = 1000;
        
        for(int i = 0; i < s.length(); i++){
            if(r[s[i]] < r[s[i+1]]){
                val -= r[s[i]];
            }
            else{
                val += r[s[i]];
            }
        }
        return val;
    }
};