// https://leetcode.com/problems/design-parking-system

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_lots = Big(big)
        self.medium_lots = Medium(medium)
        self.small_lots = Small(small)
        
    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                return self.big_lots.addCar()
            case 2:
                return self.medium_lots.addCar()
            case 3:
                return self.small_lots.addCar()

class Carpark:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filled = 0
    def addCar(self):
        if self.filled < self.capacity:
            self.filled += 1
            return True
        return False

class Big(Carpark):
    pass

class Medium(Carpark):
    pass

class Small(Carpark):
    pass




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)