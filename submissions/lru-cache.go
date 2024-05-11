// https://leetcode.com/problems/lru-cache

import "fmt"

type LRUNode struct {
	Key  int
	Val  int
	Prev *LRUNode
	Next *LRUNode
}

type LRUCache struct {
	NodeMap     map[int]*LRUNode
	Size        int
	Capacity    int
	LRUSentinel *LRUNode // the head
	MRUSentinel *LRUNode // the tail
}

func Constructor(capacity int) LRUCache {
	cache := LRUCache{
		NodeMap:     make(map[int]*LRUNode, capacity),
		Size:        0,
		Capacity:    capacity,
		LRUSentinel: &LRUNode{},
		MRUSentinel: &LRUNode{},
	}
	cache.LRUSentinel.Next = cache.MRUSentinel
	cache.MRUSentinel.Prev = cache.LRUSentinel
	return cache
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.NodeMap[key]; ok {
		this.updateNodeToMRU(node)
		return node.Val
	}
	return -1

}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.NodeMap[key]; ok {
		node.Val = value
		this.updateNodeToMRU(node)
		return
	}

	newNode := &LRUNode{
		Key:  key,
		Val:  value,
		Prev: nil,
		Next: nil,
	}
	this.NodeMap[key] = newNode

	if this.Size >= this.Capacity {
		this.removeLRU()

	}

	this.updateNodeToMRU(newNode)
	this.Size++

}

func (this *LRUCache) removeLRU() {
	if this.LRUSentinel.Next == this.MRUSentinel {
		return
	}
	node := this.LRUSentinel.Next

	this.LRUSentinel.Next = node.Next
	node.Next.Prev = this.LRUSentinel

	delete(this.NodeMap, node.Key)
	this.Size--

}

func (this *LRUCache) updateNodeToMRU(node *LRUNode) {
	// update old Prev
	if node.Prev != nil {
		node.Prev.Next = node.Next
	}
	// update old Next
	if node.Next != nil {
		node.Next.Prev = node.Prev
	}
	// update Node
	node.Prev = this.MRUSentinel.Prev
	node.Next = this.MRUSentinel

	// update Sentinel.Prev
	this.MRUSentinel.Prev.Next = node

	// update Sentinel
	this.MRUSentinel.Prev = node

}