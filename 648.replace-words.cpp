// @leet start
#include <string>
#include <vector>
#include <unordered_map>
#include <memory>
using std::string;
using std::vector;

struct TrieNode {
    bool isEnd;
    std::unordered_map<char, std::unique_ptr<TrieNode>> map;

    TrieNode(): isEnd(false) {};
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode trie;
        constructTrie(dictionary, &trie);
        const int& n = sentence.size();

        std::string ans;
        ans.reserve(n);

        TrieNode *curr = &trie;
        int i = 0;
        while (i < n) {
            const char& ch = sentence[i];
            if (ch == ' ') {
                ans.push_back(ch);
                curr = &trie;
                ++i;
            } else if (curr->map.find(ch) != curr->map.end()) {
                curr = curr->map.at(ch).get();
                ans.push_back(ch);
                ++i;
                if (curr->isEnd) {
                    while (i < n && sentence[i] != ' ') {
                        ++i;
                    }
                }
            } else {
                while (i < n && sentence[i] != ' ') {
                    ans.push_back(sentence[i]);
                    ++i;
                }
                curr = &trie;
            }
        }
        return ans;
        
    }
private:
    void constructTrie(const vector<string>& dictionary, TrieNode* root) const {
        for (const auto& word : dictionary) {
           insertWord(word, root); 
        }
    }
    void insertWord(const string& word, TrieNode* root) const {
        TrieNode* curr = root;
        for (const char& ch : word) {
            curr->map.try_emplace(ch, std::make_unique<TrieNode>());
            curr = curr->map.at(ch).get();
        }
        curr->isEnd = true;
    }
};
// @leet end
