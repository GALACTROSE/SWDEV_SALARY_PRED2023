import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#This is the Function to lower the countries as per data & keep only countries which got more than threshold data given

def country_adjustment(categories,threshold) :
    categorical_map={}
    for i in range(len(categories)) : 
        if(categories.values[i]>=threshold) : 
            categorical_map[categories.index[i]]=categories.index[i]
        else : 
            categorical_map[categories.index[i]]="Other"
    return categorical_map

#This's the Function to clean the experience feature in the dataset

def clean_the_experience(x) :
    if(x=="Less than 1 year") : 
        return 0.5
    elif(x=="More than 50 years") :
        return 50
    else : 
        return float(x)
    
#This's the Function to clean the education feature in the dataset

def clean_the_education(x) : 
    if(x=="Bachelor’s degree (B.A., B.S., B.Eng., etc.)" or x=="Some college/university study without earning a degree") : 
        return "Bachelor’s degree"
    elif(x=="Master’s degree (M.A., M.S., M.Eng., MBA, etc.)") :
        return "Master's Degree"
    elif(x=="Professional degree (JD, MD, Ph.D, Ed.D, etc.)") : 
        return "Post Graduation"
    else : 
        return "Less than a bachelor"


# This is the Function to load the dataset and clean the dataset using above function calls
@st.cache_data
def load_data() :
    survey_df=pd.read_csv("survey_results_public.csv")
    survey_df=survey_df[["Country","EdLevel","YearsCodePro","Employment","ConvertedCompYearly"]]
    survey_df=survey_df.rename({"ConvertedCompYearly":"Salary"},axis=1)
    survey_df=survey_df[survey_df["Salary"].notnull()]
    survey_df=survey_df.dropna()
    survey_df=survey_df[survey_df["Employment"].str.contains("Employed, full-time", na=False)]
    survey_df=survey_df.drop("Employment",axis=1)

    # clean the feature of country
    country_map=country_adjustment(survey_df["Country"].value_counts(),400)
    survey_df["Country"]=survey_df["Country"].map(country_map)

    #removing the feature of outliers
    survey_df=survey_df[survey_df["Salary"]<=250000]
    survey_df=survey_df[survey_df["Salary"]>=30000]
    survey_df=survey_df[survey_df["Country"]!="Other"]

    #clean the feature of experience
    survey_df["YearsCodePro"]=survey_df["YearsCodePro"].apply(clean_the_experience)
    
    # clean the feature of education
    survey_df["EdLevel"]=survey_df["EdLevel"].apply(clean_the_education)

    return survey_df


survey_df=load_data()

def show_explore_page() : 
    st.title("Explore Software Developer Salaries.")
    st.write("""
    ### Stack Overflow Developer Survey 2023
    """)

    #customizing the pie chart
    data=survey_df["Country"].value_counts()
    fig1,ax1=plt.subplots()
    colors=plt.cm.Paired(np.arange(len(data)))
    explode=[0.1 if i==0 else 0 for i in range(len(data))] 

    wedges,texts,autotexts=ax1.pie(data,labels=data.index,autopct="%1.1f%%",startangle=50,colors=colors,explode=explode,wedgeprops={'edgecolor':'black'})

    #customizing text properties
    plt.setp(autotexts,size=10,weight="bold",color="white")
    plt.setp(texts,size=8,weight="bold")

    #adding a legend
    ax1.legend(wedges,data.index,title="Countries",loc="center left",bbox_to_anchor=(1,0,0.5,1))

    #add title to the pie chart
    plt.title("Number of Records by Country", fontsize=14, weight="bold")

    ax1.axis("equal")

    st.write('''### Number of records of data from different countries''')
    st.pyplot(fig1)


    st.write("""
    ### Mean Salary based on Country
    """)
    agreement = st.button("Click to see Mean Salary based on Country")
    if agreement:
        data_salary_mean = survey_df.groupby(["Country"])["Salary"].mean().sort_values(ascending=False)
        st.bar_chart(data_salary_mean)
        print("called 2")

    
    st.write("""
    ### Mean Years of Experience based on Country
    """)
    agreement=st.button("Click to see Mean Years of Experience based on Country")
    if agreement : 
        data_experience_mean=survey_df.groupby(["Country"])["YearsCodePro"].mean().sort_values(ascending=False)
        st.bar_chart(data_experience_mean)

    
    st.write("""
    ### Mean Salary based on Years of Experience
    """)
    agreement = st.button("Click to see Mean Salary based on Years of Experience")
    if agreement:
        data_expsalary_mean = survey_df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=False)
        st.line_chart(data_expsalary_mean)
        print("called 4")


    st.write("""
    ### All Data of Salaries
    """)
    agreement = st.button("Click to see All Data of Salaries")
    if agreement:
        chart_data = pd.DataFrame(survey_df[:], columns=["Salary"])
        st.area_chart(chart_data)
        print("called 5")

    
    st.write("""
    ### Box Plot of Salaries to Identify Outliers
    """)
    agreement = st.button("Click to see Box Plot of Salaries")
    if agreement:
        fig , ax = plt.subplots(1,1, figsize=(12,7))
        survey_df.boxplot('Salary' , 'Country' , ax=ax)
        plt.suptitle("Salary USD vs Country")
        plt.title("")
        plt.ylabel("Salary")
        plt.xticks(rotation=90)
        st.pyplot(fig)
        print("called 6")
    

    st.write("""
    ### Box Plot of Years of Experience to Identify Outliers
    """)
    agreement = st.button("Click to see Box Plot of Years of Experience")
    if agreement:
        fig , ax = plt.subplots(1,1, figsize=(12,7))
        survey_df.boxplot('YearsCodePro' , 'Country' , ax=ax)
        plt.suptitle("Years of Experience vs Country")
        plt.title("")
        plt.ylabel("Experience")
        plt.xticks(rotation=90)
        st.pyplot(fig)
        print("called 7")
