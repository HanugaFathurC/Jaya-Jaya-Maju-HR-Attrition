import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load model and scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load full dataset
df = pd.read_csv("data/employee_data.csv")

# Drop unused columns
columns_to_drop = ["EmployeeId", "EmployeeCount", "StandardHours", "Over18"]
df = df.drop(columns=columns_to_drop)

# Encode categorical columns (same as training)
categorical_cols = ['Gender', 'OverTime', 'BusinessTravel', 'Department',
                    'EducationField', 'JobRole', 'MaritalStatus']

le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Take 10 random rows from data
sample_data = df.drop(columns=['Attrition']).sample(10, random_state=42)
actual_labels = df.loc[sample_data.index, 'Attrition'].values

# Scale the data
sample_scaled = scaler.transform(sample_data)

# Predict
predicted = model.predict(sample_scaled)

# Display results
for i in range(10):
    actual = 'Leave' if actual_labels[i] == 1 else 'Stay'
    pred = 'Leave' if predicted[i] == 1 else 'Stay'
    print(f"Sample {i+1}: Actual = {actual}, Predicted = {pred}")