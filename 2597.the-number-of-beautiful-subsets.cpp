// @leet start

#include <algorithm>
#include <unordered_map>
#include <vector>
using std::vector;

class Solution {
public:
  int beautifulSubsets(vector<int> &nums, int k) {
    std::sort(nums.begin(), nums.end());

    std::unordered_map<int, int> freqMap;
    // Start at -1 to avoid empty set because increment at start
    int count = -1;

    backtrack(nums, k, 0, freqMap, count);
    return count;
  }

private:
  void backtrack(const vector<int> &nums, int k, int start,
                 std::unordered_map<int, int> &freqMap, int &count) {

    int n = nums.size();
    count++;

    for (int i = start; i < n; ++i) {
      if (freqMap.find(nums[i] - k) == freqMap.end()) {
        // No diffs of k within
        // Because alr sorted, so just check the value before

        freqMap[nums[i]] += 1;
        backtrack(nums, k, i + 1, freqMap, count);
        freqMap[nums[i]] -= 1;
        if (freqMap[nums[i]] <= 0) {
          freqMap.erase(nums[i]);
        }
      }
    }
  }
};
// @leet end
