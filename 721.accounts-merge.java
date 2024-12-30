// @leet start

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        List<List<String>> ansList = new ArrayList<>();

        Map<String, ArrayList<Integer>> emailToIdx = new HashMap<>();
        Map<String, String> emailToName = new HashMap<>();

        for (int i = 0; i < accounts.size(); i++) {
            List<String> acc = accounts.get(i);
            String name = acc.get(0);
            for (int j = 1; j < acc.size(); j++) {
                String email = acc.get(j);
                emailToName.put(email, name);
                emailToIdx.computeIfAbsent(email, k -> new ArrayList<>())
                        .add(i);
            }
        }

        Set<Integer> visited = new HashSet<>();

        for (int i = 0; i < accounts.size(); i++) {
            if (visited.contains(i)) {
                continue;
            }
            String name = accounts.get(i).get(0);
            Set<String> emails = new HashSet<>();
            dfs(i, emails, visited, emailToIdx, accounts);
            List<String> emailList = new ArrayList<>(emails);
            Collections.sort(emailList);
            emailList.add(0, name);
            ansList.add(emailList);
        }

        return ansList;
    }

    public void dfs(
            int userIdx,
            Set<String> emails,
            Set<Integer> visited,
            Map<String, ArrayList<Integer>> emailToIdx,
            List<List<String>> accounts) {
        if (visited.contains(userIdx)) {
            return;
        }
        visited.add(userIdx);
        for (int i = 1; i < accounts.get(userIdx).size(); i++) {
            String email = accounts.get(userIdx).get(i);
            emails.add(email);
            for (int idx : emailToIdx.get(email)) {
                dfs(idx, emails, visited, emailToIdx, accounts);
            }
        }
    }
}
// @leet end
