import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the model,
try:
    with open('rfc_model.sav', 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    loaded_model = None

# Load LabelEncoders
try:
    with open('label_encoders.pkl', 'rb') as file:
        label_encoders = pickle.load(file)
except FileNotFoundError:
    st.error("LabelEncoders file not found.  Make sure 'label_encoders.pkl' is in the correct location.")
    label_encoders = None

def main():
    
    st.title('Thyroid Cancer Recurrence Detection Model')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["M", "F"])
        smoking = st.selectbox("Smoking", ["No", "Yes"])
        physical_examination = st.selectbox("Physical Examination (Palpation of thyroid gland)", ['Single nodular goiter-left', 'Multinodular goiter','Single nodular goiter-right', 'Normal', 'Diffuse goiter'])
        focality = st.selectbox("Focality (Cancer Location)", ['Uni-Focal', 'Multi-Focal'])
        nodal  = st.selectbox("Nodal (Nodal classification)", ['N0', 'N1b', 'N1a'])
        response = st.selectbox("Response (Response to treatment)", ['Indeterminate', 'Excellent', 'Structural Incomplete','Biochemical Incomplete'])
        
    with col2:
        age = st.number_input("Age", min_value=15, value=90)
        hx_radiotherapy = st.selectbox("Radiotherapy (Radiotherapy Treatment)", ["No", "Yes"])
        adenopathy = st.selectbox("Adenopathy (Enlarged lymph nodes)", ['No', 'Right', 'Extensive', 'Left', 'Bilateral', 'Posterior'])
        risk = st.selectbox("Risk (Risk category of the cancer)", ['Low', 'Intermediate', 'High'])
        metastasis= st.selectbox("Metastasis (Metastasis classification)", ['M0', 'M1'])
        
    with col3:
        hx_smoking = st.selectbox("HX Smoking(Have Ever Smoke)", ["No", "Yes"])
        thyroid_function = st.selectbox("Thyroid Function(Status of thyroid)", ['Euthyroid', 'Clinical Hyperthyroidism', 'Clinical Hypothyroidism','Subclinical Hyperthyroidism', 'Subclinical Hypothyroidism'])
        pathology = st.selectbox("Pathology (Specific types cancer)", ['Micropapillary', 'Papillary', 'Follicular', 'Hurthel cell'])
        tumor = st.selectbox("Tumor (Tumor classification)", ['T1a', 'T1b', 'T2', 'T3a', 'T3b', 'T4a', 'T4b'])
        stage = st.selectbox("Stage (Overall stage)", ['I', 'II', 'IVB', 'III', 'IVA'])
        
            # --- Process Input Data and Make Prediction ---
    if st.button("Predict", use_container_width=True):
        if loaded_model is not None:  # Only check for the model
##['Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response']
            input_data = pd.DataFrame({
                'Age':[age],
                'Gender':[gender],
                'Smoking': [smoking],
                'Hx Smoking': [hx_smoking],
                'Hx Radiothreapy': [hx_radiotherapy],
                'Thyroid Function': [thyroid_function],
                'Physical Examination': [physical_examination],
                'Adenopathy': [adenopathy],
                'Pathology': [pathology],
                'Focality': [focality],
                'Risk': [risk],
                'T': [tumor],
                'N': [nodal],
                'M': [metastasis],
                'Stage': [stage],
                'Response': [response]
                
            })

            #Transform columns before passing to prediction
            for col in ['Gender','Smoking','Hx Smoking','Hx Radiothreapy','Thyroid Function','Physical Examination','Adenopathy','Pathology','Focality','Risk','T','N','M','Stage','Response']:
                input_data[col] = label_encoders[col].transform(input_data[col])
            try:
                prediction = loaded_model.predict(input_data) #Returns a numpy array

                if prediction[0] == 1:
                    st.error("Thyroid cancer has Recurred!, Please start your medication!!")
                else:
                    st.success("Thyroid cancer has NOT Recurred!. Take Care of your self!")

            except Exception as e:
                st.error(f"Prediction failed: {e}")

        else:
            st.error("Model not loaded.  Please check the file path.")  # Simplified message


        
if __name__ == '__main__':
    main()