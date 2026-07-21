import streamlit as st
from predict import predict_cluster

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📊 Customer Segmentation")

st.sidebar.markdown("""
### Project Information

**Model**
- XGBoost Classifier

**Algorithm**
- K-Means Clustering
- XGBoost Classification

**Number of Segments**
- 3

**Purpose**
- Predict customer segment
- Help marketing team target customers
""")

st.sidebar.success("Developed using Streamlit")

# -----------------------------
# TITLE
# -----------------------------

st.title("📊 Customer Segmentation Dashboard")

st.markdown("""
Predict the **customer segment** using customer demographic,
spending behaviour and shopping behaviour.
""")

st.divider()

# ======================================================
# CUSTOMER PROFILE
# ======================================================

st.subheader("👤 Customer Profile")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18.0,
        max_value=100.0,
        value=35.0
    )

    education = st.selectbox(
        "Education Level",
        [
            "Basic",
            "2n Cycle",
            "Graduation",
            "Master",
            "PhD"
        ]
    )

    marital = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Together",
            "Divorced",
            "Widow",
            "Alone",
            "YOLO",
            "Absurd"
        ]
    )

with col2:

    parental = st.radio(
        "Has Children?",
        [
            "No",
            "Yes"
        ]
    )

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=5,
        value=1
    )

    income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=50000.0
    )

st.divider()

# ======================================================
# SPENDING
# ======================================================

st.subheader("💰 Spending Behaviour")

c1, c2, c3 = st.columns(3)

with c1:

    wines = st.number_input(
        "Amount Spent on Wine",
        min_value=0.0,
        value=100.0
    )

    fruits = st.number_input(
        "Amount Spent on Fruits",
        min_value=0.0,
        value=20.0
    )

with c2:

    meat = st.number_input(
        "Amount Spent on Meat",
        min_value=0.0,
        value=100.0
    )

    fish = st.number_input(
        "Amount Spent on Fish",
        min_value=0.0,
        value=20.0
    )

with c3:

    sweets = st.number_input(
        "Amount Spent on Sweets",
        min_value=0.0,
        value=20.0
    )

    gold = st.number_input(
        "Amount Spent on Gold Products",
        min_value=0.0,
        value=20.0
    )

total_spending = st.number_input(
    "Total Spending",
    min_value=0.0,
    value=500.0
)

st.divider()

# ======================================================
# SHOPPING
# ======================================================

st.subheader("🛒 Shopping Behaviour")

left, right = st.columns(2)

with left:

    web = st.number_input(
        "Number of Web Purchases",
        min_value=0,
        value=5
    )

    catalog = st.number_input(
        "Number of Catalog Purchases",
        min_value=0,
        value=2
    )

    store = st.number_input(
        "Number of Store Purchases",
        min_value=0,
        value=5
    )

    discount = st.number_input(
        "Number of Discount Purchases",
        min_value=0,
        value=1
    )

with right:

    promo = st.number_input(
        "Promotions Accepted",
        min_value=0,
        value=1
    )

    visits = st.number_input(
        "Website Visits Per Month",
        min_value=0,
        value=5
    )

    recency = st.number_input(
        "Days Since Last Purchase",
        min_value=0.0,
        value=30.0
    )

    days = st.number_input(
        "Days Since Becoming Customer",
        min_value=0.0,
        value=4000.0
    )

# -------------------------------------------------
# MAPPINGS
# -------------------------------------------------

education_mapping = {
    "Basic":0,
    "2n Cycle":1,
    "Graduation":2,
    "Master":3,
    "PhD":4
}

marital_mapping = {
    "Married":1,
    "Together":1,
    "Single":0,
    "Divorced":0,
    "Widow":0,
    "Alone":0,
    "YOLO":0,
    "Absurd":0
}

education = education_mapping[education]
marital = marital_mapping[marital]
parental = 1 if parental=="Yes" else 0

# -------------------------------------------------
# BUTTON
# -------------------------------------------------

if st.button("🎯 Predict Customer Segment", use_container_width=True):

    customer = {

        "Age": age,
        "Education": education,
        "Marital Status": marital,
        "Parental Status": parental,
        "Children": children,
        "Income": income,
        "Total_Spending": total_spending,
        "Days_as_Customer": days,
        "Recency": recency,
        "Wines": wines,
        "Fruits": fruits,
        "Meat": meat,
        "Fish": fish,
        "Sweets": sweets,
        "Gold": gold,
        "Web": web,
        "Catalog": catalog,
        "Store": store,
        "Discount Purchases": discount,
        "Total Promo": promo,
        "NumWebVisitsMonth": visits

    }

    cluster = predict_cluster(customer)

    segment = {

        0:(
            "🟦 Regular Customer",
            "Moderate income and spending.",
            [
                "Seasonal discounts",
                "Cross-selling",
                "Email campaigns"
            ]
        ),

        1:(
            "🟩 High Value Customer",
            "Highest income and spending.",
            [
                "VIP Membership",
                "Premium products",
                "Exclusive rewards"
            ]
        ),

        2:(
            "🟨 Budget Customer",
            "Lower income and spending.",
            [
                "Discount coupons",
                "Affordable bundles",
                "Price promotions"
            ]
        )

    }

    title, description, tips = segment[cluster]

    st.success(f"Predicted Cluster : {cluster}")

    st.header(title)

    st.write(description)

    st.subheader("📋 Recommended Marketing Strategy")

    for tip in tips:
        st.write(f"✅ {tip}")

    st.divider()

    st.subheader("📈 Customer Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Income", f"₹{income:,.0f}")
    c2.metric("Total Spending", f"₹{total_spending:,.0f}")
    c3.metric("Website Visits", visits)