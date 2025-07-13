# <==== Importing Dependencies ====>

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# <==== Code starts here ====>

# Load data
courses_list = pickle.load(open('D:\\RS\\courses.pkl', 'rb'))
similarity = pickle.load(open('D:\\RS\\similarity.pkl', 'rb'))

def recommend(course):
    # Find index of the selected course
    try:
        index = courses_list[courses_list['course_name'] == course].index[0]
    except IndexError:
        st.error("Selected course not found!")
        return []
    
    # Calculate distances and get top 6 recommendations
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = [courses_list.iloc[i[0]].course_name for i in distances[1:7]]
    
    return recommended_course_names

# Streamlit UI
st.markdown("<h2 style='text-align: center; color: blue;'>Online Learning Content Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)

# Dropdown selection
course_list = courses_list['course_name'].values
selected_course = st.selectbox("Type or select a course you like:", course_list)

# Show recommendations
if st.button('Show Recommended Courses'):
    recommended_course_names = recommend(selected_course)
    if recommended_course_names:
        st.write("Recommended Courses based on your interests are:")
        for name in recommended_course_names:
            st.text(name)
    else:
        st.error("No recommendations found.")

st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>", unsafe_allow_html=True)

# <==== Code ends here ====>
