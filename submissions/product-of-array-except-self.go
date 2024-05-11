// https://leetcode.com/problems/product-of-array-except-self

func productExceptSelf(nums []int) []int {
    n := len(nums)

    ans := make([]int, n)
    ans[0], ans[n - 1] = 1, 1
    
    // prefix product for every number except first
    prefixProduct := 1
    for i := 1; i < n; i++ {
        prefixProduct *= nums[i - 1]
        ans[i] = prefixProduct
    }

    // suffix product for every number except last
    suffixProduct := 1
    for i := n - 2; i >= 0; i-- {
        suffixProduct *= nums[i + 1]
        ans[i] *= suffixProduct
    }

    return ans


}