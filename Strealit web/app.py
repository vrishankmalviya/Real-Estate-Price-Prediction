import streamlit as st
import requests

# URL of your deployed Flask backend
BACKEND_URL = "https://bengaluru-real-estate-price-prediction.onrender.com"

# Page title and description
st.title("🏠 Bengaluru Real Estate Price Predictor")
st.write("Enter property details below and click **Predict** to see the estimated price.")

# 1. Fetch list of locations from backend
@st.cache_data
def fetch_locations():
    response = requests.get(f"{BACKEND_URL}/get_location")
    if response.status_code == 200:
        return response.json()["locations"]
    else:
        return []

locations = fetch_locations()

# 2. Build input form
st.header("Property Details")
location = st.selectbox("Location", options=locations)
total_sqft = st.number_input("Total Square Feet", min_value=300, value=10000, step=50)
bhk = st.selectbox("Bedrooms (BHK)", options=[1,2,3,4,5], index=1)
bath = st.selectbox("Bathrooms", options=[1,2,3,4], index=1)
balcony = st.selectbox("Balconies", options=[0,1,2,3], index=1)

# 3. Predict button
if st.button("🔮 Predict Price"):
    # Show a spinner while waiting
    with st.spinner("Predicting..."):
        # Prepare form data
        data = {
            "location": location,
            "total_sqft": total_sqft,
            "bhk": bhk,
            "bath": bath,
            "balcony": balcony
        }
        # Call the backend API
        response = requests.post(f"{BACKEND_URL}/predict_home_price", data=data)
        if response.status_code == 200:
            price = response.json()["price"]
            st.success(f"Estimated Price: ₹{price:,.2f} Lakhs")
        else:
            st.error("Failed to get prediction. Try again later.")
