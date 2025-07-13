import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset and precomputed model
@st.cache_resource
def load_data_and_model():
    data = pd.read_csv('Coursera.csv')
    with open('context_aware_recommendation_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return data, model

coursera_data, loaded_model = load_data_and_model()

# Load the vectorizer and similarity matrix
tfidf_vectorizer = loaded_model['tfidf_vectorizer']
similarity_matrix = loaded_model['similarity_matrix']

# Custom CSS for styling
st.markdown("""
    <style>
        .course-table {
            width: 100%;  /* Make table occupy the full width */
            margin: auto;
            border-collapse: collapse;
            table-layout: auto; /* Adjust column widths automatically */
        }
        .course-table th, .course-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            word-wrap: break-word; /* Enable word wrapping for longer text */
        }
        .course-table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .course-table td {
            font-size: 16px;
        }
        .course-table tr:hover {
            background-color: #f9f9f9; /* Highlight row on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🎓 Context-Aware Course Recommendation System")
st.write("Discover personalized course recommendations based on difficulty level and skill similarity. Select your preferences and view tailored course options.")

# Sidebar for user inputs
st.sidebar.header("Preferences")
user_difficulty = st.sidebar.selectbox("Select Difficulty Level:", coursera_data['Difficulty Level'].unique())
top_n = st.sidebar.slider("Number of Recommendations:", 1, 10, 5)

# Pre-filtering recommendation function
def recommend_courses_pre_filter(data, difficulty, top_n):
    filtered_data = data[data['Difficulty Level'] == difficulty]
    indices = filtered_data.index
    similarity_scores = similarity_matrix[indices].mean(axis=1)
    top_courses = filtered_data.iloc[np.argsort(similarity_scores)[-top_n:]]
    return top_courses[['Course Name', 'University', 'Difficulty Level', 'Course Rating', 'Skills']].reset_index(drop=True)

# Post-filtering recommendation function
def recommend_courses_post_filter(data, difficulty, top_n):
    indices = data.index
    difficulty_filtered_indices = data[data['Difficulty Level'] == difficulty].index
    similarity_scores = similarity_matrix[difficulty_filtered_indices].mean(axis=1)
    top_courses = data.iloc[difficulty_filtered_indices[np.argsort(similarity_scores)[-top_n:]]]
    return top_courses[['Course Name', 'University', 'Difficulty Level', 'Course Rating', 'Skills']].reset_index(drop=True)

# Recommendation method selection
st.sidebar.subheader("Recommendation Method")
recommendation_type = st.sidebar.radio("Choose Method:", ("Pre-filtering", "Post-filtering"))

# Generate recommendations based on method
if recommendation_type == "Pre-filtering":
    recommendations = recommend_courses_pre_filter(coursera_data, user_difficulty, top_n)
else:
    recommendations = recommend_courses_post_filter(coursera_data, user_difficulty, top_n)

# Ensure Course Rating is displayed as a numeric value
recommendations['Course Rating'] = pd.to_numeric(recommendations['Course Rating'], errors='coerce').round(1)

# Display Recommendations
st.subheader(f"{recommendation_type} Recommendations for {user_difficulty} Level")
st.write("Below are the top recommended courses based on your preferences:")

# Generate HTML table with responsive CSS
html_table = recommendations.to_html(
    classes='course-table',
    index=False,
    escape=False,
    float_format="{:.1f}".format,
)

# Embed the table HTML directly
st.markdown(html_table, unsafe_allow_html=True)
