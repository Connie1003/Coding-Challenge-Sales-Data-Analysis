import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#1. Read Data
df = pd.read_csv('sample_data.csv')
print(df)


#2. Data Cleaning
df['Date'] = pd.to_datetime(df['Date'])
print(df)


#3. Total Revenue Calculation
total_revenue1 = pd.DataFrame({'Date': df['Date'],'Product': df['Product'],'Total Revenue':df['Units Sold']*df['Unit Price']})
total_revenue2 = total_revenue1.groupby('Product').agg({'Total Revenue':'sum'})


#4. Monthly Sales Report
#Jan
january = df[df['Date'].dt.month == 1]
january_data = january.groupby('Product').agg({'Units Sold':'sum','Total Revenue':'sum'}).reset_index()
january_data.insert(0, column="Month", value="January")

#Feb
february = df[df['Date'].dt.month == 2]
february_data = february.groupby('Product').agg({'Units Sold':'sum','Total Revenue':'sum'}).reset_index()
february_data.insert(0, column="Month", value="February")

#Mar
march = df[df['Date'].dt.month == 3]
march_data = march.groupby('Product').agg({'Units Sold':'sum','Total Revenue':'sum'}).reset_index()
march_data.insert(0, column="Month", value="March")


#5. Best Performing Product
all_data = pd.concat([january_data,february_data,march_data])
total_data = all_data.groupby('Product').agg({'Units Sold':'sum','Total Revenue':'sum'})
print(total_data)


#6. Plotting
sns.set_style("whitegrid")
sns.set_palette('muted')
plt.figure(figsize=(7, 4))

sns.barplot(x="Month", y="Units Sold", hue="Product", data=all_data)
plt.title('Units Sold by Month and Product')
plt.show()



