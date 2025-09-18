#include <climits>
#include <vector>
using std::vector;

// @leet start
class Solution {
  public:
    int numberOfPairs(vector<vector<int>>& points) {
        std::sort(points.begin(), points.end(),
                  [](const vector<int>& a, const vector<int>& b) {
                      if (a[0] == b[0]) {
                          return a[1] > b[1];
                      } else {
                          return (a[0] < b[0]);
                      }
                  });
        int n = points.size();
        int total = 0;
        for (int i = 0; i < n; ++i) {
            int highest_y = INT_MIN;
            int y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int y2 = points[j][1];
                if (highest_y < y2 && y2 <= y1) {
                    highest_y = y2;
                    ++total;
                }
            }
        }
        return total;
    }
};
// @leet end
