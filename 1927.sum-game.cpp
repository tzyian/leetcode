// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    // note: the previous submission has clearer logic
    // idea is:
    // the LHS sum and RHS sum cancel each other out
    // the LHS ? and RHS ? cancel each other out
    // if Alice is last, Alice can choose to make not equals
    // any number Alice puts, Bob can counter to form a 9
    // so if Bob counters every time, then
    // if num_marks / 2 * 9 == diff, then
    // the numbers are equal
    bool sumGame(string num) {
        int n = num.length();

        int unk_a = 0;
        int sum_a = 0;

        for (int i = 0; i < n; ++i) {
            if (num[i] == '?') {
                unk_a += i < n / 2 ? 1 : -1;
            } else {
                int val = num[i] - '0';
                sum_a += (i < n / 2 ? 1 : -1) * val;
            }
        }

        constexpr bool EQ = false; // bob wins
        constexpr bool NEQ = true; // alice wins

        if ((unk_a & 1) == 1) {
            return NEQ;
        }

        if (sum_a + 9 * unk_a / 2 == 0) {
            return EQ;
        }
        return NEQ;
    }
};
// @leet end
