import time
from threading import Thread


def hello(n):
    while n > 0:
        print(f'Hello {n}')
        n -= 1
        time.sleep(2)


t = Thread(target=hello, args=(100, ))
t.start()

if t.is_alive():
    print(f'Thread {t.getName()} is live')
else:
    print(f'RIP thread {t.getName()}')