// https://leetcode.com/problems/majority-element

func majorityElement(nums []int) int {
    maj := 0
    count := 0
    for _, ele := range nums {
        if count == 0 {
            maj = ele
            count = 1
        } else if ele == maj {
            count++
        } else {
            count--
        }
    }

    return maj
}