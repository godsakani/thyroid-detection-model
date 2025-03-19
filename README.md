# Project Overview

**Title**
Analysis and Machine Learning detection Model for Thyroid Cancer Recurrence with Deployment

**Objective**
Develop a machine learning model to predict the recurrence of well-differentiated thyroid cancer based on clinicopathologic features.

**Scope:**  

- **Data Cleaning and Preprocessing:**  
  Address missing values, standardize column names, and ensure correct data types.
- **Exploratory Data Analysis (EDA):**  
  Visualize trends and relationships among variables to understand factors influencing Thyroid cancer recurrence.
- **Modeling:**  
  Build and compare multiple regression models (e.g., Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting) to predict market sales.
- **Deployment:**  
  Create an interactive web application using Streamlit to deploy the best performing model, allowing users to input feature values and obtain Thyroid cancer recurrences.

**About Dataset**
**Context**
This data set contains 13 clinicopathologic features aiming to predict recurrence of well differentiated thyroid cancer. The data set was collected in duration of 15 years and each patient was followed for at least 10 years.

**Potential Benefits**
• Identify patients at higher risk of recurrence, enabling early interventions and more effective treatments.
• Determine Factors responsible for thyroid cancer recurrence.
• Improve the management of hospital resources by focusing attention on patients with a higher likelihood of recurrence.
• Assist doctors in clinical decision-making by providing insights into individual recurrence risk for patients

**Column Descriptions**

1. Age: The age of the patient at the time of diagnosis or treatment.
2. Gender: The gender of the patient (male or female).
3. Smoking: Whether the patient is a smoker or not.
4. Hx Smoking: Smoking history of the patient (e.g., whether they have ever smoked).
5. Hx Radiotherapy: History of radiotherapy treatment for any condition.
6. Thyroid Function: The status of thyroid function, possibly indicating if there are any abnormalities.
7. Physical Examination: Findings from a physical examination of the patient, which may include palpation of the thyroid gland and surrounding structures.
8. Adenopathy: Presence or absence of enlarged lymph nodes (adenopathy) in the neck region.
9. Pathology: Specific types of thyroid cancer as determined by pathology examination of biopsy samples.
10. Focality: Whether the cancer is unifocal (limited to one location) or multifocal (present in multiple locations).
11. Risk: The risk category of the cancer based on various factors, such as tumor size, extent of spread, and histological type.
13.T: Tumor classification based on its size and extent of invasion into nearby structures.
14.N: Nodal classification indicating the involvement of lymph nodes.
15.M: Metastasis classification indicating the presence or absence of distant metastases.
16.Stage: The overall stage of the cancer, typically determined by combining T, N, and M classifications.
17 Response: Response to treatment, indicating whether the cancer responded positively, negatively, or remained stable after treatment.
18.Recurred: Indicates whether the cancer has recurred after initial treatment.

## Methodology

1. **Data Cleaning and Imputation:**  
   The project begins with cleaning the dataset by standardizing column names, converting data types.

2. **Exploratory Data Analysis (EDA):**  
   Various plots (histograms, heatmaps, barplot, pie plot ) are used to understand the distribution of unit price and the relationships among the predictor variables.

3. **Feature Engineering:**  
   - Categorical variables such as **Physical Environment, Tumur, Gender** are encoded.
   - Other numeric variables are standardized to ensure that models perform optimally.

4. **Model Development:**  
   Multiple regression models, including Random Forest (the primary model), are trained to predict market sales. Their performance is evaluated using metrics like Mean Squared Error (MSE), f1_Score, confusion matrix and R-squared.

5. **Deployment:**  
   The final model is deployed using Streamlit, allowing end-users to interact with the model by inputting various health indicators and received thyroid detection in real time.

## Link to dataset

[Thyroid Disease Data](https://www.kaggle.com/datasets/jainaru/thyroid-disease-data)
