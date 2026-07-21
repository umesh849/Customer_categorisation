import joblib
import pandas as pd

# Load saved objects
model = joblib.load(r"D:\customer_categoriser\models\xgb_classifier.pkl")


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