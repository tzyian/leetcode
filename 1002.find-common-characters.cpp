// @leet start
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
  vector<string> commonChars(vector<string> &words) {
    std::unordered_map<char, int> firstWord;
    for (int i = 0; i < words.size(); ++i) {
      std::unordered_map<char, int> wordDict;
      for (const auto &c : words[i]) {
        ++wordDict[c];
      }
      // Set first word
      if (i == 0) {
        firstWord = std::move(wordDict);
        continue;
      }
      // Intersection
      for (const auto &[key, value] : firstWord) {
        firstWord[key] = std::min(value, wordDict[key]);
      }
    }

    std::vector<string> v;
    for (const auto& [key, value] : firstWord) {
      for (int i = 0; i < value; ++i) {
        string s{key};
        v.push_back(s);
      }
    }
    return v;
  }
};
// @leet end
