import pandas as pd
import matplotlib.pyplot as plt

casas = pd.read_csv("../CSVs/california_housing_train.csv")

plt.scatter(casas['longitude'], casas['latitude'], c = casas['median_house_value'])
plt.show()