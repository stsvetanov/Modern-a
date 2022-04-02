import pandas as pd
from sklearn.datasets import load_boston

dataset = load_boston()

boston = pd.DataFrame(dataset.data, columns=dataset.feature_names)

boston['target'] = dataset.target

print(boston.head(10))

