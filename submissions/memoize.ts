// https://leetcode.com/problems/memoize

type Fn = (...params: any) => any


function memoize(fn: Fn): Fn {
    const dict = new Map()
    return function(...args) {
        const key = JSON.stringify(args)
        if (dict.has(key)) {
            return dict.get(key)
        }
        const res = fn(...args)
        dict.set(key, res)
        return res
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(
     function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */