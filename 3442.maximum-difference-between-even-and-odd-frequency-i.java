// @leet start

import java.util.function.Function;
import java.util.stream.Collectors;

class Solution {
    // with reference to https://stackoverflow.com/a/54792254
    // and https://howtodoinjava.com/java12/collectors-teeing-example/
    public int maxDifference(String s) {
        return s.chars()
                .boxed()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .values()
                .stream()
                .collect(Collectors.teeing(
                        Collectors.filtering(x -> x % 2 != 0, Collectors.maxBy(Long::compare)),
                        Collectors.filtering(x -> x % 2 == 0, Collectors.minBy(Long::compare)),
                        (e1, e2) -> e1.orElseThrow() - e2.orElseThrow()))
                .intValue();

    }
}
// @leet end
