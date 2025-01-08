import matplotlib.pyplot as plt
import numpy as np
a = [1,2,3,4,6,10]
print(plt.boxplot(a,notch=True))
print(plt.show())