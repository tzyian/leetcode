// @leet start
#include <vector>

using std::vector;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        for (int i = 0; i < n / 2; ++i) {
            char temp = s[i];
            char last = s[n - 1 - i];
            s[i] = last;
            s[n - 1 - i] = temp;
        }
        
    }
};
// @leet end
