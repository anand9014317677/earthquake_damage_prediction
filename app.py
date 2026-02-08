import streamlit as st
import pandas as pd
import joblib

import os

st.title("Earthquake Damage Prediction App")

# ------------------------------
# Download model from Google Drive (only first time)
# ------------------------------
model_url = "https://drive.google.com/uc?id=14fQfBzg6YNudsAW1fgPJjfmGTJ8NEiBu"
model_path = "model.pkl"

model = joblib.load(model_path)

# ------------------------------
# MODEL TRAINING COLUMNS (38)
# ------------------------------
model_columns = [
'geo_level_1_id','geo_level_2_id','geo_level_3_id',
'count_floors_pre_eq','age','area_percentage','height_percentage',
'land_surface_condition','foundation_type','roof_type',
'ground_floor_type','other_floor_type','position',
'plan_configuration','has_superstructure_adobe_mud',
'has_superstructure_mud_mortar_stone','has_superstructure_stone_flag',
'has_superstructure_cement_mortar_stone',
'has_superstructure_mud_mortar_brick',
'has_superstructure_cement_mortar_brick',
'has_superstructure_timber','has_superstructure_bamboo',
'has_superstructure_rc_non_engineered',
'has_superstructure_rc_engineered',
'has_superstructure_other','legal_ownership_status',
'count_families','has_secondary_use',
'has_secondary_use_agriculture','has_secondary_use_hotel',
'has_secondary_use_rental','has_secondary_use_institution',
'has_secondary_use_school','has_secondary_use_industry',
'has_secondary_use_health_post','has_secondary_use_gov_office',
'has_secondary_use_use_police','has_secondary_use_other'
]

# ------------------------------
# USER INPUTS
# ------------------------------

st.subheader("Building Information")

geo_level_3_id = st.number_input("Geo Level 3 ID", value=12198)
count_floors_pre_eq = st.number_input("Floors Before Earthquake", value=2)
age = st.number_input("Building Age", value=30)
area_percentage = st.number_input("Area Percentage", value=6.0)
height_percentage = st.number_input("Height Percentage", value=5.0)
count_families = st.number_input("Number of Families", value=1)

land_surface_condition = st.selectbox("Land Surface Condition", ['t','n','o'])
foundation_type = st.selectbox("Foundation Type", ['r','w','i'])
roof_type = st.selectbox("Roof Type", ['n','q','x'])
ground_floor_type = st.selectbox("Ground Floor Type", ['f','m','v'])
other_floor_type = st.selectbox("Other Floor Type", ['q','s','x'])
position = st.selectbox("Building Position", ['t','j','o'])
plan_configuration = st.selectbox("Plan Configuration", ['d','q','u'])
legal_ownership_status = st.selectbox("Legal Ownership Status", ['v','a','r','w'])

st.subheader("Superstructure Details (0 = No, 1 = Yes)")

has_superstructure_adobe_mud = st.selectbox("Adobe Mud", [0,1])
has_superstructure_mud_mortar_stone = st.selectbox("Mud Mortar Stone", [0,1])
has_superstructure_stone_flag = st.selectbox("Stone Flag", [0,1])
has_superstructure_cement_mortar_stone = st.selectbox("Cement Mortar Stone", [0,1])
has_superstructure_mud_mortar_brick = st.selectbox("Mud Mortar Brick", [0,1])
has_superstructure_cement_mortar_brick = st.selectbox("Cement Mortar Brick", [0,1])
has_superstructure_timber = st.selectbox("Timber", [0,1])
has_superstructure_bamboo = st.selectbox("Bamboo", [0,1])
has_superstructure_rc_non_engineered = st.selectbox("RC Non Engineered", [0,1])
has_superstructure_rc_engineered = st.selectbox("RC Engineered", [0,1])
has_superstructure_other = st.selectbox("Other Structure", [0,1])

st.subheader("Secondary Usage")

has_secondary_use = st.selectbox("Has Secondary Use", [0,1])
has_secondary_use_agriculture = st.selectbox("Agriculture", [0,1])
has_secondary_use_hotel = st.selectbox("Hotel", [0,1])
has_secondary_use_rental = st.selectbox("Rental", [0,1])
has_secondary_use_institution = st.selectbox("Institution", [0,1])
has_secondary_use_school = st.selectbox("School", [0,1])
has_secondary_use_industry = st.selectbox("Industry", [0,1])
has_secondary_use_health_post = st.selectbox("Health Post", [0,1])
has_secondary_use_gov_office = st.selectbox("Gov Office", [0,1])
has_secondary_use_use_police = st.selectbox("Police", [0,1])
has_secondary_use_other = st.selectbox("Other Use", [0,1])

# ------------------------------
# PREDICTION
# ------------------------------

if st.button("Predict Damage Level"):

    input_data = {
        'geo_level_1_id':0,
        'geo_level_2_id':0,
        'geo_level_3_id':geo_level_3_id,
        'count_floors_pre_eq':count_floors_pre_eq,
        'age':age,
        'area_percentage':area_percentage,
        'height_percentage':height_percentage,
        'land_surface_condition':land_surface_condition,
        'foundation_type':foundation_type,
        'roof_type':roof_type,
        'ground_floor_type':ground_floor_type,
        'other_floor_type':other_floor_type,
        'position':position,
        'plan_configuration':plan_configuration,
        'legal_ownership_status':legal_ownership_status,
        'count_families':count_families,
        'has_superstructure_adobe_mud':has_superstructure_adobe_mud,
        'has_superstructure_mud_mortar_stone':has_superstructure_mud_mortar_stone,
        'has_superstructure_stone_flag':has_superstructure_stone_flag,
        'has_superstructure_cement_mortar_stone':has_superstructure_cement_mortar_stone,
        'has_superstructure_mud_mortar_brick':has_superstructure_mud_mortar_brick,
        'has_superstructure_cement_mortar_brick':has_superstructure_cement_mortar_brick,
        'has_superstructure_timber':has_superstructure_timber,
        'has_superstructure_bamboo':has_superstructure_bamboo,
        'has_superstructure_rc_non_engineered':has_superstructure_rc_non_engineered,
        'has_superstructure_rc_engineered':has_superstructure_rc_engineered,
        'has_superstructure_other':has_superstructure_other,
        'has_secondary_use':has_secondary_use,
        'has_secondary_use_agriculture':has_secondary_use_agriculture,
        'has_secondary_use_hotel':has_secondary_use_hotel,
        'has_secondary_use_rental':has_secondary_use_rental,
        'has_secondary_use_institution':has_secondary_use_institution,
        'has_secondary_use_school':has_secondary_use_school,
        'has_secondary_use_industry':has_secondary_use_industry,
        'has_secondary_use_health_post':has_secondary_use_health_post,
        'has_secondary_use_gov_office':has_secondary_use_gov_office,
        'has_secondary_use_use_police':has_secondary_use_use_police,
        'has_secondary_use_other':has_secondary_use_other
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df[model_columns]

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("Low Damage Expected")
    elif prediction[0] == 2:
        st.warning("Medium Damage Expected")
    else:
        st.error("Severe Damage Expected")