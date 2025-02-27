import streamlit as st
import pandas as pd
import openpyxl

st.header("Career Guidance", divider='rainbow')

st.subheader("Top 10 Career Options in 2025", divider='rainbow')

df = pd.read_excel("features/data.xlsx", sheet_name="Sheet1")
st.dataframe(df, width=1000)

field = st.selectbox("Select Career Field You Are Interested In", ["Data Science & Analytics", "Software Eng & IT", "Business", "Healthcare"])

if field == "Data Science & Analytics":
    with st.container(border=True):
        st.subheader("Data Scientist", divider='rainbow')
        st.write("Data Scientists are responsible for collecting, analyzing, and interpreting large datasets to help organizations make informed decisions.")
        st.write("Average Salary: $120,000")
        st.write("Job Growth: 15%")
        st.markdown('''
            Suggested Courses:
            - [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science)
            - [Google Advanced Data Analytics Professional Certificate](https://www.coursera.org/professional-certificates/google-advanced-data-analytics)
            - [Python for Data Science and Machine Learning Bootcamp](https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/?couponCode=24T3MT270225)
        ''')

    with st.container(border=True):
        st.subheader("Data Analyst", divider='rainbow')
        st.write("Data Analysts collect, process, and analyze data to help organizations make data-driven decisions.")
        st.write("Average Salary: $70,000")
        st.write("Job Growth: 20%")
        st.markdown('''
            Suggested Courses:
            - [Google Data Analytics Professional Certificate](https://www.coursera.org/professional-certificates/google-data-analytics)
            - [IBM Data Analyst Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-analyst)
            - [Data Analyst Nanodegree](https://www.udacity.com/course/data-analyst-nanodegree--nd002)
        ''')

elif field == "Software Eng & IT":
    with st.container(border=True):
        st.subheader("Cyber Security Analyst", divider='rainbow')
        st.write("Cyber Security Analysts protect organizations from cyber threats by monitoring, detecting, and responding to security incidents.")
        st.write("Average Salary: $90,000")
        st.write("Job Growth: 10%")
        st.markdown('''
            Suggest Courses:
            - [Google Cybersecurity Professional Certificate](https://www.coursera.org/professional-certificates/google-cybersecurity)
        ''')
            