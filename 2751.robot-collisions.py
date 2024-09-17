# @leet start
from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        stack = []
        ans = []
        n = len(positions)
        # Actually you can just do indices.sort(lambda x: positions[x])
        structs = sorted(zip(positions, healths, directions, range(n)))

        for i, (pos, hp, dir, idx) in enumerate(structs):
            if not stack and directions == "L":
                # just go left all the way
                ans.append([idx, hp, dir])
            elif dir == "R":
                stack.append([idx, hp, dir])
            else:  # dir == "L":
                # there are robots still going right
                while stack:
                    prev_idx, prev_hp, prev_dir = stack[-1]
                    if prev_dir == "L":
                        break
                    elif prev_hp < hp:
                        stack.pop()
                        hp -= 1  # deplete current hp, try again
                    elif prev_hp == hp:
                        stack.pop()  # both robots die
                        hp = 0
                        break
                    else:
                        stack[-1][1] -= 1  # deplete prev robot's hp
                        hp = 0
                        break
                if hp > 0:
                    stack.append([idx, hp, dir])

        ans.extend(stack)
        ans.sort()
        return [x for _, x, _ in ans]


# @leet end

pos = [13, 3]
hp = [17, 2]
dir = "LR"

# pos = [3, 13]
# hp = [2, 17]
# dir = "RL"
x = Solution().survivedRobotsHealths(pos, hp, dir)
print(x)
