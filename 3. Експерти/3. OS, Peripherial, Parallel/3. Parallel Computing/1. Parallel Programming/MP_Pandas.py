# Паралелна Обработка на Dataframe ot Pandas
# Всеки ред от dataframe-a представя катетите на един правоъгълен триъгълник
# Функцията hypotenuse(row) пресмята хипотенузата

import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
print(df.head())

def para_rows():
# Паралелизация по редове
    def hypotenuse(row):
        return round((row[1]**2 + row[2]**2)**0.5,2)

    with mp.Pool(4) as pool:
        result = pool.imap(hypotenuse, df.itertuples(name=False), chunksize=10)
    # imap служи итериране на итеративни променливи
    # itertuples прави от всеки ред итеративна редица
    # пример: да се разпечата всеки ред от df:
    # for row in df.itertuples():
    #     print(row)
        output = [x for x in result]

    print(output) #> [9.43, 5.83, 5.0, 5.66, 11.4]


# Паралелизация по колони

def para_cols():
    def sum_of_squares(column):
        return sum([i**2 for i in column[1]])

    with mp.Pool(2) as pool:
        result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
        output = [x for x in result]
    # алтернативен запис:
    # pool=mp.Pool(2)
    # with pool:
    #   result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
    #   output = [x for x in result]
    print(output) #> [163, 147]

# Пълна паралелизация на данните:
# Pandas Dataframe, NumPy Array, etc.
# Pathos следва методиката на multiprocessing:
# Pool > Map > Close > Join > Clear.
# Документация за pathos: https://github.com/uqfoundation/pathos

def para_full():
    from pathos.multiprocessing import ProcessingPool as Pool
    df = pd.DataFrame(np.random.randint(3, 10, size=[500, 2]))

    def func(df):
        return df.shape

    prc = mp.cpu_count()

    df_split = np.array_split(df, prc, axis=0)
    # df на равни порции, като броя на порциите са колкото е броя на процесите (prc)
    # разделянето се иззвършва по редове: axis=0

    # create the multiprocessing pool
    pool = Pool(prc)

    # process the DataFrame by mapping function to each df across the pool

    df_out = np.vstack(pool.map(func, df_split))
    # vstack обратно слепва резултата от паралелното прилагане на функцията към split-натия dataframe

    # close down the pool and join
    pool.close()
    pool.join()
    pool.clear()
    print(df_out)

