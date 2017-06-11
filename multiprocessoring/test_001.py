from multiprocessing import Process
import time


class Timer:
    def __init__(self):
        self.p_time = time.process_time()
        self.t_time = time.perf_counter()

    def start(self):
        self.p_time = time.process_time()
        self.t_time = time.perf_counter()

    def stop(self, title):
        print(title,
              time.process_time() - self.p_time,
              time.perf_counter() - self.t_time)


def f1(name):
    timer1 = Timer()
    timer1.start()

    x = 0
    y = 0
    for i in range(20):
        for j in range(100000):
            y = i * i + y // 7 + j % 3
        x += y
        print('-hello', name, i, x)
        # time.sleep(0.001)

    timer1.stop('Time in loop #1')


def f2(name):
    timer2 = Timer()
    timer2.start()

    x = 0
    y = 0
    for i in range(20):
        for j in range(100000):
            y = i * i + y // 7 + j % 3
        x += y
        print('+hello', name, i, x)
        # time.sleep(0.001)

    timer2.stop('Time in loop #2')

if __name__ == '__main__':
    timer = Timer()
    timer.start()

    p1 = Process(target=f1, args=('bob1',))
    p1.start()

    timer.stop('Time to start process #1')

    timer.start()

    p2 = Process(target=f2, args=('bob2',))
    p2.start()

    timer.stop('Time to start process #2')

    time.sleep(10)
    p1.terminate()
    p2.terminate()
