
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="ProThaali",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 ProThaali")
st.subheader("Your Personalized Vegetarian Meal Recommendation System")

st.write(
    "Find meals based on your protein goals, calorie targets, "
    "and preferred main ingredient."
)

# Load dataset
df = pd.read_csv("prothaali_300_meals.csv")

# Train the ML model
np.random.seed(42)

num_samples = 1000

protein_deviation = np.random.uniform(0, 5, num_samples)
calorie_deviation = np.random.uniform(0, 200, num_samples)

protein_normalized = protein_deviation / 5
calorie_normalized = calorie_deviation / 200

scores = 100 - 50 * (
    0.6 * protein_normalized +
    0.4 * calorie_normalized
)

training_data = pd.DataFrame({
    "protein_deviation_normalized": protein_normalized,
    "calorie_deviation_normalized": calorie_normalized,
    "score": scores
})

X = training_data[
    ["protein_deviation_normalized",
     "calorie_deviation_normalized"]
]

y = training_data["score"]

model = LinearRegression()
model.fit(X, y)

# User inputs
st.sidebar.header("Your Nutrition Goals")

target_protein = st.sidebar.slider(
    "Target Protein (g)",
    min_value=1,
    max_value=40,
    value=25
)

target_calories = st.sidebar.slider(
    "Target Calories (kcal)",
    min_value=100,
    max_value=1000,
    value=400,
    step=50
)

selected_ingredient = st.sidebar.selectbox(
    "Choose Main Ingredient",
    ["Paneer", "Tofu", "Soya", "Eggs"]
)

st.markdown("---")

# Filter meals
recommendation_df = df[
    df["main_ingredient"] == selected_ingredient
].copy()

# Calculate deviations
recommendation_df["protein_deviation_normalized"] = (
    abs(recommendation_df["protein_g"] - target_protein) / 5
)

recommendation_df["calorie_deviation_normalized"] = (
    abs(recommendation_df["calories"] - target_calories) / 200
)

# Predict scores
X_recommendation = recommendation_df[
    ["protein_deviation_normalized",
     "calorie_deviation_normalized"]
]

recommendation_df["score"] = model.predict(X_recommendation)

recommendation_df["score"] = recommendation_df["score"].clip(1, 100)

# Sort recommendations
recommendation_df = recommendation_df.sort_values(
    "score",
    ascending=False
)

top_5 = recommendation_df.head(5)

# Display results
st.header("🏆 Your Top 5 Recommended Meals")

for index, meal in top_5.iterrows():

    score = meal["score"]

    if score >= 90:
        category = "Excellent Match"
    elif score >= 80:
        category = "Good Match"
    elif score >= 70:
        category = "Decent Match"
    else:
        category = "Less Suitable"

    with st.expander(
        f"{meal['meal_name']} | Score: {score:.2f}/100 | {category}",
        expanded=True
    ):

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Protein", f"{meal['protein_g']} g")

        with col2:
            st.metric("Calories", f"{meal['calories']} kcal")

        with col3:
            st.metric("Match Score", f"{score:.2f}/100")

        st.markdown("### 🧺 Ingredients")
        st.write(meal["ingredients"])

        st.markdown("### 👩‍🍳 Preparation Steps")
        st.write(meal["preparation_steps"])

# Chart
st.markdown("---")
st.header("📊 Recommendation Score Comparison")

chart_data = top_5.set_index("meal_name")["score"]

st.bar_chart(chart_data)

# Full results
st.markdown("---")
st.header("📋 All Matching Meals")

st.dataframe(
    recommendation_df[
        ["meal_name", "main_ingredient", "protein_g",
         "calories", "score"]
    ],
    use_container_width=True
)

st.caption(
    "Nutrition values are estimates. Recommendations are generated "
    "using a machine learning model trained on synthetic scoring data."
)
