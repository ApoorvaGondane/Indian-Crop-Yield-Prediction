# 🌾 Indian Crop Yield Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![ML](https://img.shields.io/badge/Model-XGBoost%20%7C%20RandomForest-green)

An end-to-end Machine Learning project that predicts agricultural crop yields in India based on soil, climate, and historical data. This project demonstrates a complete lifecycle from **data cleaning** and **leakage detection** to **feature engineering** and **deployment** via a Streamlit web app.

---

## Medium Article Link
https://medium.com/@apoorvagondane99/from-99-fake-accuracy-to-real-world-impact-building-a-crop-yield-predictor-with-xgboost-636d5cef6275

## 🚀 Project Overview

Predicting crop yield is critical for agricultural planning and food security. This model uses historical data (1997-2020) including **Rainfall, Temperature, Fertilizer, and Pesticide usage** to estimate yield (Tonnes/Hectare) for various crops across Indian states.

### 🎯 Key Objectives
1.  **Solve Real-World Data Issues:** Identified and fixed major data leakage in the original dataset.
2.  **Compare Algorithms:** Benchmarked Random Forest vs. XGBoost to find the optimal model.
3.  **Deployment:** Built an interactive web application for end-users.

---

## 💡 Key Technical Insights (Portfolio Highlights)

This project went beyond basic modeling by addressing specific data challenges:

### 1. Data Leakage Detection 🕵️‍♂️
* **Initial Problem:** The first iteration achieved a suspicious **99% R² score**.
* **Diagnosis:** EDA revealed that the `Production` feature was directly correlated with the target `Yield` ($Yield = Production / Area$).
* **Solution:** Removed `Production` from the training set to ensure the model predicts based on *inputs* (weather, fertilizer) rather than *derived outputs*, resulting in a realistic baseline of ~0.35 R².

### 2. Advanced Feature Engineering 🛠️
To improve the baseline, I engineered domain-specific features:
* **Input Density:** Converted raw usage to density metrics (`Fertilizer_per_Hectare`, `Pesticide_per_Hectare`). This significantly improved model correlation as absolute volumes are biased by farm size.
* **Regional Grouping:** Aggregated states into agro-climatic zones (North, South, East, West, etc.) to capture geographic weather patterns.
* **Impact:** These features improved the model's predictive power by **~20%** over the baseline.

---

## 📊 Model Performance

I compared multiple algorithms using 5-Fold Cross-Validation:

| Model | R² Score (Avg) | Findings |
| :--- | :--- | :--- |
| **Random Forest** | ~0.60 | Robust, but struggled with extreme outliers. |
| **XGBoost** | ~0.65 | **Best Performer.** Better at handling non-linear relationships and outliers. |

*Note: While academic datasets often yield 90%+ accuracy, real-world agricultural data is subject to high variance due to unmeasured factors (pests, sudden storms). A score of 0.65 represents a strong signal for this specific domain.*

---

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/ApoorvaGondane/Indian-Crop-Yield-Prediction.git](https://github.com/ApoorvaGondane/Indian-Crop-Yield-Prediction.git)
cd Indian-Crop-Yield-Prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
streamlit run app.py
```

## 🔮 Future Scope
Weather API Integration: Fetch real-time weather forecasts for the upcoming season.

Soil Health Data: Incorporate N-P-K (Nitrogen, Phosphorus, Potassium) values for more granular fertilizer recommendations.


Deep Learning: Experiment with LSTM models for time-series forecasting of yield trends.

## 📝 Dataset & Credits
Dataset: Crop Yield in Indian States

External Data: NASA POWER API for supplementary climate data.
