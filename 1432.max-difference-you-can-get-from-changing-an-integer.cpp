#include <numeric>
#include <vector>
using std::vector;
#include <string>
using std::string;
#include <iostream>

// @leet start
class Solution {
  public:
    int maxDiff(int num) {
        // for smallest, if largest digit is non-one, change to 1
        // else, change smallest non-one to 0
        //
        // for largest, if largest digit is non-nine, change to 9
        // else, change smallest non-nine to 9
        string numStr = std::to_string(num);
        auto n = numStr.size();
        vector<char> smallVec(numStr.begin(), numStr.end());
        vector<char> bigVec(numStr.begin(), numStr.end());

        bool bigFound = false;
        char bigRepFrom = '\0';

        bool smallFound = false;
        char smallRepFrom = '\0';
        char smallRepTo = '\0';

        for (int i = 0; i < n; i++) {
            char curr = numStr[i];
            if (!bigFound) {
                if (curr != '9') {
                    bigRepFrom = curr;
                    bigFound = true;
                    bigVec[i] = '9';
                }
            } else {
                if (curr == bigRepFrom) {
                    bigVec[i] = '9';
                }
            }

            if (!smallFound) {
                if (i == 0 && curr != '1') {
                    smallRepFrom = curr;
                    smallRepTo = '1';
                    smallFound = true;
                    smallVec[i] = smallRepTo;
                } else if (i > 0 && curr != '1' && curr != '0') {
                    smallRepFrom = curr;
                    smallRepTo = '0';
                    smallFound = true;
                    smallVec[i] = smallRepTo;
                }
            } else {
                if (curr == smallRepFrom) {
                    smallVec[i] = smallRepTo;
                }
            }
        }

        string bigStr(bigVec.begin(), bigVec.end());
        int bigNum = std::stoi(bigStr);
        string smallStr(smallVec.begin(), smallVec.end());
        int smallNum = std::stoi(smallStr);

        return bigNum - smallNum;
    }
};
// @leet end
