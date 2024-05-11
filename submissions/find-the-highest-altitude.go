// https://leetcode.com/problems/find-the-highest-altitude

func largestAltitude(gain []int) int {
    max := 0
    curr := 0
    for _, element := range gain {
        curr += element
        if curr > max {
            max = curr
        }
    }
    return max
}