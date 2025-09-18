def lis(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    ans = 1
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])

    return ans


print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4  ([2,3,7,101])


def tallest_stack(boxes: list[list[int]]) -> int:
    boxes.sort()  # sort by (w, d, h)
    n = len(boxes)
    dp = [0] * n
    for i in range(n):
        wi, di, hi = boxes[i]
        dp[i] = hi
        for j in range(i):
            wj, dj, hj = boxes[j]
            if wj < wi and dj < di and hj < hi:
                dp[i] = max(dp[i], dp[j] + hi)
    return max(dp, default=0)


print(tallest_stack([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))  # 6
print(tallest_stack([[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]))  # 10
