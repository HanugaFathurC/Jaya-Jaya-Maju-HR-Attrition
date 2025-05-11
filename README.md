# 📊 Business Dashboard Project: Jaya Jaya Maju

It focuses on solving employee attrition issues in the fictional company **Jaya Jaya Maju**, using data exploration, business dashboarding with Metabase, and machine learning modeling.

---

## 🚀 Project Objective

To assist the HR department in identifying and monitoring the key factors that contribute to high employee attrition (more than 10%) using a data-driven business dashboard and predictive model.

---

## 📘 Contents

- `README.md` - Project overview.
- `documentation.md` - Project documentation.
- `rf_model.pkl` - Machine Learning model training script using Random Forest + SMOTE.
- `scaler.pkl` - Scaler for preprocessing the data.
- `prediction.py` - File for making predictions using the trained model.
- `cleaned_employee_data.csv` - Processed dataset used for modeling.
- `employee_data.csv` - Original dataset containing employee information.
- `notebook.ipynb` - Jupyter Notebook containing the modeling process.
- `metabase.db.mv.db` - Exported Metabase database file containing saved questions and dashboards.

---

## 📈 Business Dashboard

This dashboard was built using **Metabase** and includes the following key visualizations:

- **Attrition by Department**
- **Attrition by Job Satisfaction**
- **Attrition by WorkLifeBalance**
- **Attrition Rate**
- **Monthly Income Distribution of Employees Who Left**
- **Years at Company vs Attrition**

> 📂 Dashboard stored in: `metabase.db.mv.db`

### 🧪 How to Load the Dashboard

To view the dashboard locally:

```bash
docker run -d -p 3000:3000 --name metabase \
  -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
  metabase/metabase
```

Then, open your browser and navigate to `http://localhost:3000` to access the Metabase dashboard.

If you want to use the Metabase dashboard, you can use the following credentials:
```plaintext
Email: hans@mail.com
Password: metabase-root123-hans
```

> Note: Ensure you have Docker installed and running on your machine.

## 🧠 Machine Learning
A classification model was developed to predict whether an employee is likely to leave the company. 
The modeling process focused on identifying patterns in the data that indicate potential attrition, which can help the HR department take proactive measures.

### ✅ Approach

- **Algorithm Used**: Random Forest Classifier
- **Imbalance Handling**: SMOTE (Synthetic Minority Over-sampling Technique)
- **Training Environment**: Jupyter Notebook with scikit-learn, imbalanced-learn, and pandas
- **Model Evaluation**: Precision, Recall, F1-score, and confusion matrix

### 🧪 Model Performance
**Overall Accuracy** :        0.844      

### 🚀 How to Run the Model

After training the model, it was exported using `joblib`. 
You can test new employee data using the `prediction.py`.

#### 1. Install Required Libraries

Make sure the following packages are installed:

```bash
pip install pandas scikit-learn joblib
```

#### 2. Run the Prediction Script
```bash
python prediction.py
```




