import math


def SampleSD(sample):
    size = len(sample)
    average = sum(sample)/size
    # sumSD = 0
    # for element in sample:
    #     sumSD += math.fabs(element - average)**2
    SD = math.sqrt(1/(size - 1) * sum([math.fabs(element - average)**2 for element in sample ]))
    return SD


sample = [1.0, 3.0, 5.0, 7.0]
print(SampleSD(sample))