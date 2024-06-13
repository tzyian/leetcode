// @leet start
#include <map>
#include <vector>

using std::vector;

class Solution {
public:
  bool isNStraightHand(vector<int> &hand, int groupSize) {
    // TC O(nlogn) for each making and iterating treemap
    // SC O(n) for treemap
    if (hand.size() % groupSize != 0) {
      return false;
    }

    std::map<int, int> map;
    for (const auto &var : hand) {
      ++map[var];
    }

    while (!map.empty()) {
      if (map.size() < groupSize) {
        return false;
      }
      int firstEle = map.begin()->first;

      for (int i = 0; i < groupSize; ++i) {
        if (map[firstEle + i] == 0) {
          return false;
        }
        --map[firstEle + i];
        if (map[firstEle + i] == 0) {
          map.erase(firstEle + i);
        }
      }
    }
    return true;
  }
};
// @leet end
