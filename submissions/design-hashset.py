// https://leetcode.com/problems/design-hashset

# copied from the answer.
# the key part to note is how to implement the hashcode

class MyHashSet: 
    def hashcode(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5
        # h(K) = (aK mod 2**w)/2**(w-m)
        # a = 1031237, a prime
        # m is length in bits of output i.e. the array is 2**15
        # w = any value, here 20
        # s % (2^t) = s & (1<<t) - 1
        # the 5 is the specific value, which is the divide by 2**(w-m)

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]
        # 1 << 15 (i.e. 1 bitshift 15 times)is the same as 2**15,
        # faster to bitshift than exponent

    def add(self, key: int) -> None:
        k = self.hashcode(key)
        if key not in self.arr[k]:
            self.arr[k].append(key)

    def remove(self, key: int) -> None:
        k = self.hashcode(key)
        if key in self.arr[k]:
            self.arr[k].remove(key)

    def contains(self, key: int) -> bool:
        k = self.hashcode(key)
        return key in self.arr[k]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)