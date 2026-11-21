
# 🥗 ProThaali – Personalized Vegetarian Meal Recommendation System

## 📌 Project Overview
ProThaali is a machine-learning-based vegetarian meal recommendation system that helps users discover meals according to their protein and calorie requirements.

Users can select a main ingredient, set their nutritional targets, and receive suitable meal recommendations through an interactive Streamlit application.

## 🎯 Objectives
- Recommend vegetarian meals based on nutritional requirements.
- Provide ingredient-based meal filtering.
- Display meal ingredients and preparation steps.
- Use a machine learning model to estimate meal suitability scores.
- Make healthy meal discovery simple and interactive.

## ✨ Features
- 300 vegetarian meals across four ingredient categories.
- Categories: Paneer, Tofu, Soya and Eggs.
- Search and filter meals.
- Personalized top-five meal recommendations.
- Protein and calorie-based scoring.
- Ingredients and preparation instructions.
- Interactive Streamlit interface.
- Data visualizations.

## 🧠 Machine Learning Methodology
ProThaali uses a Linear Regression model trained on synthetically generated examples based on a predefined nutritional scoring formula.

The scoring formula is:

Score = 100 − 50 × (0.6 × Pn + 0.4 × Cn)

Where:
- Pn = Absolute protein deviation / 5
- Cn = Absolute calorie deviation / 200

Protein deviation is assigned 60% weight, while calorie deviation is assigned 40% weight.

The final score is clipped between 1 and 100. Meals are ranked according to their predicted suitability scores.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Google Colab
- GitHub

## 📂 Project Files
- `app.py` – Streamlit application.
- `prothaali_300_meals (1).csv` – Meal dataset containing 300 meals, ingredients, nutrition estimates and preparation steps.
- `ProThaali_ML_Project.ipynb` – Google Colab notebook containing project implementation and analysis.
- `requirements.txt` – Required Python libraries.

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder
```bash
cd YOUR_REPOSITORY_NAME
```

### 3. Install dependencies
```bash
py -m pip install -r requirements.txt
```

### 4. Run the application
```bash
py -m streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset Information
The dataset contains 300 vegetarian meal entries, distributed across four categories:
- Paneer – 75 meals
- Tofu – 75 meals
- Soya – 75 meals
- Eggs – 75 meals

Each entry includes the meal name, main ingredient, estimated protein, estimated calories, ingredients and preparation steps.

## ⚠️ Limitations
- Nutrition values are estimates and may vary with ingredients and serving sizes.
- Training labels are synthetically generated using the scoring formula, not collected from real user preferences.
- Recommendations are based on nutritional similarity and selected ingredient category.

## 🔮 Future Scope
- Integration with verified nutrition databases.
- User feedback-based recommendations.
- Personalized weekly meal planning.
- Improved nutritional and dietary filters.
- Mobile-friendly application.

## 👩‍💻 Project Information
**Project Name:** ProThaali  
**Domain:** Artificial Intelligence and Machine Learning  
**Application:** Streamlit-based Vegetarian Meal Recommendation System
