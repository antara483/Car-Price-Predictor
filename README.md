# 🚗 Car Price Predictor

An intelligent and interactive Machine Learning web app that predicts the **resale price of a used car** based on its specifications and market trends. This project is built using **Streamlit for the frontend** and a **Random Forest Regression model** trained on real-world car data.

---

## 📌 Project Description

This project aims to help users estimate how much their car is worth in the resale market. It takes into account important features such as:

- Year of manufacture
- Present price
- Kilometers driven
- Fuel type
- Transmission type
- Seller type
- Number of previous owners

Using this information, the app calculates the **car’s age**, encodes categorical variables, and feeds the cleaned data into a trained **Random Forest Regressor** model to provide an accurate price prediction.

It also supports **future year predictions**, allowing users to estimate resale value in coming years based on projected age.

---

## 💡 How It Works

1. 🔍 The user enters car details via an easy-to-use Streamlit interface (dropdowns, sliders, etc.)
2. 🔁 The input data is preprocessed and encoded just like it was during model training
3. 🧠 The preprocessed data is passed into the trained Random Forest model (`random_forest_model.pkl`)
4. 📊 The app displays the estimated price in Indian Rupees (₹) in lakhs
5. 📅 The app also calculates **car age** dynamically based on the user-selected year and future prediction year

---

## 🧠 Key Features

- Predicts **resale car prices** based on real features
- Uses **Random Forest Regression** for better accuracy
- Accepts **future year predictions**
- Clean, modern UI built with Streamlit
- Lightweight and runs locally or on cloud

---


---

## 🧪 Model Used

- **Algorithm**: Random Forest Regressor
- **Library**: scikit-learn
- **Trained on**: 301 entries of used car data
- **Target Variable**: Selling Price
- Saved as: `random_forest_model.pkl` using `joblib`

---

## 🚀 How to Run the Project

### 📦 Install requirements

```bash
pip install -r requirements.txt
streamlit run app.py


