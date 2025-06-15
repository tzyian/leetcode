// @leet start

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Solution {

    public int maxAdjacentDistance(int[] nums) {
        // return IntStream.range(0, nums.length)
        // .map(i -> Math.abs(nums[i] - nums[(i + 1) % nums.length]))
        // .max()
        // .orElseThrow();
        //
        return Stream.generate(() -> IntStream.of(nums).boxed())
                .flatMap(s -> s)
                .flatMap(x -> Stream.of(x, x))
                .skip(1)
                .limit(2 * nums.length)
                .collect(Collectors.collectingAndThen(
                        // there's no partition in java???
                        Collectors.toList(),
                        list -> {
                            List<Integer> result = new ArrayList<>();
                            for (int i = 0; i < list.size(); i += 2) {
                                int a = list.get(i);
                                int b = list.get(i + 1);
                                result.add(Math.abs(b - a));

                            }
                            return result;
                        }))
                .stream()
                .max(Integer::compareTo)
                .orElseThrow();

    }
}
// @leet end
