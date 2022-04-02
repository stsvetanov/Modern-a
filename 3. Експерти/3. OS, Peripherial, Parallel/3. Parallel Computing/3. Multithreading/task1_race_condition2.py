import logging
import multiprocessing
import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self):
        logging.info("Thread %s: starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    np = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=np)
    database = FakeDatabase()
    pool.apply(database.update)
    logging.info("Testing update. Starting value is %d.", database.value)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     for index in range(2):
    #         executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)