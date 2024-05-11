// https://leetcode.com/problems/largest-3-same-digit-number-in-string

func largestGoodInteger(num string) string {
	ans := ""
	for i := 0; i < len(num)-2; i++ {
		if num[i] == num[i+1] && num[i+1] == num[i+2] {
			str := num[i : i+3]
			if str > ans {
				ans = str
			}
		}
	}
	return ans
}
