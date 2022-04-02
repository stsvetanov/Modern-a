import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 4), pd.date_range('1/1/2000', periods=1000))
df = df.cumsum()
plt.figure()
df.plot()