
class Tire:
    def __init__(self, size: int):
        self.__size = size
        self.__pressure = 0
    def get_pressure(self):
        return self.__pressure
    def pump(self, psi: int):
        self.__pressure = psi
        
        
class Engie:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type
        self.__state = 'off'
    def start(self):
        self.__state = 'on'
    def stop(self):
        self.__state = 'off'
    def get_state(self):
        return self.__state

class Vehicle:
    def __init__(self, VIN: str, tire: Tire, engie: Engie):
        self.VIN = VIN
        self.tire = tire 
        self.engine = engie

city_tires = Tire(15)
off_road_tires = Tire(18)

electric_engine = Engie('electricity')
petrol_engine = Engie("petrol")

city_car = Vehicle('city_car_001', city_tires, electric_engine)
terrain_car = Vehicle('off-road-car_001', off_road_tires, petrol_engine)

city_car.tire.pump(10)
print(city_car.engine.start())
print(city_car.engine.stop())
print(city_car.engine.get_state())
print(city_car.tire.get_pressure())