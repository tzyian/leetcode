// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start

class Solution {
  private:
    static constexpr int MAX_ALPHABETS = 26;
    constexpr char to_char(int x) { return static_cast<char>(x + 'a'); }
    constexpr int to_int(char c) { return c - 'a'; }

  public:
    string lexGreaterPermutation(string s, string target) {
        // using arbitrarily lengths of S and T
        // where |S| = n and |T| = m and |Sigma| = 26
        // taking n, m <= 2 * 10^5
        // hence necessitating TC of O( (n+m) * |sigma|)
        // with bitmask, can drop to O( n + m + |sigma|)

        // Case 1: k = m < n
        // i.e. T is a proper prefix of S
        // fill remaining alphabetically

        // Case 2a: k = n = m
        // i.e. S == T
        // no more chars to take from s

        // Case 2b: k = n < m
        // p is a proper prefix of T
        // no more chars to take from s

        // Case 3: k < n, m
        // i.e. divergence at k < min(n, m)

        std::string ans;
        ans.reserve(s.size());

        int n = s.size();
        int m = target.size();

        unsigned int mask = 0;
        vector<int> freqs(MAX_ALPHABETS);

        auto add_freq = [&](int k) {
            if (++freqs[k] >= 1) {
                mask |= 1 << k;
            }
        };

        auto lower_freq = [&](int k) {
            if (--freqs[k] == 0) {
                mask &= ~(1 << k);
            }
        };

        auto fill_remaining = [&](string& str) {
            for (int i = 0; i < MAX_ALPHABETS; ++i) {
                while (freqs[i] > 0) {
                    lower_freq(i);
                    str += to_char(i);
                }
            }
        };

        auto greater_than = [&](char c) {
            int x = to_int(c);
            // for (int i = x + 1; i < MAX_ALPHABETS; ++i) {
            //     if (freqs[i] > 0) {
            //         return i;
            //     }
            // }
            // return -1;

            // zero out bits <= current idx
            auto available = mask & (~0u << (x + 1));

            if (available == 0) {
                return -1;
            }
            // no. of consec 0s from lsb gives idx of next greater
            return std::countr_zero(available);
        };

        for (char c : s) {
            add_freq(to_int(c));
        }

        // Form prefix
        for (int i = 0; i < min(n, m); ++i) {
            if (freqs[to_int(target[i])] > 0) {
                ans += target[i];
                lower_freq(to_int(target[i]));
            } else {
                break;
            }
        }

        int k = ans.size();

        if (s.empty()) {
            return {};
        } else if (target.empty()) {
            fill_remaining(ans);
            return ans;
        }

        // Case 1, k == m < n
        if (k == m && n > m) {
            fill_remaining(ans);
            return ans;
        }

        // Case 2a
        // k == n == m
        // if S == T,
        // we must turn k back into the next char under consideration
        // since we can't consider idx[n]
        // e.g. if k == 4 == N <= M
        // 0 1 2 3 _
        // a b c d
        // there is no more n to be considered

        // Case 2b:
        // k == n < m
        // k has no more chars
        if (k == n) {
            add_freq(to_int(ans.back()));
            ans.pop_back();
            --k;
        }

        // Case 2+3
        // backtrack
        // k < n, m
        // k is the idx of char under consideration
        for (int i = k; i >= 0; --i) {
            int next_greater = greater_than(target[i]);
            if (next_greater != -1) {
                ans += to_char(next_greater);
                lower_freq(next_greater);
                fill_remaining(ans);
                return ans;
            }

            if (i > 0) {
                add_freq(to_int(ans.back()));
                ans.pop_back();
            }
        }
        return {};
    }
};
// @leet end

int main() {
    Solution s;
    string ss = "zaaz";
    string target = "az";
    auto out = s.lexGreaterPermutation(ss, target);
    debug(out);
}
