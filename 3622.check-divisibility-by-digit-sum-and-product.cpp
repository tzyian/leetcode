// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start
class Solution {
  public:
    bool checkDivisibility(int n) {
        long long sum = 0;
        long long product = 1;
        int x = n;
        while (x > 0) {
            int last = x % 10;
            sum += last;
            product *= last;
            x /= 10;
        }
        return n % (sum + product) == 0;
    }
};
// @leet end
