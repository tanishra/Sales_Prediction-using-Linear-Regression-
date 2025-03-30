# Sales Prediction Using Linear Regression

## 📌 Project Overview
This project predicts sales revenue based on advertisement spending across **TV, Radio, and Newspaper**. It utilizes **Multiple Linear Regression** and **Regularization techniques (L1, L2, Elastic Net)** to improve accuracy.

## 📂 Dataset
The dataset consists of three input features:
- **TV** (Amount spent on TV ads)
- **Radio** (Amount spent on Radio ads)
- **Newspaper** (Amount spent on Newspaper ads)

Target Variable:
- **Sales** (Total revenue generated)

## 🔍 Data Preprocessing
1. Checked for missing values (None found ✅)
2. Performed **Multicollinearity Check** (VIF values: TV=2, Radio=3, Newspaper=3 ✅)
3. **Feature Scaling** using **StandardScaler** for both inputs (X) and outputs (y)

## 📊 Model Building
1. **Simple Linear Regression** (One feature at a time)
2. **Multiple Linear Regression** (All features used)
3. **Regularization Techniques**
   - **Lasso (L1)**
   - **Ridge (L2)**
   - **Elastic Net**
4. **Model Performance Evaluation**
   - R² Score for Normal Linear Regression: **0.89**
   - R² Scores for Regularization:
     - L2 (Ridge): **0.887**
     - L1 (Lasso): **0.886**
     - Elastic Net: **0.879**

## 🏆 Model Selection
The **Multiple Linear Regression model without regularization (R² = 0.89)** performed the best and was selected for deployment.

## 🛠️ Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/tanishra/sales-prediction.git
   cd sales-prediction
