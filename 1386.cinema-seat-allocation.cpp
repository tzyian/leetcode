// @leet imports start
#include "debug.hpp"
// #include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
  private:
    unordered_map<int, int> map;
    bool empty(int shift, int seats) {
        int check = 0b1111 << shift;
        return (seats & check) == 0;
    }

  public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {

        for (const auto& vec : reservedSeats) {
            int row = vec[0];
            int seat = vec[1];
            map[row] |= 1 << seat;
        }

        // from rows with no reserved seats (2 groups)
        int ans = (n - map.size()) * 2;

        for (const auto& [_, seats] : map) {
            bool p1 = empty(2, seats);
            bool p2 = empty(4, seats);
            bool p3 = empty(6, seats);
            if (p1 && p3) {
                ans += 2;
            } else if (p1 || p2 || p3)
                ++ans;
        }
        return ans;
    }
};
// @leet end
int main() {
    Solution s;
    int n = 3;
    vector<vector<int>> vec2 = {{1, 2}, {1, 3}, {1, 8},
                                {2, 6}, {3, 1}, {3, 10}};
    auto out = s.maxNumberOfFamilies(n, vec2);
    debug(out);
}
