// https://leetcode.com/problems/remove-duplicates-from-sorted-array

func removeDuplicates(nums []int) int {
    // in place, linear TC
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    prev := -101 // arbitrary value below constraint
    checked := 0
    for i := 0; i < n; i++ {
        // if prev < nums[i] {
        //     prev = nums[i]
        //     checked += 1
        //     continue
        // }

        for i < n && prev >= nums[i]  {
            i++
        }
        if i < n {
            prev = nums[i]
            nums[checked], nums[i] = nums[i], nums[checked]
            checked++
        }
    }
    
    return checked
    
}