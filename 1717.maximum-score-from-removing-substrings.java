// @leet start
import java.util.ArrayList;

class Solution {

    public int maximumGain(String s, int x, int y) {
        int n = s.length();
        int score = 0;

        char c1 = x >= y ? 'b' : 'a';
        char c2 = x >= y ? 'a' : 'b';
        int higherScore = Math.max(x, y);
        int lowerScore = Math.min(x, y);

        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            char nextChar = s.charAt(i);
            stack.add(nextChar);

            while (stack.size() >= 2
                    && stack.get(stack.size() - 1) == c1
                    && stack.get(stack.size() - 2) == c2) {
                stack.remove(stack.size() - 1);
                stack.remove(stack.size() - 1);
                score += higherScore;
            }
        }
        ArrayList<Character> newStack = new ArrayList<>();

        for (char c : stack) {
            newStack.add(c);

            while (newStack.size() >= 2
                    && newStack.get(newStack.size() - 1) == c2
                    && newStack.get(newStack.size() - 2) == c1) {
                newStack.remove(newStack.size() - 1);
                newStack.remove(newStack.size() - 1);
                score += lowerScore;
            }
        }


        return score;
    }
}
// @leet end
