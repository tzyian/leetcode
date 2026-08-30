#include <bits/stdc++.h>

using namespace std;

unordered_map<int, int> uf;
int find(int x) {
    // just reusing the it using try_emplace
    auto [it, inserted] = uf.try_emplace(x, x);
    if (it->second != x) {
        it->second = find(it->second);
    }
    return it->second;
}

void unite(int x, int y) {
    int px = find(x);
    int py = find(y);
    if (px != py) {
        uf[px] = py;
    }
}
