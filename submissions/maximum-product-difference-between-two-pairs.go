// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

func maxProductDifference(nums []int) int {
    maxArr := [3]int{0,0,0}
    maxVals := maxArr[:]
    minArr := [3]int{9999,9999,9999}
    minVals := minArr[:]

    for _, ele := range nums {

        maxVals[0] = ele
        minVals[2] = ele
        sort.Ints(maxVals)
        sort.Ints(minVals)
    }
    return maxVals[2] * maxVals[1] - minVals[0] * minVals[1]
}