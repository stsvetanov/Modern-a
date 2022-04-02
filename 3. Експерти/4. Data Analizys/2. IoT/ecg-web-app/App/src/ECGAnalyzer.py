import heartpy as hp
import numpy as np
import sys

class ECGAnalyzer:
    SAMPLE_RATE = 100

    def __init__(self):
        self.__ecg_data = []
    
    def appendData(self, value):
        self.__ecg_data.append(value)

    def analyzeData(self):
        _ , measurements = hp.process(np.array(self.__ecg_data), self.SAMPLE_RATE)
        return measurements
    
    def getSamples(self):
        return len(self.__ecg_data)

