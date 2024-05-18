// Method taken from https://leetcode.com/problems/distribute-coins-in-binary-tree/solutions/256136/java-recursion-really-easy-to-understand/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @leet start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <cstdlib>
#include <tuple>

class Solution {
public:
    int distributeCoins(TreeNode* root) {
        int moves;
        std::tie(std::ignore, moves) = getNumNodes(root);
        return moves;
    }

private:
    std::tuple<int, int> getNumNodes(TreeNode* root) {
        if (root == nullptr) {
            return {0, 0};
        }

        auto [leftExtra, leftMoves] = getNumNodes(root->left);
        auto [rightExtra, rightMoves] = getNumNodes(root->right);

        // Can also be done by passing 3 vars: nodes, moves, coins (see previous submission).
        // -1 because if root is 1, no extra moves needed.
        // extraCoins is equiv to sum of abs(numNodes - numCoins) on both subtrees
        // then doing wishful thinking.
        int extraCoins = root->val - 1 + leftExtra + rightExtra;
        // extraCoins can be negative i.e. need to pass coins down 
        // but it's still a move.
        int moves = leftMoves + rightMoves + std::abs(extraCoins);

        return {extraCoins, moves};
    }

};
// @leet end
