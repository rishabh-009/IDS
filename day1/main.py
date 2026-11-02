import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pathlib import Path

filepath = "D:\\Learning\\IDS\\retail_marketing_sales.csv"

sns.set_style('darkgrid')

df = pd.read_csv(filepath)

# print(df.head(5))

# print(df.info())
# print(df.describe())




# nulls = df.isnull().sum()
# print(nulls)

# duplicates = df.duplicated().sum()
# print(duplicates)

# TASK B1

# plt.hist(df["Order_Value"],bins = 15)
# plt.title('Order Value Distribution')
# plt.xlabel("Total Order Value")
# plt.ylabel("Number of Orders")
# plt.show()

# TASK B2

# plt.scatter(df['Discount_Percent'],df['Profit'])
# plt.show()

# Task B3


df.groupby("Product_Category")["Profit"].mean().plot(kind="bar")

plt.title("Average Profit by Product Category")
plt.ylabel("Mean Profit")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()




# plt.title("Average Profit by Product Category")
# plt.ylabel("Mean Profit")
# plt.xlabel("Product Category")
# plt.tight_layout()






# Task B4

# counts = df['Customer_Segment'].value_counts()
# plt.pie(counts, labels=counts.index)
# plt.show()


# Task B5
# sns.countplot(x="Payment_Mode", data=df)
# plt.xticks(rotation=20)
# plt.show()

# Task B6

# sns.boxplot(x=df["Order_Value"])
# plt.show()

# Task B7

# sns.regplot(x="Order_Value", y="Profit", data=df)
# plt.show()

df['Value_Tier'] = pd.cut(df['Order_Value'], bins=[0,5000,25000,90000],labels=["Low","Medium","High"])

# a.value_counts().plot(kind='bar')
# plt.show()


df['Log_Order_Value']=np.log(df['Order_Value'])
df['Profit_Margin'] = (df['Profit'] / df['Order_Value']) * 100


# print(df[["Order_ID", "Order_Value", "Profit", "Value_Tier", "Log_Order_Value", "Profit_Margin"]].head(8))


# sns.violinplot(df,x='Customer_Segment',y='Order_Value')
# plt.show()


# sns.swarmplot(x="Value_Tier",y="Profit",data=df)
# plt.show()

# a = pd.pivot_table(df, values="Profit",index='Customer_Segment',columns="Product_Category", aggfunc="mean")
# plt.figure(figsize=(10, 4))
# sns.heatmap(a,annot=True, fmt=".0f", cmap="YlOrRd")

# plt.show()

# sns.pairplot(df[["Order_Value", "Discount_Percent", "Profit", "Delivery_Days", "Customer_Rating", "Value_Tier"]], hue="Value_Tier")

# plt.show()

# corr = df.select_dtypes(include=[np.number]).corr()
# sns.heatmap(corr,annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
# plt.show()