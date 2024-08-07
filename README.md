<div align="center">
    <h1>Anime Recommender System</h1>
    <img src="https://miro.medium.com/v2/resize:fit:1400/1*XPHpomPGMCHbvekEQ21C8w.jpeg" alt="Anime Recommender" width="800"/>
</div>


## Table of Contents
- [Project Overview](#project-overview)
  - [Introduction](#introduction)
  - [Use and Benefits](#use-and-benefits)
  - [Key Features](#key-features)
  - [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Embark on Your Journey](#embark-on-your-journey)
  - [Prerequisites](#prerequisites)
  - [Installations](#installations)
  - [Packages](#packages)
- [Usage](#usage)
- [Contributors](#contributors)

## Project Overview
### Introduction
Welcome to the Anime Recommender System project! This repository showcases an innovative recommender system designed to enhance the anime-watching experience by suggesting anime titles tailored to individual preferences. The system employs a blend of advanced collaborative and content-based recommendation algorithms to deliver highly relevant and personalized suggestions.

In the realm of anime recommendations, users often face the challenge of finding new titles that match their tastes amidst a vast array of options in the anime universe. This system addresses this challenge by leveraging sophisticated machine learning techniques to analyze user preferences and anime attributes. By doing so, it aims to offer users a seamless experience in discovering new anime that aligns with their interests and viewing history, whether they are into shounen, shoujo, mecha, or slice of life.

This project is a culmination of data science, machine learning, and web development, integrating various technologies and methodologies to provide a robust and user-friendly recommendation engine. Whether someone is an anime enthusiast looking to expand their watchlist with hidden gems and popular series alike, or a developer interested in the intricacies of recommender systems, this project offers valuable insights and a practical application of machine learning techniques. Users can get ready to dive into the world of anime with tailored recommendations just for them!
### Use and Benefits
The Anime Recommender System is designed to assist users in discovering new anime that perfectly matches their tastes and preferences. By analyzing historical user data and anime attributes, the system provides personalized recommendations that enhance the overall viewing experience. Here’s how it benefits users:

- **Personalized Recommendations**: The system leverages collaborative filtering, which analyzes user behavior and preferences to suggest anime that similar users have enjoyed. This ensures that the recommendations are tailored to individual tastes.

- **Content-Based Suggestions**: By examining the attributes and genres of anime titles, the system offers suggestions based on the specific characteristics of the anime that users have already shown interest in. This method helps in discovering new titles with similar themes or styles.

- **Enhanced Discovery**: With a vast library of anime titles available, finding the right one can be overwhelming. The recommender system simplifies this process by providing curated suggestions that align with user preferences, making it easier to find the next favorite show.

- **Interactive User Experience**: Integrated with Streamlit, the application provides an interactive and intuitive interface for users to input their preferences and receive real-time recommendations. This enhances user engagement and satisfaction.

Overall, the Anime Recommender System not only helps users find new and exciting anime but also provides valuable insights into the mechanics of recommendation algorithms and their application in real-world scenarios.
### Key Features

- **Model Selection**: Users can choose between three recommendation models:
  - **NMF Model**: Utilizes Non-negative Matrix Factorization to generate predictions based on historical user preferences.
  - **Content-Based Model**: Recommends anime by analyzing the content and attributes of the input titles.
  - **Hybrid Model**: Combines the strengths of both the NMF and content-based models to offer more accurate and personalized recommendations.

- **Interactive User Interface**: The app features a user-friendly interface built with Streamlit, making it easy for users to input their favorite anime and receive recommendations.

- **Personalized Recommendations**: Provides tailored suggestions based on the user’s input, enhancing the discovery of new anime that matches individual tastes.

- **Exploratory Data Analysis (EDA)**: Includes visualizations and insights on anime distribution, genres, and ratings, allowing users to explore data trends and patterns.

- **Dynamic Background and Imagery**: Utilizes a visually appealing background and logo to create an engaging and immersive experience for users.

- **Real-Time Feedback**: The app generates recommendations in real-time, ensuring that users receive immediate and relevant suggestions based on their preferences.

- **Continuous Improvement**: The recommendation algorithms are refined using MLflow for hyperparameter tuning and performance tracked through Kaggle submissions to ensure high-quality suggestions.

- **Comprehensive Information**: The "About" page provides detailed information on how the recommendation system works and the models used, giving users insights into the underlying mechanics.

These features combine to create a robust and user-centric anime recommendation system that caters to both casual viewers and anime enthusiasts alike.

### How It Works
The Anime Recommender System uses a complex approach by integrating both collaborative and content-based recommendation methods to provide highly accurate and personalized suggestions.

**Collaborative Filtering**: This method relies on the analysis of user interactions, such as ratings and viewing histories. By identifying patterns in how users with similar preferences interact with various anime titles, the system can suggest new anime that have been well-received by users with comparable tastes. Collaborative filtering helps in recommending anime based on the collective behavior and preferences of a community of users, effectively leveraging the wisdom of the crowd.

**Content-Based Filtering**: In parallel, content-based filtering focuses on the attributes and characteristics of anime titles themselves. By examining features such as genres, themes, and plot elements, the system can recommend anime that align with the specific attributes of titles that users have previously shown interest in. This method ensures that recommendations are relevant to the user’s interests and preferences based on the content of the anime.

**Continuous Improvement and Performance Tracking**: The system is designed to adapt and improve over time. Using MLflow, the model undergoes regular refinement through hyperparameter tuning, optimizing its performance to deliver better recommendations. MLflow tracks the experiments and allows for systematic adjustments to the model parameters to enhance accuracy. Additionally, the performance of the recommender system is evaluated and validated through ongoing submissions to Kaggle competitions. This competitive platform provides insights into how the model performs against benchmarks and other systems, ensuring that it remains state-of-the-art.

By combining these advanced techniques and continuously refining the model, the Anime Recommender System aims to offer users a seamless and engaging experience in discovering new anime tailored to their unique preferences.

## Project Structure

Explore the layout of the Anime Recommender System with this organized structure designed to enhance your development journey:

1. **base_app.py**: The epicenter of the project, this Streamlit application file brings the anime recommender system to life with an interactive user interface.
2. **anime_df_cleaned.csv**: The star player! This vital dataset, sitting at the root of the project, fuels the recommendation engine with all the anime goodness.
3. **models/**: Where the magic happens! This folder contains pickled model files that have been meticulously trained and tuned for precise anime recommendations.
4. **README.md**: The scroll that contains the lore of the project, including essential information and instructions to guide you through the setup and usage of the recommender system.
5. **requirements.txt**: The scroll that lists all the necessary Python packages required to run the application, ensuring you have all the right tools for a smooth setup.                                                                                         
This structure ensures that each component is neatly organized and easily accessible.

## Embark on Your Journey
Prepare to dive into the world of anime recommendations with the following steps.

### Prerequisites
Prepare your battle gear with the following:
- Python 3.9
- Pip (Python package manager)

### Installations
Get ready for your anime adventure by setting up the environment with these steps!

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/justin9503/Anime-Recommendation-system.git
   cd Anime-Recommender-system
   ```
2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit App:**
    ```bash
   streamlit run base_app.py
   ```

### Packages
To carry out all the objectives for this repository, the following necessary dependencies need to be loaded:

- Pandas 2.2.2
- Numpy 1.26.4
- Scikit-learn
- Streamlit
  
## Usage

The Anime Recommender System uses a combination of collaborative and content-based filtering to provide personalized anime recommendations. Here’s a step-by-step guide to using the app:

1. **Access the App**: Open the Anime Recommender System app using the following link: [Anime Recommender System App](https://justin9503-anime-recommender-system-base-app-bc2a21.streamlit.app/)

2. **Select the Model**: In the sidebar, choose the recommendation model you want to use:
   - **NMF Model**: This model uses Non-negative Matrix Factorization to predict ratings.
   - **Content-Based Model**: This model suggests anime based on content similarity to the input titles.
   - **Hybrid Model**: This model combines both NMF and content-based approaches for enhanced recommendations.

3. **Enter Favorite Anime**: Input the names of three anime titles you enjoy in the provided text fields. These titles will be used as a reference to generate recommendations.

4. **Get Recommendations**: Click the “Get Recommendations” button to receive personalized anime suggestions based on the selected model. The app will display a list of recommended anime with their ratings and types.

5. **Explore Data**: Navigate to the "EDA" page to view various visualizations and insights about anime distribution, genres, ratings, and more.

6. **Learn More**: Visit the "About" page to get information about how the app works and the models used for recommendations.


## Contributors

| Name                                                                                        | Email                           |
|---------------------------------------------------------------------------------------------|---------------------------------|
| [Justin Ndivhuwo Tshifaro](https://github.com/justin9503) (Team Lead)                      | Njtshifaro@gmail.com             |
| [Mahlatse Hunadi Masemola](https://github.com/MahlatseMasemola) (Project Manager)           | masemola.hunadi@gmail.com        |
| [Zwiitwaho Mugodo](https://github.com/ZweeteM)                                               | mugodozwiitwaho@gmail.com        |
| [Mbalenhle Lenepa](https://github.com/Mbali0901)                                            | lenepembali@gmail.com            |
| [Lungile Faith Baloyi](https://github.com/LFBaloyi19)                                       | lfbaloyi@gmail.com               |

