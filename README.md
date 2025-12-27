# AI-Echo-Your-Smartest-Conversational-Partner
NLP-powered Streamlit dashboard for sentiment analysis of user reviews with interactive insights, trends, and feedback visualization.
📊 Sentiment Analysis Dashboard – AI Echo

An interactive Sentiment Analysis system that analyzes user reviews to understanding user opinions, trends, and feedback patterns.
The project combines Natural Language Processing (NLP), Machine Learning, and Streamlit to answer key business questions related to user sentiment.



🚀 Project Overview

This project focuses on analyzing user reviews by classifying them into Positive, Neutral, and Negative sentiments and visualizing insights through an interactive dashboard.

It helps answer questions such as:

1. What is the overall user sentiment?

2. How does sentiment vary by rating, platform, and time?

3. What keywords dominate positive or negative feedback?

4. Are verified users more satisfied?

5. What are the common negative feedback themes?



🧠 Project Components:

1️⃣ Jupyter Notebook (conversationalpartner.ipynb)

1. Data cleaning & preprocessing

2. Text normalization and feature extraction
 
3. Sentiment labeling
 
4. Exploratory Data Analysis (EDA)
 
5. Model preparation and validation



Domain:
   Customer Experience & Business Analytics


2️⃣ Streamlit Application (senapp.py)

1. Interactive dashboard for sentiment insights
 
2. Filters by platform and rating
 
3. Visualizations using charts and word clouds
 
4. Safe handling of missing metadata (e.g., ChatGPT version)


📂 Project Structure
├── conversationalpartner.ipynb   # Model building & analysis
├── senapp.py                               # Streamlit dashboard
├── data/
│   └── cleaned_reviews.csv          # Preprocessed dataset
├── requirements.txt
└── README.md


📊 Key Questions Answered

1.Overall Sentiment Distribution
Displays the proportion of Positive, Neutral, and Negative reviews.

2.Sentiment vs Rating
Analyzes mismatch between numeric ratings and actual sentiment.

3.Keywords per Sentiment
Uses word clouds to highlight dominant terms for each sentiment.

4.Sentiment Over Time
Monthly sentiment trends to detect satisfaction or dissatisfaction spikes.

5.Verified Users vs Sentiment
Compares sentiment between verified and non-verified users.

6.Platform-Based Sentiment
Identifies differences in sentiment across platforms.

7.ChatGPT Version vs Sentiment
Displays sentiment per version if metadata is available, otherwise handled safely.

8.Negative Feedback Themes
Visualizes common pain points from negative reviews using word clouds.



🛠️ Technologies Used

- [ ] Python

- [ ] Streamlit
 
- [ ] Pandas

- [ ] Matplotlib

- [ ] WordCloud

- [ ] Scikit-learn

- [ ] spaCy (for NLP preprocessing)

- [ ] Jupyter Notebook



 ⚠️ Notes & Assumptions

*The dataset does not include ChatGPT version metadata by default.
  The dashboard safely displays a warning when unavailable.

*Sentiment labels used:
  positive, neutral, negative


🎯 Use Cases

1.User experience analysis

2.Product feedback monitoring

3.Academic NLP projects

4.Business decision support


👩‍💻 Author

Tamilselvi | M.Sc. Software Engineering

📊 Project: Sentiment Analysis – AI Echo
🛠️ Technologies: NLP | Machine Learning | Streamlit
