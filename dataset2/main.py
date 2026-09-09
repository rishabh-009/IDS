import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

filepath = "D:\\Learning\\IDS\\retail_marketing_sales.csv"

sns.set_style('darkgrid')



df = pd.read_csv(filepath)

print(df.head(150))

# plt.hist(df['Store_Area_sqft'],bins=15)
# plt.show()

# city_sales = df.groupby('City')['Monthly_Sales_Lakhs'].sum()

# city_sales.plot(kind='bar')
# plt.show()

# plt.scatter(df['No_of_Promotions'],df['Monthly_Sales_Lakhs'])
# plt.show()

# sns.pairplot(df[["Store_Area_sqft", "No_of_Promotions", "Avg_Footfall_per_Day", "Monthly_Sales_Lakhs"]])

# plt.show()

# corr = df.select_dtypes(include=[np.number]).corr()
# sns.heatmap(corr,annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
# plt.show()

