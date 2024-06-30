import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill
        self.enemies = 100


    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 1
        while self.enemies > 0:
            print(f"{self.name}, сражается {days} день(дня)... осталось {self.enemies} воинов.")
            self.enemies -= self.skill
            days += 1
            time.sleep(1)
        print(f"{self.name} одержал победу ")


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)    # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()