// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start
using ll = long long;
class Solution {
  public:
    int distinctSubseqII(string s) {
        int MOD = 1'000'000'007;
        int SIZE = 26;
        auto seen = vector<ll>(SIZE);

        ll prev = 0;
        for (char c : s) {
            // 1. if prev = adc, then curr is (adc) + (adc.d) + (d)
            // 2. subtract duplicates which also end in d (d, ad)
            // then (+MOD)%MOD to ensure positive modulus
            // 3. update the duplicates (adc.d)
            int x = c - 'a';
            ll curr = (prev * 2 + 1) % MOD;      // 1
            curr = (curr - seen[x] + MOD) % MOD; // 2
            seen[x] = (prev + 1) % MOD;          // 3
            prev = curr;
        }

        return prev;
    }
};
// @leet end

int main() {
    Solution s;
    string s1 = "ababa";
    // a, ab, aba, abab, ababa // 5
    // b, ba, bab, baba // 4
    // aa, aab, aaba, // 3
    // baa, abaa  // 2
    // aaa
    // abba
    // b, bb, bba // 3

    string s2 =
        "asdasdasidoajsasjdasdjasdjasdasdasdajsdknajsdnakjsdnakjsdnakjsdnoqqiow"
        "rjsauasiufansfakjfndsssssdfsdfsdfsdfssssssssssssssssssssssfsdfsdfsdfka"
        "nfiuanisfaosifnaosdnaosudhuhfnansdnvsnbfugisdgg";

    auto out = s.distinctSubseqII(s2);
    debug(out);
}
