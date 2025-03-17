import threading

class TrafficLight:
    def __init__(self):
        self.lock = threading.Lock()
        self.green = 1  # green on roadA

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:


        thread = threading.Thread()

        self.lock.acquire()
        if self.green != roadId:
            self.green = roadId
            turnGreen()
        crossCar()
        self.lock.release()






    
        