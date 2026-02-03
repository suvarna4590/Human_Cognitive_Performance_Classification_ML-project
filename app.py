import streamlit as st
import pandas as pd
import pickle
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Cognitive Performance Predictor",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.markdown(
    "<h1 style='text-align: center;'>🧠 Cognitive Performance Predictor</h1>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------------
# Load model
# -------------------------------
@st.cache_resource
def load_model():
    with open("lgbm_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# -------------------------------
# Sidebar - User Inputs
# -------------------------------
st.sidebar.header("📋 Enter Details")

age = st.sidebar.number_input("Age", 0, 100, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
stress_level = st.sidebar.slider("Stress Level (1–10)", 1, 10, 5)
diet_type = st.sidebar.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])
daily_screen_time = st.sidebar.slider("Daily Screen Time (hours)", 0.0, 15.0, 5.0)
exercise_frequency = st.sidebar.selectbox("Exercise Frequency", ["Low", "Medium", "High"])
caffeine_intake = st.sidebar.number_input("Caffeine Intake (mg/day)", 0, 500, 100)
reaction_time = st.sidebar.number_input("Reaction Time (ms)", 100, 1000, 400)
memory_test_score = st.sidebar.slider("Memory Test Score", 0, 100, 50)

# -------------------------------
# Prepare input DataFrame
# -------------------------------
columns = [
    'Age', 'Gender', 'Sleep_Duration', 'Stress_Level',
    'Diet_Type', 'Daily_Screen_Time', 'Exercise_Frequency',
    'Caffeine_Intake', 'Reaction_Time', 'Memory_Test_Score'
]

input_data = pd.DataFrame([[ 
    age,
    gender,
    sleep_duration,
    stress_level,
    diet_type,
    daily_screen_time,
    exercise_frequency,
    caffeine_intake,
    reaction_time,
    memory_test_score
]], columns=columns)

# -------------------------------
# Center - Display Inputs + Prediction
# -------------------------------
st.markdown("### Entered Input Details")

st.dataframe(
    input_data,
    width="stretch"
)
st.divider()

if st.button("Predict Cognitive Performance"):
    prediction = model.predict(input_data)[0]

    st.markdown("### Prediction Result")

    if prediction == 2:
        st.success("🟢 **Cognitive Performance: HIGH**")
    elif prediction == 1:
        st.warning("🟡 **Cognitive Performance: MEDIUM**")
    else:
        st.error("🔴 **Cognitive Performance: LOW**")
