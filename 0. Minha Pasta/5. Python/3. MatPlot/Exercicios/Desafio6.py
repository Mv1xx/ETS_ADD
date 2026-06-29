import pandas as pd
import matplotlib.pyplot as plt

casa = pd.read_csv("../CSVs/california_housing_train.csv")

plt.hist(casa['median_house_value'])
plt.show()