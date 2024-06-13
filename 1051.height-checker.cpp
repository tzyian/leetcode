// @leet start
#include <vector>
#include <unordered_map>
using std::vector;

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // TC, SC O(n)
        std::unordered_map<int, int> map;
        for (const int& h : heights) {
            ++map[h];
        }

        int wrongs = 0;
        int i = 0;
        int curr = 1;
        while (i < heights.size()) {
            while (map[curr] > 0) {
                if (heights[i] != curr) {
                    ++wrongs;
                }
                ++i;
                --map[curr];
            }
            ++curr;
        }
        return wrongs;
    }
};
// @leet end
