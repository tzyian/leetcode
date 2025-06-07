// @leet start

import java.util.ArrayList;
import java.util.TreeMap;

class Solution {
    public String clearStars(String s) {
        // TC O(nlog26) from n * heap-ops
        // SC O(n) from storing string in heap
        int n = s.length();
        boolean[] deleted = new boolean[n];

        TreeMap<Character, ArrayList<Integer>> map = new TreeMap<>();

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '*') {
                char smallestChar = map.firstKey();
                ArrayList<Integer> charIndices = map.get(smallestChar);
                int toDel = charIndices.get(charIndices.size() - 1);
                deleted[toDel] = true;
                charIndices.remove(charIndices.size() - 1);
                if (charIndices.isEmpty()) {
                    map.remove(smallestChar);
                }
                deleted[i] = true;
            } else {
                map.computeIfAbsent(c, k -> new ArrayList<>()).add(i);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (!deleted[i]) {
                char c = s.charAt(i);
                sb.append(c);
            }
        }

        return sb.toString();

    }
}
// @leet end
