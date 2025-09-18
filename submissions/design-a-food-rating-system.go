// https://leetcode.com/problems/design-a-food-rating-system
package submissions

import (
	"cmp"
	"container/heap"
	"log"
)

// CustomItem interface represents an item in the priority queue.
type CustomItem[T cmp.Ordered] interface {
	Value() string
	Priority() T
	Index() int
	SetPriority(T)
	SetIndex(int)
}

// CustomPriorityQueue implements a priority queue using a min-heap.
type CustomPriorityQueue[T cmp.Ordered] struct {
	ItemsMap map[string]CustomItem[T]
	Items    []CustomItem[T]
	Compare  func(i, j CustomItem[T]) bool
}

func (pq *CustomPriorityQueue[T]) Len() int { return len(pq.Items) }

// Less implements sort interface. Do not use directly.
func (pq *CustomPriorityQueue[T]) Less(i, j int) bool {
	return pq.Compare(pq.Items[i], pq.Items[j])
}

// Swap implements sort interface. Do not use directly
func (pq *CustomPriorityQueue[T]) Swap(i, j int) {
	pq.Items[i], pq.Items[j] = pq.Items[j], pq.Items[i]
	pq.Items[i].SetIndex(i)
	pq.Items[j].SetIndex(j)
}

// Push implements heap interface. Do not use directly. Use heap.Push instead
func (pq *CustomPriorityQueue[T]) Push(x interface{}) {
	item := x.(CustomItem[T])
	item.SetIndex(len(pq.Items))
	pq.Items = append(pq.Items, item)
	pq.ItemsMap[item.Value()] = item
}

// Pop implements heap interface. Do not use directly. Use heap.Pop instead
func (pq *CustomPriorityQueue[T]) Pop() interface{} {
	old := pq.Items
	n := len(old)
	item := old[n-1]
	item.SetIndex(-1)
	pq.Items = old[0 : n-1]
	delete(pq.ItemsMap, item.Value())
	return item
}

// Peek returns the item with the highest priority
func (pq *CustomPriorityQueue[T]) Peek() CustomItem[T] {
	if pq.Len() == 0 {
		log.Fatal("Heap is empty")
	}
	return pq.Items[0]
}

// Insert convenience function
// pq.Insert(item) is equivalent to heap.Push(pq, item)
// except it panics if item already exists
func (pq *CustomPriorityQueue[T]) Insert(item CustomItem[T]) {
	if _, exists := pq.ItemsMap[item.Value()]; exists {
		log.Fatal("CustomItem already exists in priority queue: ", item)
	} else {
		pq.ItemsMap[item.Value()] = item
		heap.Push(pq, item)
	}
}

// InsertOrUpdate inserts if not exists, or updates if exists
func (pq *CustomPriorityQueue[T]) InsertOrUpdate(item CustomItem[T]) {
	if oldItem, exists := pq.ItemsMap[item.Value()]; exists {
		pq.update(oldItem, item.Priority())
	} else {
		pq.ItemsMap[item.Value()] = item
		heap.Push(pq, item)
	}
}

// Update the priority of an existing item
func (pq *CustomPriorityQueue[T]) Update(value string, priority T) {
	if item, exists := pq.ItemsMap[value]; exists {
		pq.update(item, priority)
	} else {
		log.Fatal("CustomItem does not exist in priority queue: ", value)
	}
}

// update modifies the priority of an item in the queue. Do not use directly
func (pq *CustomPriorityQueue[T]) update(item CustomItem[T], priority T) {
	item.SetPriority(priority)
	heap.Fix(pq, item.Index())
}

// Remove a value from the heap
func (pq *CustomPriorityQueue[T]) Remove(value string) {
	if item, exists := pq.ItemsMap[value]; exists {
		delete(pq.ItemsMap, value)
		heap.Remove(pq, item.Index())
	} else {
		log.Fatal("CustomItem does not exist in priority queue: ", value)
	}
}

// FindItem finds an item by value
func (pq *CustomPriorityQueue[T]) FindItem(value string) (CustomItem[T], bool) {
	item, exists := pq.ItemsMap[value]
	return item, exists
}

func MakeCustomIntPriorityQueue() *CustomPriorityQueue[int] {
	pq := &CustomPriorityQueue[int]{
		ItemsMap: make(map[string]CustomItem[int]),
		Items:    make([]CustomItem[int], 0),
		Compare:  func(i, j CustomItem[int]) bool { return i.Priority() < j.Priority() },
	}
	return pq
}

func MakeCustomFloatPriorityQueue() *CustomPriorityQueue[float64] {
	pq := &CustomPriorityQueue[float64]{
		ItemsMap: make(map[string]CustomItem[float64]),
		Items:    make([]CustomItem[float64], 0),
		Compare:  func(i, j CustomItem[float64]) bool { return i.Priority() < j.Priority() },
	}
	return pq
}

func compare(i CustomItem[int], j CustomItem[int]) bool {
	if i.Priority() == j.Priority() {
		return i.Value() < j.Value()
	}
	return i.Priority() > j.Priority()
}

type FoodRatings struct {
	CuisinesMap map[string]*CustomPriorityQueue[int]
	FoodMap     map[string]*Food
}

type Food struct {
	Name     string
	Cuisine  string
	Rating   int
	IndexVal int
}

func (food *Food) Value() string            { return food.Name }
func (food *Food) Priority() int            { return food.Rating }
func (food *Food) Index() int               { return food.IndexVal }
func (food *Food) SetPriority(priority int) { food.Rating = priority }
func (food *Food) SetIndex(index int)       { food.IndexVal = index }

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	cuisinesMap := make(map[string]*CustomPriorityQueue[int])
	foodMap := make(map[string]*Food)

	for i := 0; i < len(foods); i++ {
		pq, ok := cuisinesMap[cuisines[i]]
		if !ok {
			cuisinesMap[cuisines[i]] = &CustomPriorityQueue[int]{
				ItemsMap: make(map[string]CustomItem[int]),
				Items:    make([]CustomItem[int], 0),
				Compare:  compare,
			}
		}
		pq = cuisinesMap[cuisines[i]]
		food := &Food{Name: foods[i], Rating: ratings[i], Cuisine: cuisines[i]}
		pq.Insert(food)
		foodMap[foods[i]] = food
	}
	return FoodRatings{CuisinesMap: cuisinesMap, FoodMap: foodMap}
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	foodItem, ok := this.FoodMap[food]
	if !ok {
		log.Fatal("Food does not exist: ", food)
	}
	foodItem.SetPriority(newRating)
	cuisinePQ := this.CuisinesMap[foodItem.Cuisine]
	cuisinePQ.InsertOrUpdate(foodItem)
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	cuisinePQ := this.CuisinesMap[cuisine]
	return cuisinePQ.Peek().Value()
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
 */
