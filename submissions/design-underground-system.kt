// https://leetcode.com/problems/design-underground-system

class UndergroundSystem() {
    private val stationList = mutableMapOf<String, Station>() // stationName to Station()
    private val custList = mutableMapOf<Int, Customer>() // id to Customer()


    fun checkIn(id: Int, stationName: String, t: Int) {
        val startStation = stationList.getOrPut(stationName) { Station(stationName) }
        custList[id] = Customer(id, startStation, t)
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        // val endStation = stationList[stationName]!!
        val endStation = stationList.getOrPut(stationName) { Station(stationName) }
        val cust = custList.getValue(id)
        endStation.updateStartStation(cust, endStation, t)

        custList.remove(id)


    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        val start: Station = stationList[startStation]!!
        val end: Station= stationList[endStation]!!
        return start.getAveTime(end)
    }

    class Station(val name: String) {
        // map of EndStation to Pair<total time, count>
        private val endStations = mutableMapOf<Station, Pair<Int, Int>>()

        fun updateStartStation(cust: Customer, endStation: Station, endTime: Int) {
            val timeTaken = cust.timeTaken(endTime)
            val startStation = cust.startStation


            startStation.endStations[endStation] = startStation.endStations
                .getOrDefault(endStation, 0 to 0)
                .let { (totalTime, count) -> (totalTime + timeTaken) to (count + 1)}

//            if (startStation.endStations[endStation] == null) {
//                startStation.endStations[endStation] = Pair(timeTaken, 1)
//            } else {
//                val (time, count) = startStation.endStations[endStation]!!
//                startStation.endStations[endStation] = Pair(time + timeTaken, count + 1)
//            }

        }

        fun getAveTime(end: Station): Double {
            val (totalTime, count) = endStations[end]!!
            return totalTime.toDouble() / count.toDouble()
        }

    }


    class Customer(
        id: Int,
        val startStation: Station,
        val startTime: Int
    ) {
        fun timeTaken(endTime: Int): Int {
            return endTime - startTime
        }

    }


}



/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */