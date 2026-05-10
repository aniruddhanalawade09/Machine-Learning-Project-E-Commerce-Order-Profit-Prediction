import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
import warnings
warnings.filterwarnings('ignore')

# =====================
# Load Files
# =====================

if not os.path.exists('model.pkl') or not os.path.exists('scaler.pkl'):
    st.error("Model files not found. Please make sure best_model.pkl and scaler.pkl are in the same folder.")
    st.stop()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.set_page_config(page_title="Profit Predictor", layout="centered")

st.title("💰 Order Profit Prediction App")
st.write("Predict expected profit using order details")

# ======================
# Inputs
# ======================

ship_mode = st.selectbox("Ship Mode", ["Second Class", "Standard Class", "First Class", "Same Day"])

segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])

region = st.selectbox("Region", ["West", "East", "Central", "South"])

category = st.selectbox("Category", ["Technology", "Office Supplies", "Furniture"])

sub_category = st.selectbox("Sub-Category", [
     'Bookcases',      'Chairs',      'Labels',      'Tables',     'Storage',
 'Furnishings',         'Art',      'Phones',     'Binders',  'Appliances',
       'Paper', 'Accessories',   'Envelopes',   'Fasteners',    'Supplies',
    'Machines',     'Copiers'
])

sales = st.number_input("Sales", min_value=1.0, value=100.0)
quantity = st.number_input("Quantity", min_value=1, value=2)
discount = st.slider("Discount", 0.0, 1.0, 0.1)
delivery_days = st.slider("Delivery Days", 1, 10, 3)
order_month = st.slider("Order Month", 1, 12, 6)
order_year = st.selectbox("Order Year", [2026,2027,2028,2029])

# ======================
# Predict Button
# ======================

if st.button("Predict Profit"):

    input_dict = {
        'Sales': sales,
        'Quantity': quantity,
        'Discount': discount,
        'Delivery Days': delivery_days,
        'Order Month': order_month,
        'Order Year': order_year
    }

    # Create empty row
    input_df = pd.DataFrame(columns=features)
    input_df.loc[0] = 0

    # Fill numeric columns
    for col in input_dict:
        if col in input_df.columns:
            input_df[col] = input_df[col].astype(float)
            input_df.at[0, col] = input_dict[col]  

    # Fill encoded columns
    cols_to_activate = [
        f"Ship Mode_{ship_mode}",
        f"Segment_{segment}",
        f"Region_{region}",
        f"Category_{category}",
        f"Sub-Category_{sub_category}"
    ]

    for col in cols_to_activate:
        if col in input_df.columns:
            input_df.at[0, col] = 1

    prediction = model.predict(input_df)[0]

    if prediction >= 0:
        st.success(f"Predicted Profit: ₹ {round(prediction,2)}")
    else:
        st.error(f"Predicted Loss: ₹ {round(prediction,2)}")