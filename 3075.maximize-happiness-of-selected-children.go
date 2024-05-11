package local

// @leet start

import (
	"fmt"
	"math/rand"
	"sort"
)

func maximumHappinessSum(happiness []int, k int) int64 {
	n := len(happiness)
	if n == 0 {
		return 0
	}
	quickselect(happiness, 0, n-1, n-k)
	fmt.Println(happiness)

	maxK := happiness[n-k:]
	sort.Ints(maxK)
	fmt.Println(maxK)

	total := 0
	for i := 0; i < k; i++ {
		if maxK[k-i-1] > i {
			total += maxK[k-i-1] - i
		} else {
			break
		}
	}
	return int64(total)

}

func quickselect(arr []int, left, right, k int) int {
	if left > right {
		panic("Left > right")
	}
	prePivotIndex, postPivotIndex := threeWayPartition(arr, left, right)
	if prePivotIndex <= k && k <= postPivotIndex {
		return k
	} else if k < prePivotIndex {
		return quickselect(arr, left, prePivotIndex, k)
	} else {
		return quickselect(arr, postPivotIndex+1, right, k)
	}
}

func threeWayPartition(arr []int, low, high int) (int, int) {
	pIndex := rand.Intn(high-low+1) + low
	pivot := arr[pIndex]

	// Initialize variables for partitioning
	i := low
	mid := low
	j := high

	for mid <= j {
		if arr[mid] < pivot {
			swap(arr, mid, i)
			i++
			mid++
		} else if arr[mid] == pivot {
			mid++
		} else {
			swap(arr, mid, j)
			j--
		}
	}

	// Return indices of partitioned elements
	return i, j
}

func swap(arr []int, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

// @leet end

