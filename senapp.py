import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")
st.title("📊 Key Questions for Sentiment Analysis")
st.write("Interactive analysis of user reviews")

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_reviews.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filters")

platform = st.sidebar.multiselect(
    "Platform",
    df["platform"].unique(),
    default=df["platform"].unique()
)

rating = st.sidebar.multiselect(
    "Rating",
    sorted(df["rating"].unique()),
    default=sorted(df["rating"].unique())
)

df_filt = df[(df["platform"].isin(platform)) & (df["rating"].isin(rating))].copy()

# ---------------- 1️⃣ Overall Sentiment ----------------
st.header("1️⃣ Overall Sentiment")
st.bar_chart(df_filt["sentiment"].value_counts(normalize=True) * 100)

# ---------------- 2️⃣ Sentiment vs Rating ----------------
st.header("2️⃣ Sentiment vs Rating")
st.dataframe(
    pd.crosstab(df_filt["rating"], df_filt["sentiment"], normalize="index")
)

# ---------------- 3️⃣ Keywords per Sentiment ----------------
st.header("3️⃣ Keywords per Sentiment")
sent_choice = st.selectbox("Select Sentiment", df_filt["sentiment"].unique())

text = " ".join(
    df_filt[df_filt["sentiment"] == sent_choice]["review"].astype(str)
)

if text.strip():
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No text available for this sentiment.")

# ---------------- 4️⃣ Sentiment Over Time ----------------
st.header("4️⃣ Sentiment Over Time")

if "date" in df_filt.columns:
    df_filt["date"] = pd.to_datetime(df_filt["date"], errors="coerce")

    trend = (
        df_filt.dropna(subset=["date"])
        .groupby([pd.Grouper(key="date", freq="ME"), "sentiment"])
        .size()
        .unstack()
        .fillna(0)
    )

    st.line_chart(trend)
else:
    st.info("Date column not available.")

# ---------------- 5️⃣ Verified Users vs Sentiment ----------------
st.header("5️⃣ Verified Users vs Sentiment")

if "verified_purchase" in df_filt.columns:
    st.dataframe(
        pd.crosstab(
            df_filt["verified_purchase"],
            df_filt["sentiment"],
            normalize="index"
        )
    )
else:
    st.info("Verified purchase data not available.")

# ---------------- 8️⃣ Platform-Based Sentiment ----------------
st.header("8️⃣ Platform-Based Sentiment")

st.dataframe(
    pd.crosstab(df_filt["platform"], df_filt["sentiment"], normalize="index")
)

# ---------------- 9️⃣ ChatGPT Version vs Sentiment ----------------
st.header("9️⃣ ChatGPT Version vs Sentiment")

if "chatgpt_version" in df_filt.columns:
    st.dataframe(
        pd.crosstab(
            df_filt["chatgpt_version"],
            df_filt["sentiment"],
            normalize="index"
        )
    )
else:
    st.warning("ChatGPT version data not available.")

# ---------------- 🔟 Negative Feedback Themes ----------------
st.header("🔟 Negative Feedback Themes")

neg_reviews = df_filt[df_filt["sentiment"] == "negative"]["review"].astype(str)

if neg_reviews.empty:
    st.write("No negative reviews found.")
else:
    neg_text = " ".join(neg_reviews)
    neg_wc = WordCloud(
        width=800,
        height=400,
        background_color="black"
    ).generate(neg_text)

    fig2, ax2 = plt.subplots()
    ax2.imshow(neg_wc)
    ax2.axis("off")
    st.pyplot(fig2)

st.success("✅ Sentiment Analysis Dashboard Ready")