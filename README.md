# 💰 Superstore Profit Prediction using Machine Learning

## 📌 Project Overview

This project is an end-to-end Machine Learning Regression Project developed using the Superstore dataset.

The objective of this project is to predict the expected **Profit** of an order based on features like:

- Sales
- Quantity
- Discount
- Category
- Region
- Ship Mode
- Segment
- Delivery Days

The project includes:

✔ Data Preprocessing  
✔ Exploratory Data Analysis (EDA)  
✔ Feature Engineering  
✔ Model Building  
✔ Hyperparameter Tuning  
✔ Cross Validation  
✔ Streamlit Web App Deployment

---

# 🎯 Business Problem

Many retail businesses generate high sales but still suffer low profits due to:

- Excessive discounts
- Poor pricing strategies
- Regional inefficiencies
- High operational costs

This project helps businesses predict future profit and identify loss-making orders before finalizing sales.

---

# 🎯 Business Objectives

- Predict expected order profit
- Detect potential loss-making orders
- Understand factors affecting profitability
- Improve discount strategy
- Build an interactive prediction system

---

# 📂 Dataset Information

Dataset Used: **Superstore Dataset**

### Dataset Features

| Column | Description |
|--------|-------------|
| Ship Mode | Shipping method |
| Segment | Customer segment |
| Region | Sales region |
| Category | Product category |
| Sub-Category | Product sub-category |
| Sales | Total sales amount |
| Quantity | Quantity ordered |
| Discount | Discount applied |
| Profit | Target variable |

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

# ⚙️ Machine Learning Workflow

## 1️⃣ Data Preprocessing
- Missing value checking
- Duplicate removal
- Data type inspection

## 2️⃣ Exploratory Data Analysis
- Profit distribution
- Sales vs Profit analysis
- Discount impact analysis
- Category-wise and Region-wise analysis

## 3️⃣ Feature Engineering
Created new features:
- Delivery Days
- Order Month
- Order Year
- Discount Amount
- Unit Price

## 4️⃣ Encoding
Applied One-Hot Encoding for categorical variables.

## 5️⃣ Model Building
Models Used:
- Linear Regression
- KNN Regressor
- Decision Tree Regressor
- Random Forest Regressor

## 6️⃣ Hyperparameter Tuning
Used GridSearchCV to optimize model parameters.

## 7️⃣ Cross Validation
Performed 5-Fold Cross Validation for model stability.

---

# 📊 Model Performance

| Model | R² Score |
|------|----------|
| Random Forest Regressor | 0.8347 |
| Decision Tree Regressor | 0.6921 |
| Linear Regression | 0.5573 |
| KNN Regressor | 0.4827 |

### ✅ Best Model
Random Forest Regressor

---

# 📈 Key Insights

- Technology category generated highest profit
- West region showed best performance
- High discounts significantly reduced profit
- Some orders generated losses despite high sales

---

# 🌐 Streamlit Web Application

The project includes an interactive Streamlit web application where users can:

- Enter order details
- Predict expected profit/loss
- View business recommendations

---

# ⭐ Conclusion

This project successfully transforms historical retail data into a predictive machine learning system capable of estimating future profit with high accuracy.

The final Random Forest model achieved an R² Score of approximately 83.4% and was deployed using Streamlit for real-time prediction.
