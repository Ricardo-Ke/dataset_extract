import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

test_size_all_1 = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
test_size_all = [0.3]

for test_size in test_size_all:
    x, y = np.sp
    x, y = train_test_split(x, y, test_size=test_size, random_state=42)
