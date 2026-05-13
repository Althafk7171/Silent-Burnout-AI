import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ------------------- LOAD MODEL -------------------
try:
    BASE_DIR = Path(__file__).resolve().parent

    model = joblib.load(BASE_DIR / "models" / "gradient_boosting_model.pkl")
    imputer = joblib.load(BASE_DIR / "models" / "imputer.pkl")
    feature_order = joblib.load(BASE_DIR / "models" / "feature_order.pkl")

except Exception as e:
    st.error(f"Error loading model files: {e}")
    
# ------------------- UI -------------------
st.set_page_config(page_title="Silent Burnout AI", layout="wide")

st.title("Silent Burnout Detection System")
st.write("Predict student disengagement using behavioral and academic data.")

# ------------------- INPUT SECTION -------------------
st.header("Enter Student Data")

col1, col2 = st.columns(2)

with col1:
    total_clicks = st.number_input("Total LMS Clicks", min_value=0)
    active_days = st.number_input("Active Days", min_value=0)
    avg_clicks_per_day = st.number_input("Avg Clicks per Day", min_value=0.0)
    unique_resources_accessed = st.number_input("Resources Accessed", min_value=0)
    engagement_change = st.number_input("Engagement Change")

with col2:
    engagement_span = st.number_input("Engagement Span (days)")
    engagement_variability = st.number_input("Engagement Variability")
    avg_score = st.number_input("Average Score", min_value=0.0, max_value=100.0)
    assessments_submitted = st.number_input("Assessments Submitted", min_value=0)
    score_std = st.number_input("Score Std Dev")

# ------------------- PREDICTION -------------------
if st.button("🔍 Predict Risk"):

    user_input = {
        "total_clicks": total_clicks,
        "active_days": active_days,
        "avg_clicks_per_day": avg_clicks_per_day,
        "unique_resources_accessed": unique_resources_accessed,
        "engagement_change": engagement_change,
        "engagement_span": engagement_span,
        "engagement_variability": engagement_variability,
        "avg_score": avg_score,
        "assessments_submitted": assessments_submitted,
        "score_std": score_std
    }

    input_df = pd.DataFrame([user_input])
    input_df = input_df.reindex(columns=feature_order, fill_value=0)
    input_processed = input_df

    prediction = model.predict(input_processed)
    probability = model.predict_proba(input_processed)

    # ------------------- RESULT -------------------
    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("🟢 Low Risk Student")
    elif prediction[0] == 1:
        st.warning("🟡 Moderate Risk Student")
    else:
        st.error("🔴 High Risk / Potential Withdrawal")

    st.write(f"Confidence: {max(probability[0])*100:.2f}%")

    # ------------------- GRAPH SECTION -------------------
    col3, col4 = st.columns([1, 1])

    # ---------- Bar Chart ----------
    with col3:
        st.subheader("Risk Probability Distribution")

        labels = ["Low", "Medium", "High"]
        values = probability[0]

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.bar(labels, values)
        ax.set_ylabel("Probability")

        st.pyplot(fig)

    # ---------- Radar Chart ----------
    with col4:
        st.subheader("Student Engagement Profile")

        radar_features = [
            "Clicks",
            "Days",
            "Clicks/Day",
            "Resources",
            "Score"
        ]

        values = [
            total_clicks,
            active_days,
            avg_clicks_per_day,
            unique_resources_accessed,
            avg_score
        ]

        # Normalize values
        values = [
            total_clicks / 1000,
            active_days / 30,
            avg_clicks_per_day / 50,
            unique_resources_accessed / 50,
            avg_score / 100
        ]

        values += values[:1]
        angles = np.linspace(0, 2*np.pi, len(radar_features), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))

        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)

        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.2)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(radar_features)

        st.pyplot(fig)
