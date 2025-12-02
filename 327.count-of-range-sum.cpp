// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// Using a multiset and lower/upper_bound() still requires you to
// find the distance beween the lower bound and the upper bound.
// The std::distance() function runs in linear time.
// Giving overall O( n(2logn + n) ) = O(n^2) time
//
// Unless you hand-roll your Red-Black trees to also keep track
// of the count of nodes up to each point, giving O(1) distance
// operations which gives O(nlogn) time
//
// e.g.
// https://leetcode.com/problems/count-of-range-sum/solutions/78005/java-red-black-tree-72-ms-solution-by-se-gysd/
// As such, the proper solution is to use a Segtree/Fenwick/Merge sort

// @leet start
class Solution {
  public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        int ans = 0;

        long long psum = 0;
        multiset<long long> ms;
        ms.insert(0);
        for (int i = 0; i < n; ++i) {
            psum += nums[i];

            // ms contains prefix sums up to nums[i]
            // psum - prev_psum >= lower
            // prev_psum <= psum - lower
            //
            // psum - prev_psum <= upper
            // prev_psum >= psum - upper
            //
            // [psum - upper, psum - lower]

            auto upper_it = ms.upper_bound(psum - lower);
            auto lower_it = ms.lower_bound(psum - upper);

            // distance operation iterates from low to high (linear time)
            // which results in overall n^2 time
            // as a result, you need to handroll your RBT to keep track of node
            // counts
            ans += distance(lower_it, upper_it);
            ms.insert(psum);
        }
        return ans;
    }
};
// @leet end
