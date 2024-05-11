// https://leetcode.com/problems/insert-delete-getrandom-o1

import "math/rand"

type RandomizedSet struct {
    set map[int]int
    list []int
}


func Constructor() RandomizedSet {
    return RandomizedSet{
        make(map[int]int),
        make([]int, 0),
    }
    
}


func (this *RandomizedSet) Insert(val int) bool {
    if _, ok := this.set[val]; ok {
        return false
    }

    this.list = append(this.list, val)
    this.set[val] = len(this.list)-1
    return true
    
}


func (this *RandomizedSet) Remove(val int) bool {
    n := len(this.list)
    idx, ok := this.set[val]
    if !ok {
        return false
    }
    if idx != n-1 {
        this.list[idx], this.list[n-1] = this.list[n-1], this.list[idx]
        this.set[this.list[idx]] = idx
    }
    this.list = this.list[:n-1]
    delete(this.set, val)
    return true
    
}


func (this *RandomizedSet) GetRandom() int {
    n := len(this.list)
    idx := rand.Intn(n)
    return this.list[idx]

    
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */