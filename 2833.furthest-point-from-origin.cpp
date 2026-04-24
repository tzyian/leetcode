// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    int furthestDistanceFromOrigin(string moves) {
        int dist = 0;
        int underscore = 0;
        for (char x : moves) {
            if (x == 'L') {
                --dist;
            } else if (x == 'R') {
                ++dist;
            } else {
                ++underscore;
            }
        }
        return abs(dist) + underscore;
    }
};
// @leet end
