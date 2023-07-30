from matplotlib import pyplot as plt
import pandas as pd

cols = ["date","barbie","oppenheimer"]

df = pd.read_csv("./data.csv", usecols=cols)

df.plot(x="date", y=["barbie", "oppenheimer"], kind="line", figsize=(9,8))
plt.ylabel("Box Office Gross (Millions)")
plt.xlabel("Date")
plt.suptitle("Barbie vs Oppenheimer")

plt.savefig("./barbieVopp.png")