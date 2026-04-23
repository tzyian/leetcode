// @leet imports start
#include <bits/stdc++.h>
#include <cstdlib>
#include <map>
#include <utility>
using namespace std;
// @leet imports end

// @leet start
// NOTE: brute force will TLE
// to do it properly, use psums
// break down each summation operation into i-j
// Then a pattern is formed.
// i    psum
// 3    3               (5-3 + 8-3 + 10-3)
// 5    8       (5-3) + (8-5 + 10-5 + 11-5)
// 8    16      (8-3 + 5-3) + ...
// 10   26
// 11   37

// After sum: psum_aft - count_aft * i
// Before sum: count_bef * i - psum_bef

using ll = long long;

class Solution {
  public:
    vector<long long> distance(vector<int>& nums) {
        auto n = nums.size();
        // value : vec<idx, psum>
        map<int, vector<pair<int, ll>>> dict;
        vector<ll> dsts(n, 0);
        for (auto i = 0; i < n; ++i) {
            ll x = nums[i];
            auto it = dict.find(x);
            if (it == dict.end()) {
                dict[x] = vector{pair{i, ll(i)}};
            } else {
                auto& vec = it->second;
                ll psum = vec.back().second;
                vec.emplace_back(i, psum + i);
            }
        }
        for (const auto& [_, vec] : dict) {
            auto m = vec.size();
            for (auto i = 0; i < m; ++i) {
                ll nums_idx = vec[i].first;
                ll sum_bef_i = 0LL;
                ll sum_aft_i = 0LL;
                if (i > 0) {
                    ll count_before = i;
                    ll pre_sum = vec[i - 1].second;
                    sum_bef_i = count_before * nums_idx - pre_sum;
                }
                if (i < m - 1) {
                    ll count_aft = m - i - 1;
                    ll post_sum = vec.back().second - vec[i].second;
                    sum_aft_i = post_sum - count_aft * nums_idx;
                }
                dsts[nums_idx] = sum_bef_i + sum_aft_i;
            }
        }
        return dsts;
    }
};
// @leet end
