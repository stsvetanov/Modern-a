import time
from threading import Thread


class HelloThread:
    def __init__(self):
        self._live = True

    def terminate(self):
        self._live = False

    def start(self, n):
        while self._live and n > 0:
            print(f'Hello {n}')
            n -= 1
            time.sleep(2)


hi = HelloThread()
t = Thread(target=hi.start, args=(100, ))
t.start()
time.sleep(5)
hi.terminate()
t.join()