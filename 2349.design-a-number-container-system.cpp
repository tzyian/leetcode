// @leet start
#include <set>
#include <unordered_map>

using std::set;
using std::unordered_map;

class NumberContainers {
  private:
    // number to sorted_list of container_ids
    unordered_map<int, set<int>> ordered_lists;
    unordered_map<int, int> containers;

  public:
    NumberContainers() {}

    void change(int index, int number) {
        auto it = containers.find(index);
        if (containers.contains(index)) {
            auto& prev_num = containers[index];
            ordered_lists[prev_num].erase(index);
        }
        containers[index] = number;
        ordered_lists[number].insert(index);
    }

    int find(int number) {
        if (!ordered_lists[number].empty()) {
            // O(logn) of popping treeset to get the smallest index
            return *ordered_lists[number].begin();
        }
        return -1;
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
// @leet end
