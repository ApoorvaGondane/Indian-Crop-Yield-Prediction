import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the model and data options
@st.cache_resource
def load_assets():
    model = joblib.load('crop_yield_model.joblib')
    options = joblib.load('unique_values.joblib')
    return model, options

model, options = load_assets()

# 2. Define Mappings (COPY THESE FROM YOUR NOTEBOOK)
# You need the exact same dictionaries you used in the notebook
region_mapping = {
    'North': ['Haryana', 'Punjab', 'Uttar Pradesh', 'Uttarakhand', 'Himachal Pradesh', 'Jammu and Kashmir', 'Delhi'],
    'South': ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Telangana', 'Puducherry'],
    'East': ['Bihar', 'West Bengal', 'Odisha', 'Jharkhand'],
    'West': ['Gujarat', 'Maharashtra', 'Goa', 'Rajasthan'],
    'Central': ['Madhya Pradesh', 'Chhattisgarh'],
    'North East': ['Assam', 'Arunachal Pradesh', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Sikkim', 'Tripura']
}

# Invert region mapping for easier lookup
state_to_region = {}
for region, states in region_mapping.items():
    for state in states:
        state_to_region[state] = region

# 3. App Layout
st.title("🌾 Indian Crop Yield Predictor")
st.markdown("Enter the farm details below to get a yield prediction.")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    crop = st.selectbox("Crop", options['Crop'])
    season = st.selectbox("Season", options['Season'])
    state = st.selectbox("State", options['State'])
    year = st.number_input("Crop Year", min_value=1997, max_value=2030, value=2024)
    area = st.number_input("Area (Hectares)", min_value=0.1, value=10.0)

with col2:
    rainfall = st.number_input("Annual Rainfall (mm)", value=1000.0)
    avg_temp = st.number_input("Avg Temperature (°C)", value=25.0)
    max_temp = st.number_input("Max Temperature (°C)", value=32.0)
    min_temp = st.number_input("Min Temperature (°C)", value=18.0)
    fertilizer = st.number_input("Total Fertilizer (kg)", value=1000.0)
    pesticide = st.number_input("Total Pesticide (kg)", value=10.0)

# 4. Prediction Logic
if st.button("Predict Yield"):
    # A. Create DataFrame from input
    input_data = pd.DataFrame({
        'Crop': [crop], 'Crop_Year': [year], 'Season': [season], 'State': [state],
        'Area': [area], 'Annual_Rainfall': [rainfall],
        'Avg_Temperature': [avg_temp], 'Max_Temperature': [max_temp], 'Min_Temperature': [min_temp],
        'Fertilizer': [fertilizer], 'Pesticide': [pesticide]
    })

    # B. Apply Feature Engineering (MUST MATCH NOTEBOOK EXACTLY)
    # 1. Per Hectare calculation
    input_data['Fertilizer_per_Hectare'] = input_data['Fertilizer'] / (input_data['Area'] + 1)
    input_data['Pesticide_per_Hectare'] = input_data['Pesticide'] / (input_data['Area'] + 1)
    
    # 2. Region Mapping
    input_data['Region'] = input_data['State'].map(state_to_region)
    # Handle states not in mapping (fallback)
    input_data['Region'] = input_data['Region'].fillna('Other')

    # 3. Crop Type Mapping (You need to define your crop_to_type dict here or load it)
    # Simple logic placeholder if you don't want to copy the full dict:
    # (Ideally, save crop_to_type dictionary in joblib and load it like unique_values)
    # For now, we pass 'Other' if unknown, but you should copy your dict here.
    input_data['Crop_Type'] = 'Cereal' # Placeholder! Replace with actual mapping logic.

    # C. Drop columns model doesn't expect
    final_input = input_data.drop(columns=['Fertilizer', 'Pesticide'])

    try:
        prediction = model.predict(final_input)[0]
        st.success(f"🌱 Predicted Yield: **{prediction:.2f} tonnes/hectare**")
        
        # Calculate Total Production
        total_production = prediction * area
        st.info(f"📦 Estimated Total Production: {total_production:.2f} tonnes")
        
    except Exception as e:
        st.error(f"Error predicting: {e}")