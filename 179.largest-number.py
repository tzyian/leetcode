# @leet start
from typing import List

ALPHABET_SIZE = 10  # 0 to 9

# NOTE: This solution is not correct. It fails for the test case 5.


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        trie = Trie(ALPHABET_SIZE)
        ans = []
        for num in nums:
            trie.add(str(num))
        trie.find_largest(ans)
        ans_str = "".join(ans)
        if ans_str[0] == "0":
            return "0"
        return ans_str


class TrieNode:
    def __init__(self, num_size: int):
        self.children = [None] * 10
        self.end_counter = 0


class Trie:
    def __init__(self, num_size: int = 10):
        self.num_size = num_size
        self.root = TrieNode(num_size)

    def add(self, s: str) -> None:
        curr = self.root
        for c in s:
            idx = int(c)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode(self.num_size)
            curr = curr.children[idx]
        curr.end_counter += 1

    def find_largest(
        self, ans: list[str], node: TrieNode = None, new_num: list[str] = None
    ) -> None:
        if node is None:
            node = self.root
        if new_num is None:
            new_num = []

        for child_val in range(
            self.num_size - 1, -1, -1
        ):  # Iterate from largest child to smallest
            child = node.children[child_val]

            parent_val = int(new_num[-1]) if new_num else -1  # -1 if at root

            if child is not None and child_val > parent_val:  # child > parent
                new_num.append(str(child_val))
                self.find_largest(ans, child, new_num)
                new_num.pop()
            elif child_val == parent_val:  # child == parent
                if child is not None:
                    new_num.append(str(child_val))
                    self.find_largest(ans, child, new_num)
                    new_num.pop()
                while node.end_counter > 0:
                    ans.extend(new_num)
                    node.end_counter -= 1
            elif child is not None:  # child < parent
                new_num.append(str(child_val))
                self.find_largest(ans, child, new_num)
                new_num.pop()

        # Handle any remaining end counts at this node
        while node.end_counter > 0:
            ans.extend(new_num)
            node.end_counter -= 1


# @leet end

sol = Solution()

test_cases = [
    ([10, 2], "210"),  # Test case 1: Simple case
    ([3, 30, 34, 5, 9], "9534330"),  # Test case 2: Larger input
    ([0, 0], "0"),  # Test case 3: All numbers are zero
    ([1, 112, 111], "1121111"),  # Test case 4: Mixed length numbers
    ([34323, 3432], "343234323"),  # Test case 5: Complex case. NOTE: FAILS!
]

# Loop through each test case
for i, (input_data, expected) in enumerate(test_cases, 1):
    result = sol.largestNumber(input_data)
    print(f"Test case {i}: {'Pass' if result == expected else 'Fail'}")
