# 📊 Customer Segmentation using Machine Learning

A machine learning web application that predicts the customer segment of a new customer based on demographic information, spending behaviour, and purchasing history.

The project combines **unsupervised learning (K-Means Clustering)** with **supervised learning (XGBoost Classifier)** to provide fast and accurate customer segmentation.


# 📌 Project Overview

Customer segmentation helps businesses divide customers into groups with similar characteristics. These groups can then be targeted with personalized marketing strategies.

In this project:

- Performed Exploratory Data Analysis (EDA)
- Cleaned and preprocessed the dataset
- Applied feature engineering
- Used multiple clustering algorithms
- Selected the best clustering model
- Used generated cluster labels to train a classifier
- Built a Streamlit web application for prediction

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Streamlit
- Joblib

# 📊 Dataset

The project uses the **Marketing Campaign Dataset** containing customer information such as:

- Age
- Education
- Marital Status
- Income
- Spending on different products
- Number of purchases
- Promotions accepted
- Website visits
- Customer recency

---

# 🔍 Exploratory Data Analysis

Performed:

- Missing value treatment
- Feature engineering
- Outlier detection
- Correlation analysis
- Distribution plots
- Box plots
- Heatmaps
- Spending analysis
- Customer demographics analysis

---

# ⚙ Feature Engineering

Created new features such as:

- Age
- Total Spending
- Days as Customer
- Children
- Parental Status

Encoded categorical variables including:

- Education
- Marital Status

Applied:

- Standard Scaling
- Power Transformation

---

# 🤖 Clustering

The following clustering algorithms were evaluated:

- K-Means
- Agglomerative Clustering
- DBSCAN
- Gaussian Mixture Model (if applicable)

Evaluation metrics:

- Silhouette Score
- Elbow Method
- Kneedle Algorithm

The best performing algorithm was selected to generate customer segments.

---

# 🎯 Classification

The generated cluster labels were used as target labels.

Several classification algorithms were compared.

Final model:

✅ XGBoost Classifier

Hyperparameter tuning was performed using **RandomizedSearchCV**.

---

# 📈 Model Performance

Model Used:

**XGBoost Classifier**

Evaluation Metrics:

- Accuracy
- Classification Report
- Confusion Matrix

Accuracy : 97.02%

Example:


---

# 💻 Web Application

Built using **Streamlit**.

Features:

- Customer Profile Input
- Spending Behaviour Input
- Shopping Behaviour Input
- Predict Customer Segment
- Business Recommendation
- Customer Summary Dashboard

---

# ▶️ Installation

Clone the repository

```bash
git clone
https://github.com/umesh849/Customer_categorisation.git
```

Go inside the project

```bash
cd Customer_categorisation 
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---
