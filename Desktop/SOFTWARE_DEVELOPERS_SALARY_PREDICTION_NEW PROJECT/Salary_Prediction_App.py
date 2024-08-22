
import streamlit as st
from prediction_page import model_dt,model_linear,model_gradient
from explore_page import show_explore_page


explore=st.sidebar.selectbox("Choose : ",("Explore Data","Predict"))


if(explore=="Predict") : 
    selection=st.sidebar.selectbox("Regression Model",("Decision Tree Regressor","Linear Regressor","Gradient Regressor"))
    if(selection=="Decision Tree Regressor") :
        model_dt()
    if(selection=="Linear Regressor") : 
        model_linear()
    if(selection=="Gradient Regressor") : 
        model_gradient()

if(explore=="Explore Data") : 
    show_explore_page()
