// https://leetcode.com/problems/longest-increasing-subsequence

// Patience algorithm
// TC is \sum_{i=1}^{n} \log(i) = log(n!) ≈ nlogn by Stirling's approx
func lengthOfLIS(nums []int) int {
    n := len(nums)
    subseq := make([]int, 1)
    subseq[0] = nums[0]

    for i := 1; i < n; i++ {
        if nums[i] == subseq[len(subseq)-1] {
            // dupes technically will be accounted for by binary search
            // so this case is not strictly necessary
            // note that preprocessing will not work eg 4 3 4
            continue
        } else if nums[i] > subseq[len(subseq)-1] {
            subseq = append(subseq, nums[i])
        } else {
            j := binarySearch(subseq, nums[i])
            subseq[j] = nums[i]
        }
    }
    return len(subseq)
}

// find smallest i where subseq[i] >= x
func binarySearch(subseq []int, x int) int {
    l := 0
    h := len(subseq) - 1
    for l < h {
        m := l + (h - l) / 2
        if subseq[m] == x {
            return m
        } else if subseq[m] < x {
            l = m + 1
        } else {
            h = m
        }
    }
    return l
}