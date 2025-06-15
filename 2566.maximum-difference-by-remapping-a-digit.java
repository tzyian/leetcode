// @leet start
class Solution {
    public int minMaxDifference(int num) {
        // i think the nth place should always be remapped to 0 for lowest
        // 100 vs 000
        // for largest, go down nth place. if 9, check (n-1) th place, until nothing can
        // be changed
        String numStr = Integer.toString(num);

        StringBuilder sb = new StringBuilder();

        Character toReplace = null;

        for (int i = 0; i < numStr.length(); i++) {
            char curr = numStr.charAt(i);
            if (toReplace == null) {
                if (curr != '9') {
                    toReplace = curr;
                }
                sb.append('9');
            } else {
                if (curr == toReplace) {
                    sb.append('9');
                } else {
                    sb.append(curr);
                }
            }
        }
        String biggest = sb.toString();
        int bigNum = Integer.parseInt(biggest);

        char firstChar = numStr.charAt(0);
        String firstCharStr = Character.toString(firstChar);
        // probably better to use String::replace here
        String smallest = numStr.replaceAll(firstCharStr, "0");
        int smallNum = Integer.parseInt(smallest);

        return bigNum - smallNum;

    }
}
// @leet end
