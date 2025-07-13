# Course Recommendation System

A content-based course recommendation system that suggests online courses based on users' interests and preferences. Built using Jupyter Notebook and Python, the system utilizes a dataset of online courses (e.g., from Coursera) and applies natural language processing techniques to recommend similar courses.

## Features

- **Course Data Analysis:** Loads and processes a dataset containing thousands of courses with their names, descriptions, difficulty levels, and taught skills.
- **Content-Based Recommendations:** Builds a recommendation engine using course metadata and text similarity.
- **Custom Tagging:** Combines course name, difficulty, description, and skills for richer matching.
- **User Input:** Recommends courses by matching user-provided interests with course tags.
- **Model Saving:** Saves trained models, vectorizers, and processed datasets for easy re-use.

## Dataset

- The system uses a dataset (e.g., `Coursera.csv`) containing columns such as:
  - Course Name
  - Difficulty Level
  - Course Description
  - Skills
  - Course Rating
- The dataset is preprocessed to clean and structure the text, and combined into a single 'tags' column for similarity calculation.

## How It Works

1. **Preprocessing:** Cleans and prepares the course data.
2. **Tag Creation:** Concatenates course metadata into a single string per course.
3. **Vectorization:** Uses `CountVectorizer` to convert tags into vectors.
4. **Similarity Calculation:** Computes similarity between courses using cosine similarity.
5. **Recommendation:** Given a course or set of interests, returns a list of similar/recommended courses.


# Deployed Streamlit App

You can try the live Streamlit web application here:

https://course-recolearn.streamlit.app/

> Replace the above link with the actual deployed URL of your Streamlit app (e.g., on Streamlit Community Cloud or another hosting service).
