# import pandas as pd
# import numpy as np
# from datetime import datetime
# from sklearn.cluster import KMeans
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_excel("Clusters.xlsx")

# # Data Cleaning
# df = df[df['CustomerID'].notnull()] #shouldnt be null if null data row will be deleted
# df['CustomerID'] = df['CustomerID'].astype(int) #to uniquely identify
# df = df[df['Quantity'] > 0] #quantity less than 0 would be cleaned (entire row)
# df = df[df['UnitPrice'] > 0] #unitprice less than 0 would be cleaned (entire row)
# df['TotalPrice'] = df['Quantity'] * df['UnitPrice'] #total purchase amount will be stored in TotalPrice for each row

# # Define the snapshot date (assumed as the last date in dataset)
# snapshot_date = df['InvoiceDate'].max() #finding out the recent most(latest) purchase date

# # RFM Calculation
# rfm = df.groupby('CustomerID').agg({ #agg function used to iterate each data in a highly optimized way
#     'InvoiceDate': lambda x: (snapshot_date - x.max()).days,#Recency  #calculates no. of days difference between recent purchase and customers's last purchase
#     'InvoiceNo': 'count',  # Frequency #no. of items purchased
#     'TotalPrice': 'sum'  # Monetary #total purchase money throughout the customer's career (like how much a customer spend in total)
# })

# # Rename columns
# rfm.rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalPrice': 'Monetary'}, inplace=True)

# # Log transformation to normalize data
# rfm_log = np.log1p(rfm) #used to decrease large difference values to smaller (normalized form)

# # K-Means Clustering
# kmeans = KMeans(n_clusters=4, random_state=42) #n_clusters means no. of clusters required  #random_state ensures that every time the code is executed, the results remain consistent instead of changing on each run.
# rfm['Cluster'] = kmeans.fit_predict(rfm_log) #dividing users to different clusters
# print(rfm[['Cluster']]) #printing clusters division in console

# # Visualize Clusters
# sns.pairplot(rfm, hue='Cluster', diag_kind='kde') #visualizing whole data in a graph for better understanding 
# plt.show()

# # Display clustered RFM data
# rfm.head()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50],
    'SpendingScore': [60, 55, 70, 80, 65, 50],
    'Cluster': [0, 1, 0, 2, 1, 2]
})

# Scatter plot with Seaborn
sns.scatterplot(x='Age', y='SpendingScore', hue='Cluster', palette='viridis', data=data)
plt.title("Customer Clusters Based on Age & Spending Score")
plt.show()