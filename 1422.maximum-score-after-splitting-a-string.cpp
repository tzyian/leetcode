// @leet start
#include <climits>
#include <string>

using std::string;

class Solution {
  public:
    int maxScore(string s) {
        // score = left_0s + right_1s
        // right_1s = total_1s - left_1s
        // score = left_0s + total_1s - left_1s
        // 0T is constant across all maxes, so add it at the end
        int num_zeroes = 0;
        int num_ones = 0;
        int score = INT_MIN;

        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] == '0') {
                ++num_zeroes;
            } else if (s[i] == '1') {
                ++num_ones;
            }

            score = std::max(score, num_zeroes - num_ones);
        }
        if (s[s.size() - 1] == '1') {
            ++num_ones;
        }
        return score + num_ones;
    };
};
// @leet end
