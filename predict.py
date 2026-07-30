import joblib
import pandas as pd

# Load saved objects
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "xgb_classifier.pkl")

model = joblib.load(model_path)


def predict_cluster(customer_data):

    # Convert dictionary to DataFrame
    df = pd.DataFrame([customer_data])

    # Keep the same column order used during training
    df = df[
        ['Age', 'Education', 'Marital Status', 'Parental Status', 'Children',
         'Income', 'Total_Spending', 'Days_as_Customer', 'Recency', 'Wines',
         'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold', 'Web', 'Catalog',
         'Store', 'Discount Purchases', 'Total Promo',
         'NumWebVisitsMonth']
    ]

    # Apply preprocessing

    # Predict cluster
    cluster = model.predict(df)

    return int(cluster[0])