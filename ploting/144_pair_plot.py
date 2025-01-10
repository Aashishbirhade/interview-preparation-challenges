import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    'Feature1': [10, 30, 20, 44, 50, 23, 5, 52, 1],
    'Feature2': [5, 12, 15, 20, 22, 30, 40, 50, 60],
    'Feature3': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})
print(sns.pairplot(data))
print(plt.show())
