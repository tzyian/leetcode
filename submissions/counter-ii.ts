// https://leetcode.com/problems/counter-ii

type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    const reset = init
    return {
        increment: () => ++init,
        decrement: () => --init,
        reset: () => init = reset
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */