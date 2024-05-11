// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

package main

import (
	"fmt"
)


// TO REDO
func strStr(haystack, needle string) int {
	n := len(haystack)
	m := len(needle)

	if n < m {
		return -1
	}

	base := 256
	mod := 1000000007

	needleHash, basePower := newHash(needle, base, mod)
	haystackHash, _ := newHash(haystack[:m], base, mod)

	for i := 0; i <= n-m; i++ {
		if haystackHash == needleHash && haystack[i:i+m] == needle {
			return i 
		}

		if i+m < n {
			haystackHash = updateHash(haystackHash, haystack[i], haystack[i+m], base, basePower, mod)
			if haystackHash < 0 {
				haystackHash += mod // Ensure the hash value is non-negative
			}
		}
	}

	return -1
}


func newHash(str string, base, mod int) (int, int) {
	hashValue := 0
	basePower := 1

	for _, char := range str {
		basePower = (basePower * base) % mod
		hashValue = (hashValue*base + int(char)) % mod
	}

	return hashValue, basePower
}

func updateHash(oldHash int, oldChar, newChar byte, base, basePower, mod int) int {
	return (oldHash*base - int(oldChar)*basePower + int(newChar)) % mod
}
