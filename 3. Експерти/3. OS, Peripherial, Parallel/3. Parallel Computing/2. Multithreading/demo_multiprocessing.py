import multiprocessing
import threading


def task1():
    print(f"Hello from thread {threading.current_thread().name}")


if __name__ == "__main__":

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    number_of_cpus = multiprocessing.cpu_count()
    for i in range(1, number_of_cpus + 1):
        thread_name = f't{i}'
        thread_name = threading.Thread(target=task1, name=thread_name)
        thread_name.start()