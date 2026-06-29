import pandas as pd
import matplotlib.pyplot as plt

cat = pd.read_csv("../CSVs/cat_breeds_clean.csv", sep=';')

a = cat.groupby("Body_length")["Weight"].mean()

print(a)

plt.bar(a.index, a.values, width=0.5)
plt.show()