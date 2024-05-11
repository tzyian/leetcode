// https://leetcode.com/problems/snapshot-array

class SnapshotArray(length: Int) {
    private val arr: Array<TreeMap<Int, Int>> = Array(length) { TreeMap<Int, Int>().apply{ put (0,0) } }
    private var snapId = 0

    fun set(index: Int, `val`: Int) {
        this.arr[index][snapId] = `val`
    }

    fun snap(): Int {
        return this.snapId++
    }

    fun get(index: Int, snap_id: Int): Int {
        val key = this.arr[index].floorKey(snap_id)
        return this.arr[index][key]!!
    }

}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = SnapshotArray(length)
 * obj.set(index,`val`)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */