// https://leetcode.com/problems/product-of-array-except-self

func productExceptSelf(nums []int) []int {
    n := len(nums)
    prefixSlice := make([]int, n)
    suffixSlice := make([]int, n)
    
    prefixProduct := 1
    suffixProduct := 1
    for i := 0; i < n; i++ {
        prefixProduct *= nums[i]
        suffixProduct *= nums[n - 1 - i]
        prefixSlice[i] = prefixProduct
        suffixSlice[n - 1 - i] =  suffixProduct
    }

    ans := make([]int, n)
    for i := 0; i < n; i++ {
        prefix, suffix := 1, 1
        if i != 0 {
            prefix = prefixSlice[i - 1]
        }
        if i != n - 1 {
            suffix = suffixSlice[i + 1]
        }
        ans[i] = prefix * suffix
    }

    return ans


}