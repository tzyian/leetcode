#include <bits/stdc++.h>
using namespace std;

// @leet start
class Solution {
  public:
    string shortestCommonSupersequence(string str1, string str2) {

        // NOTE: Same as python, and likewise MLE here.
        // But only maintain the previous row and the current row.
        // Similar idea to space-optimised LCS
        // Cuts the table size to m rather than n*m, saving SC.
        // Hence TC O(n*m*(n+m))
        // SC O(m * (n+m))
        auto n = str1.size();
        auto m = str2.size();
        vector<string> prevRow(m + 1);
        for (auto j = 0; j <= m; ++j) {
            // recall substr uses pos, num_chars_to_index
            prevRow[j] = str2.substr(0, j);
        }

        for (int i = 1; i <= n; ++i) {
            vector<string> currRow(m + 1);
            currRow[0] = str1.substr(0, i);

            // go across the row
            for (int j = 1; j <= m; ++j) {
                if (str1[i - 1] == str2[j - 1]) {
                    currRow[j] = prevRow[j - 1] + str1[i - 1];
                } else {
                    string s1 = prevRow[j];
                    string s2 = currRow[j - 1];

                    currRow[j] = s1.size() < s2.size() ? s1 + str1[i - 1]
                                                       : s2 + str2[j - 1];
                }
            }
            prevRow = currRow;
        }

        return prevRow[m];
    }
};
// @leet end
