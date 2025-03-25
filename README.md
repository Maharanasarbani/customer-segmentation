This project performs Customer Segmentation using Recency, Frequency, and Monetary (RFM) analysis and K-Means Clustering.
The goal is to segment customers based on their purchasing behavior to enable data-driven marketing strategies.

Dataset-
The dataset is loaded from Clusters.xlsx, containing customer transaction details.

Key columns include-
CustomerID: Unique identifier for each customer.
InvoiceDate: Date of purchase.
InvoiceNo: Number of purchases.
Quantity: Number of items purchased.
UnitPrice: Price per unit of the item.
TotalPrice: Computed as Quantity * UnitPrice.

Preprocessing Steps -
Data Cleaning:
1)Remove rows where CustomerID is missing.
2)Convert CustomerID to an integer type.
3)Remove negative values in Quantity and UnitPrice.
4)Compute TotalPrice (Total amount spent per transaction).

RFM Calculation:
1)Recency: Days since the last purchase.
2)Frequency: Number of purchases made.
3)Monetary: Total money spent.
4)Data Normalization: Log transformation is applied to RFM values to reduce skewness.

Clustering Using K-Means-
1)K-Means Algorithm:
a)We use 4 clusters (n_clusters=4) to segment customers.
b)random_state=42 ensures reproducibility.
c)Clustering is performed on the log-transformed RFM data.
2)Cluster Assignment:
a)Each customer is assigned to a cluster based on purchasing behavior.
b)The results are displayed in the console.

Visualization-
1)Pairplot with Seaborn:
A pairplot is used to visualize clusters across RFM dimensions.
2)Scatter Plot:
Customers are plotted based on Age vs. Spending Score with color-coded clusters.

To improve customer relationship management and business decision-making, advanced features have been added to the customer segmentation model. These features allow businesses to provide personalized product recommendations, optimize loyalty programs, and create targeted marketing campaigns.
1)Personalized Product Recommendations:
A key goal of customer segmentation is to offer the right products to the right customers. This feature suggests specific product categories based on customer segments.
2)Loyalty Program Optimization:
Loyalty programs encourage customers to make repeat purchases. This feature assigns custom discount offers based on customer value.
3)Email & Ad Campaign Segmentation:
Effective marketing requires personalized communication. This feature segments customers into different marketing campaigns for better engagement.


Key Takeaways-
1)High-value customers have high frequency & monetary scores but may need re-engagement if their recency is high.
2)New or low-spending customers can be identified and targeted differently.
3)The segmentation can help in personalized marketing campaigns to improve customer engagement and retention.

How to Run the Project-
1)Install dependencies:
a)pip install pandas numpy seaborn matplotlib scikit-learn openpyxl
b)Run the Python script:
  python main.py
c)View the segmentation results and visualizations.

Usage-
1)Run the Jupyter notebook:
jupyter notebook
Open Customer_Segmentation.ipynb and execute the cells step by step.

Results-
Visualizations of customer clusters
Insights for targeted marketing campaigns
Better customer engagement strategies

Contributing-
Feel free to fork this repository, raise issues, or submit pull requests.

License-
This project is licensed under the MIT License
