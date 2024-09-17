// @leet start
#include <string>
#include <map>
#include <unordered_map>
using std::string;

class TimeMap {
public:
    // Actually timestamp will be strictly increasing so unoredered_map<int, vector<string> + bin search is sufficient
    std::unordered_map<string, std::map<int, string>> m;

    TimeMap() {
        this->m = {};
        
    }
    
    void set(string key, string value, int timestamp) {
        this->m[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        const auto& map = this->m[key];
        // Upper bound returns iterator with key strictly greater than arg if it exists, else returns end()
        auto it = map.upper_bound(timestamp);

        // Map is empty, so end() == begin()
        if (it == map.begin()) {
            return "";
        }

        --it;

        // Not necessary to check `it->first > timestamp` because upper_bound gives the very first value that is strictly greater than
        // Can do `prev(it)`
        return it->second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
// @leet end
