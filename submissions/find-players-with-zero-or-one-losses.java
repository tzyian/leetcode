// https://leetcode.com/problems/find-players-with-zero-or-one-losses

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.TreeSet;

public class Solution {
    public record Player(int id, int losses) {
    }

    public HashMap<Integer, Player> playerMap;
    public HashMap<Integer, TreeSet<Integer>> lossMap;

    public List<List<Integer>> findWinners(int[][] matches) {
        this.playerMap = new HashMap<>();
        this.lossMap = new HashMap<>();

        TreeSet<Integer> zeroTreeSet = lossMap.computeIfAbsent(0, k -> new TreeSet<>());
        TreeSet<Integer> oneTreeSet = lossMap.computeIfAbsent(1, k -> new TreeSet<>());

        for (int[] match : matches) {
            int winnerId = match[0];
            int loserId = match[1];

            if (!playerMap.containsKey(winnerId)) {
                playerMap.put(winnerId, new Player(winnerId, 0));
                zeroTreeSet.add(winnerId);
            }

            Player loserNode = playerMap.computeIfAbsent(loserId, k -> new Player(loserId, 0));
            TreeSet<Integer> oldTree = this.lossMap.computeIfAbsent(loserNode.losses, k -> new TreeSet<>());
            oldTree.remove(loserId);
            Player updatedLoserNode = this.playerMap.computeIfPresent(loserId, (k1, k2) -> new Player(loserId, loserNode.losses + 1));
            assert updatedLoserNode != null;
            TreeSet<Integer> newTree = this.lossMap.computeIfAbsent(updatedLoserNode.losses, k -> new TreeSet<>());
            newTree.add(loserId);

//            if (!playerMap.containsKey(loserId)) {
//                playerMap.put(loserId, new Player(loserId, 1));
//                oneTreeSet.add(loserId);
//            } else {
//                Player loserNode = this.playerMap.get(loserId);
//                TreeSet<Integer> oldTree = this.lossMap.get(loserNode.losses);
//                Player updatedLoserNode = this.playerMap.computeIfPresent(loserId, (k1, k2) -> new Player(loserId, loserNode.losses + 1));
//                oldTree.remove(loserId);
//                assert updatedLoserNode != null;
//                TreeSet<Integer> newTree = this.lossMap.computeIfAbsent(updatedLoserNode.losses, k -> new TreeSet<>());
//                newTree.add(loserId);
//
//
//            }
        }

        List<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> zeroList = new ArrayList<>(zeroTreeSet);
        ArrayList<Integer> oneList = new ArrayList<>(oneTreeSet);
        result.add(zeroList);
        result.add(oneList);
        return result;

    }

}

