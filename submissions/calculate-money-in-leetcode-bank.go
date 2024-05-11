// https://leetcode.com/problems/calculate-money-in-leetcode-bank

func totalMoney(n int) int {
    weeks := n / 7
    sums := weeks * (2 * 28 + 7 * (weeks-1)) / 2
    for i := 0; i < n % 7; i++ {
      sums += i + 1 + weeks
    }
    return sums

}