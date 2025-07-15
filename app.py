import streamlit as st
import joblib
import numpy as np

# Set page config
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

st.title("🚗 Car Price Predictor")
st.markdown("### Enter the details of the car below:")

# Layout for better UI
col1, col2 = st.columns(2)

with col1:
    year = st.slider("Year of Manufacture", 2000, 2025, 2015)
    present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, step=0.5, value=5.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500, value=30000)
    owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])  # Not used in model
    future_year = st.slider("Predict Price As Of Year", 2024, 2030, 2025)

# Encoding categorical variables (based on training format)
fuel_diesel = 1 if fuel_type == 'Diesel' else 0
fuel_petrol = 1 if fuel_type == 'Petrol' else 0
# CNG is the "other" category (both 0)

seller_individual = 1 if seller_type == 'Individual' else 0

# Compute car age for future prediction
car_age = max(future_year - year, 0)

# Final input array (7 features as per trained model)
input_data = np.array([[present_price, kms_driven, owner, car_age,
                        fuel_diesel, fuel_petrol, seller_individual]])

# Load trained model
model = joblib.load("random_forest_model.pkl")

# Predict
if st.button("🔍 Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Car Price in {future_year}: ₹{prediction[0]:,.2f} Lakhs")

# Footer
st.markdown("---")
st.caption("Created by Antara | Built with Streamlit and scikit-learn")
