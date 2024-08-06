import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import csr_matrix
from PIL import Image
import base64
from sklearn.decomposition import TruncatedSVD

# Load models and data
with open('nmf.pkl', 'rb') as f:
    nmf_model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

anime_df_cleaned = pd.read_csv('anime_df_cleaned.csv')

# Create the TF-IDF matrix and reduce its dimensions
tfidf_matrix = tfidf_vectorizer.fit_transform(anime_df_cleaned['genre'])
svd = TruncatedSVD(n_components=100)
tfidf_matrix_reduced = svd.fit_transform(tfidf_matrix)

# Convert to sparse matrix
tfidf_matrix_sparse = csr_matrix(tfidf_matrix_reduced)

# Compute cosine similarity using the sparse matrix
cosine_sim = linear_kernel(tfidf_matrix_sparse, tfidf_matrix_sparse)

# Function to get recommendations based on cosine similarity
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in anime_df_cleaned['name'].values:
        return []
    idx = anime_df_cleaned[anime_df_cleaned['name'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    anime_indices = [i[0] for i in sim_scores]
    return anime_df_cleaned[['name', 'rating', 'type']].iloc[anime_indices].values.tolist()

# Predict ratings using the hybrid approach
def hybrid_predict(user_id, anime_id, nmf_model, cosine_sim):
    nmf_pred = nmf_model.predict(user_id, anime_id).est
    idx = anime_df_cleaned[anime_df_cleaned['anime_id'] == anime_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    sim_anime_indices = [i[0] for i in sim_scores]
    content_pred = np.mean([nmf_model.predict(user_id, anime_df_cleaned.iloc[aid]['anime_id']).est for aid in sim_anime_indices])
    hybrid_pred = 0.7 * nmf_pred + 0.3 * content_pred
    return hybrid_pred

# Get recommendations based on an anime name using hybrid approach
def get_recommendations_hybrid(anime_name, nmf_model, cosine_sim, anime_df):
    if anime_name not in anime_df['name'].values:
        return []
    idx = anime_df[anime_df['name'] == anime_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    sim_anime_indices = [i[0] for i in sim_scores]
    recommendations = []
    for i in sim_anime_indices:
        user_id = 1
        anime_id = anime_df.iloc[i]['anime_id']
        hybrid_rating = hybrid_predict(user_id, anime_id, nmf_model, cosine_sim)
        recommendations.append((anime_df.iloc[i]['name'], hybrid_rating, anime_df.iloc[i]['type']))
    return recommendations

# Function to set background image
def set_background(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    # Load images
    logo = Image.open("Pictures/anime2_logo.jpeg")
    background = "Pictures/back7.jpg"
    eda1 = Image.open("Pictures/Distribution of Anime types.png")
    eda2 = Image.open("Pictures/Common genre.png")
    eda3 = Image.open("Pictures/Top 10 most rated animes.png")
    eda4 = Image.open("Pictures/User_anime_rating distribution.png")
    eda5 = Image.open("Pictures/Averarage anime rating by anime type.png")
    eda6 = Image.open("Pictures/Box_plots.png")
    
    # Set background image
    set_background(background)
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "EDA", "About"])

    # Page content
    if page == "Home":
        st.title("Anime Recommendation System")
        st.image(logo, width=500) 
        model_choice = st.selectbox(
            "Choose a model",
            ("NMF Model", "Content-Based Model", "Hybrid Model")
        )
        first_anime = st.text_input("Enter your first favorite anime")
        second_anime = st.text_input("Enter your second favorite anime")
        third_anime = st.text_input("Enter your third favorite anime")

        if st.button("Get Recommendations"):
            favorite_anime = [first_anime, second_anime, third_anime]
            recommendations = []

            if model_choice == "NMF Model":
                for anime in favorite_anime:
                    recommendations.extend(get_recommendations(anime, cosine_sim))
            elif model_choice == "Content-Based Model":
                for anime in favorite_anime:
                    recommendations.extend(get_recommendations(anime, cosine_sim))
            elif model_choice == "Hybrid Model":
                for anime in favorite_anime:
                    recommendations.extend(get_recommendations_hybrid(anime, nmf_model, cosine_sim, anime_df_cleaned))

            if recommendations:
                st.write("Recommendations:")
                for i, rec in enumerate(recommendations):
                    background_color = "#f0f0f0" if i % 2 == 0 else "#ffffff"
                    st.markdown(f"""
                    <div style="background-color: {background_color}; padding: 10px; border-radius: 5px;">
                        <p><b>Name:</b> {rec[0]}</p>
                        <p><b>Rating:</b> {rec[1]}</p>
                        <p><b>Type:</b> {rec[2]}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("No recommendations found for the given anime titles.")

    elif page == "EDA":
        st.title("Exploratory Data Analysis")
        st.image(eda1, caption='Distribution of Anime Types', use_column_width=True)
        st.image(eda2, caption='Common Genre', use_column_width=True)
        st.image(eda3, caption='Top 10 most rated anime', use_column_width=True)
        st.image(eda4, caption='User and anime_rating distribution', use_column_width=True)
        st.image(eda5, caption='Average anime rating by anime type', use_column_width=True)
        st.image(eda6, caption='Box plots', use_column_width=True)


    elif page == "About":
        st.title("About")
        st.write("""
        This application is designed to recommend anime based on user preferences.
        It uses three models:
        - **NMF Model**: Non-negative Matrix Factorization
        - **Content-Based Model**: Recommendations based on content similarity
        - **Hybrid Model**: A combination of the above two models
        
        The user can input their three favorite anime, and the app will provide recommendations based on the selected model.
        """)

    # Add footer
    footer = """
    <div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: white; color: black; text-align: center; padding: 10px;">
        <p>Designed by TeamEG3 | Contact: +36 20 265 9496, WhatsApp, Email: njtshifaro@gmail.com</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
