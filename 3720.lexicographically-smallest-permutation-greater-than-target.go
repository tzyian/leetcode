package leetcode

// @leet start

func lexGreaterPermutation(s string, target string) string {
	// N = len(str), N = len(target)
	// Case 1: k == M < N
	// prefix = target, fill remaining
	// Case 2: need to diverge before
	// backtrack
	const MAX_ALPHABETS = 26

	n := len(s)
	m := len(target)

	freqs := make([]int, MAX_ALPHABETS)
	for _, c := range s {
		freqs[toInt(c)]++
	}

	ans := make([]rune, 0, n)
	k := 0

	fillRemaining := func(str []rune) string {
		for i := range freqs {
			for freqs[i] > 0 {
				str = append(str, toRune(i))
				freqs[i]--
			}
		}
		return string(str)
	}

	greaterThan := func(c rune) int {
		idx := toInt(c)
		for i := idx + 1; i < MAX_ALPHABETS; i++ {
			if freqs[i] > 0 {
				return i
			}
		}
		return -1
	}

	// form prefix
	for i := range min(n, m) {
		c := rune(target[i])
		if freqs[toInt(c)] > 0 {
			freqs[toInt(c)]--
			ans = append(ans, c)
			k++
		} else {
			break
		}
	}

	// Case 1
	if k == m && n < m {
		return fillRemaining(ans)
	}

	// S == T, we put last char back under consideration
	if k == n {
		lastChar := ans[len(ans)-1]
		ans = ans[:len(ans)-1]
		freqs[toInt(lastChar)]++
		k--
		// if S == T, we must turn k back into the next char under consideration
		// 0 1 2 3 _    but _ is out-of-idx
		// a b c d
		// if k = 4, but S == T, we decr k to 3

	}

	// if prefixLen = 3, 3 is also the idx of the next char under consideration
	// 0 1 2 3
	//       ^   this is now the char under consideration
	// a b c _   ans
	//           we try to find a greater than _

	// Case 2
	// we already know backtracking is required immediately
	// k is the index of the char under consideration
	// i.e. for 0123_
	for i := k; i >= 0; i-- {
		nextGreater := greaterThan(rune(target[i]))
		if nextGreater >= 0 {
			ans = append(ans, toRune(nextGreater))
			freqs[nextGreater]--
			return fillRemaining(ans)
		}

		if i > 0 {
			lastChar := ans[len(ans)-1]
			ans = ans[:len(ans)-1]
			freqs[toInt(lastChar)]++
		}
	}

	return ""
}

func toRune(s int) rune {
	return rune(s + 'a')
}

func toInt(c rune) int {
	return int(c) - int('a')
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @leet end
