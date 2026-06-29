import matplotlib.pyplot as plt
import pandas as pd

gols = pd.read_csv("../CSVs/gols_pr.csv", sep=",")

plt.plot(gols['ano'][gols['clube'] == 'parana'], gols['gols_pro'][gols['clube'] == 'parana'], marker = "o", label = "parana")
plt.plot(gols['ano'][gols['clube'] == 'coritiba'], gols['gols_pro'][gols['clube'] == 'coritiba'], marker = "o", label = "coritiba")
plt.plot(gols['ano'][gols['clube'] == 'athletico-pr'], gols['gols_pro'][gols['clube'] == 'athletico-pr'], marker = "o", label = "athletico-pr")
plt.legend()
plt.show()


