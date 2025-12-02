// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class SnapshotArray {
  private:
    int snap_id = 0;
    vector<map<int, int>> arr;

  public:
    SnapshotArray(int length) : arr(length) {}

    void set(int index, int val) { arr[index][snap_id] = val; }

    int snap() { return snap_id++; }

    int get(int index, int snap_id) {
        // snaps = [0, 3]
        // to query at snap 2, if you take lower bound, you find 3
        // when you want snap 0
        auto it = arr[index].upper_bound(snap_id);
        if (it == arr[index].begin()) {
            return 0;
        }
        --it;
        return it->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
// @leet end
