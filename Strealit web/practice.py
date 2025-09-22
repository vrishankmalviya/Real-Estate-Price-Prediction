import streamlit as st 

st.title("Bengluru price prediction")
st.header("Please tell your requirnments below :")

area=st.number_input("Area(SQFT)",min_value=200,max_value=200000,step=50)

bhk=st.slider("BHK",1,10,3,step=1)

bathroom=st.slider("Number of Bathrooms",1,10,3,step=1)

balcony = st.slider("Number of balcony",1,10,3,step=1)

location = st.selectbox("Select Location", ["Indira Nagar", "Whitefield", "Electronic City", "Banashankari"])


if st.button("Predict Price"):
    st.write("### 📌 Input Summary")
    st.write(f"Area: {area} sqft")
    st.write(f"BHK: {bhk}")
    st.write(f"Bathroom: {bathroom}")
    st.write(f"Balcony: {balcony}")
    st.write(f"Location: {location}")

    # Placeholder (later will call API here)
    st.success("Estimated Price: (API will be connected here)")
