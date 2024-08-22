import streamlit as st
import pickle
import numpy as np


def model_dt():
    def load_model():
        with open("saved_steps.pkl", "rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_dt"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Developers Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2023 data using Decision Tree Regressor with max depth = 10 to minimize the error.""")
        st.write("""### We need some info to predict the salary.""")
        
        countries = ('United States of America', 'Germany', 'United Kingdom of Great Britain and Northern Ireland', 'Canada', 'India', 'France', 'Brazil', 'Netherlands', 'Australia', 'Spain', 'Poland', 'Sweden', 'Italy', 'Switzerland', 'Denmark', 'Norway', 'Israel', 'Portugal', 'Austria')
        education_options = ('Bachelor’s degree', "Master's Degree", 'Post Graduation', 'Less than a bachelor')
        
        country = st.selectbox("Country", countries)
        education = st.selectbox("Education Level", education_options)
        experience = st.slider("Years of Experience", 0, 50, 2)
        
        predict_button = st.button("Calculate Salary")
        
        if predict_button:
            # Ensure country name is stripped of leading/trailing spaces
            country = country.strip()
            X = np.array([[country, education, experience]])
            
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(float)

            y_prediction_inp = model.predict(X)

            st.subheader(f"The estimated salary is {y_prediction_inp[0]:.2f} USD")

    show_predict_page()




def model_linear():
    def load_model():
        with open("saved_steps.pkl", "rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_linear"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Developers Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2023 data using Linear Regressor""")
        st.write("""### We need some info to predict the salary.""")
        
        countries = ('United States of America', 'Germany', 'United Kingdom of Great Britain and Northern Ireland', 'Canada', 'India', 'France', 'Brazil', 'Netherlands', 'Australia', 'Spain', 'Poland', 'Sweden', 'Italy', 'Switzerland', 'Denmark', 'Norway', 'Israel', 'Portugal', 'Austria')
        education_options = ('Bachelor’s degree', "Master's Degree", 'Post Graduation', 'Less than a bachelor')
        
        country = st.selectbox("Country", countries)
        education = st.selectbox("Education Level", education_options)
        experience = st.slider("Years of Experience", 0, 50, 2)
        
        predict_button = st.button("Calculate Salary")
        
        if predict_button:
            # Ensure country name is stripped of leading/trailing spaces
            country = country.strip()
            X = np.array([[country, education, experience]])
            
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(float)

            y_prediction_inp = model.predict(X)

            st.subheader(f"The estimated salary is {y_prediction_inp[0]:.2f} USD")
            print("Predicted Salary using linear model sucessfully")

    show_predict_page()



def model_gradient():
    def load_model():
        with open("saved_steps.pkl", "rb") as file:
            data = pickle.load(file)
        return data

    data = load_model()

    model = data["model_gradient"]
    le_country = data["le_country"]
    le_education = data["le_education"]

    def show_predict_page():
        st.title("Software Developers Salary Prediction")
        st.write("""#### The Salary is predicted from Stackoverflow developer survey 2023 data using Gradient Descent Regressor""")
        st.write("""### We need some info to predict the salary.""")
        
        countries = ('United States of America', 'Germany', 'United Kingdom of Great Britain and Northern Ireland', 'Canada', 'India', 'France', 'Brazil', 'Netherlands', 'Australia', 'Spain', 'Poland', 'Sweden', 'Italy', 'Switzerland', 'Denmark', 'Norway', 'Israel', 'Portugal', 'Austria')
        education_options = ('Bachelor’s degree', "Master's Degree", 'Post Graduation', 'Less than a bachelor')
        
        country = st.selectbox("Country", countries)
        education = st.selectbox("Education Level", education_options)
        experience = st.slider("Years of Experience", 0, 50, 2)
        
        predict_button = st.button("Calculate Salary")
        
        if predict_button:
            # Ensure country name is stripped of leading/trailing spaces
            country = country.strip()
            X = np.array([[country, education, experience]])
            
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(float)

            y_prediction_inp = model.predict(X)

            st.subheader(f"The estimated salary is {y_prediction_inp[0]:.2f} USD")
            print("Predicted Salary using linear gradient model sucessfully")

    show_predict_page()

