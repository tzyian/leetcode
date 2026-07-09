// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
// NOTE:
// consteval is CPP20. CPP17 can use constexpr instead
// consteval is guaranteed compile
// init_pow() has to be defined outside because members are not fully defined
// until after class defintion is finished, so pow cannot be constexpr if this
// is defined within the class static consteval array<int, MAX> init_pow() {

// NOTE: good practice to default initalise pow with {}
// to force array to be of 0s rather than garbage

// std::array<int, MAX> p{};
// static consteval std::array<int, MAX> init_pow() {
//     p[0] = 1;
//     for (int i = 1; i < MAX; ++i)
//         p[i] = p[i - 1] * 10LL % MOD;
//     return p;
// }

class Solution {
  private:
    // NOTE: standard practice is to put static first
    static constexpr int MOD = 1'000'000'007;
    static constexpr int MAX = 1'00'001;

    // immediate invoked lambda expression (IIFE)
    static constexpr std::array<int, MAX> pow = []() consteval {
        std::array<int, MAX> p{};
        p[0] = 1;
        for (int i = 1; i < MAX; ++i) {
            p[i] = (p[i - 1] * 10LL) % MOD;
        }
        return p;
    }();

    // static inline array<int, MAX> pow{}
    // static inline int init = []() {
    //     pow[0] = 1;
    //     for (int i = 1; i < MAX; ++i)
    //         pow[i] = pow[i - 1] * 10LL % MOD;
    //     return 0;
    // }();

  public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        auto n = s.size();
        vector<int> psums(n + 1, 0), pnums(n + 1, 0), lens(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            int d = s[i] - '0';
            psums[i + 1] = psums[i] + d;
            pnums[i + 1] = (pnums[i] * (d > 0 ? 10LL : 1LL) + d) % MOD;
            lens[i + 1] = lens[i] + (d > 0);
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            long long l = q[0];
            long long r = q[1];
            // 5 to 5748 from l to r + 1
            // we want 748
            int exp = lens[r + 1] - lens[l];
            long long sub = pnums[l] * 1LL * pow[exp] % MOD;
            // in cpp you must do (x+MOD) % MOD to get positive mod
            long long x = (pnums[r + 1] - sub + MOD) % MOD;

            long long sum = psums[r + 1] - psums[l];
            long long next_val = (sum * x) % MOD;
            ans.push_back(next_val);
        }
        return ans;
    }
};

// @leet end
class SolutionWrong {
  private:
    long long pow(long long a, long long b) {
        long long res = 1;
        while (b > 0) {
            if (b & 1)
                res *= a;
            a *= a;
            b >>= 1;
        }
        return res;
    }

  public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        // it's 1 with 10**5 0's behind, not 10**5 itself
        vector<int> psums{0};
        psums.reserve(s.size());
        vector<int> pdigits;
        pdigits.reserve(s.size());

        int digits_before = 0;
        int xs = 0;
        for (char c : s) {
            pdigits.push_back(digits_before);

            int d = c - '0';
            psums.push_back(psums.back() + d);
            if (d > 0) {
                xs = xs * 10 + d;
                ++digits_before;
            }
        }
        pdigits.push_back(digits_before);

        // i       0 1 2 3 4 5 6 7
        // s       1 0 2 0 3 0 0 4
        // x       1   2   3     4
        // psums 0 1 1 3 3 6 6 6 10
        // pdigits 0 1 1 2 2 3 3 3 4
        //           l   r
        // l = 1, r = 3
        // 2
        // 1 2 3 4

        constexpr int MOD = 1'000'000'007;
        vector<int> ans;
        int n = digits_before;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];
            // l = 0, r = 5, psums = 0 [0 1 2 3 4 5]
            // (everything is shifted by one)
            long long sum = psums[r + 1] - psums[l];
            long long before = pow(10, n - pdigits[l]);
            long long after = pow(10, n - pdigits[r + 1]);
            long long x = (xs % before) / after;
            ans.push_back((sum * x) % MOD);
        }
        return ans;
    }
};

int main() {
    Solution s;
    string st = "102030405060708090102030405060708090";
    vector<vector<int>> queries{{0, 35}, {0, 17}, {18, 35}};
    auto out = s.sumAndMultiply(st, queries);
    debug(out);
}
