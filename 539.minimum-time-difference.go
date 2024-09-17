package leetcode

// @leet start
import (
	"math"
	"slices"
	"strconv"
)

type Time struct {
	hours   int
	minutes int
}

func findMinDifference(timePoints []string) int {
	times := make([]Time, 0, len(timePoints)+1)
	minDiff := math.MaxInt

	for _, tp := range timePoints {
		hr, _ := strconv.Atoi(tp[:2])
		minute, _ := strconv.Atoi(tp[3:])
		times = append(times, Time{hr, minute})
	}

	slices.SortFunc(times, func(i, j Time) int {
		if i.hours == j.hours {
			if i.minutes < j.minutes {
				return -1
			} else if i.minutes == j.minutes {
				return 0
			}
			return 1
		} else if i.hours < j.hours {
			return -1
		}
		return 1
	})

	first := times[0] // copy first value
	first.hours += 24
	times = append(times, first)

	for i := 1; i < len(times); i++ {
		minDiff = min(timeDiff(times[i], times[i-1]), minDiff)
	}

	return minDiff

}

// timeDiff has t1 > t2
func timeDiff(larger, smaller Time) int {
	if larger.minutes >= smaller.minutes {
		// 10:45 - 9:30
		return 60*(larger.hours-smaller.hours) + (larger.minutes - smaller.minutes)
	}

	// 12:30 - 10:40
	// 24:00 - 23:59
	minuteDiff := larger.minutes + 60 - smaller.minutes
	hourDiff := larger.hours - 1 - smaller.hours
	return 60*hourDiff + minuteDiff
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end

