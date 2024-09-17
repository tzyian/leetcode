// @leet start
#include <algorithm>
#include <string>
#include <vector>
using std::string;

class Solution {
public:
    int findTheLongestSubstring(string s) {
        int prefix_xor = 0;
        int char_map[26] = {};
        std::vector<int> starting_xors(32, -1);
        int longest = 0;

        char_map['a'-'a'] = 1;
        char_map['e'-'a'] = 2;
        char_map['i'-'a'] = 4;
        char_map['o'-'a'] = 8;
        char_map['u'-'a'] = 16;


        for (int i = 0; i < s.size(); i++) {
            prefix_xor ^= char_map[s[i] - 'a'];
            if (starting_xors[prefix_xor] == -1 && prefix_xor != 0) {
                starting_xors[prefix_xor] = i;
            }
            longest = std::max(longest, i - starting_xors[prefix_xor]);
        }

        
        return longest;
    }
};
// @leet end
