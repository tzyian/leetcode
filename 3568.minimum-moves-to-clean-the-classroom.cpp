// @leet imports start
#include "debug.hpp"
using namespace std;
// @leet imports end

// @leet start
class Solution {
  private:
    struct State {
        int i = 0;
        int j = 0;
        int collected = 0;
        int energy = 0;
        int moves = 0;
    };

  public:
    int minMoves(vector<string>& classroom, int energy) {
        int n = classroom.size();
        int m = classroom[0].size();

        State start;

        int idx = 0;
        vector<int> litter_idx(n * m);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                char cell = classroom[i][j];
                if (cell == 'S') {
                    start = {i, j, 0, energy, 0};
                } else if (cell == 'L') {
                    litter_idx[i * m + j] = idx;
                    ++idx;
                }
            }
        }

        if (idx == 0) {
            return 0;
        }

        auto visited = vector(n, vector(m, vector<int>(1 << idx, -1)));
        visited[start.i][start.j][0] = energy;
        int DONE = (1 << idx) - 1;

        auto can_visit = [&](int i, int j, int energy) {
            bool in_range = (0 <= i && i < n && 0 <= j && j < m);
            bool have_energy = energy > 0; // energy to move to (ni, nj)
            return in_range && have_energy && classroom[i][j] != 'X';
        };
        auto should_visit = [&](int i, int j, int collected, int energy) {
            int e = visited[i][j][collected];
            return e == -1 || e < energy;
        };

        deque<State> frontier{start};
        vector<pair<int, int>> neighbours = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!frontier.empty()) {
            State s = std::move(frontier.front());
            frontier.pop_front();
            for (const auto& [di, dj] : neighbours) {
                int ni = s.i + di;
                int nj = s.j + dj;

                if (!can_visit(ni, nj, s.energy)) {
                    continue;
                }

                int coll = s.collected;
                int mov = s.moves + 1;
                int en = s.energy - 1;

                if (classroom[ni][nj] == 'L') {
                    coll |= 1 << litter_idx[ni * m + nj];
                } else if (classroom[ni][nj] == 'R') {
                    en = energy;
                }

                if (coll == DONE) {
                    return mov;
                }

                if (!should_visit(ni, nj, coll, en)) {
                    continue;
                }

                visited[ni][nj][coll] = en;
                frontier.push_back(State(ni, nj, coll, en, mov));
            }
        }

        return -1;
    }
};
// @leet end
int main() {
    Solution s;
    vector<string> vec = {"L.R.S.R.L"};
    int energy = 4;
    auto out = s.minMoves(vec, energy);
    debug(out);
}
