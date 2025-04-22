import os
import joblib
from sklearn.preprocessing import LabelEncoder

# Initialize LabelEncoders for categorical variables
label_encoders = {
    "Gender": LabelEncoder(),
    "BMI Category": LabelEncoder(),
    "Blood Pressure": LabelEncoder(),
    "Occupation": LabelEncoder()
}

# Fit encoders with actual known values
label_encoders["Gender"].fit(["Male", "Female"])
label_encoders["BMI Category"].fit(["Underweight", "Normal", "Overweight", "Obese"])
label_encoders["Blood Pressure"].fit(["Low", "Normal", "High"])
label_encoders["Occupation"].fit(["Student", "Engineer", "Doctor", "Teacher", "Night Shift", "Morning Shift", "Regular Job", "Other"])

# Define the correct save directory
save_dir = r"C:\Users\Ramya\Downloads\Projetcs\Sleep_Disorder_Prediction"

# Ensure the directory exists
os.makedirs(save_dir, exist_ok=True)

# Define the path to save the encoders
label_encoders_path = os.path.join(save_dir, "target_encoder.pkl")

# Save the encoders
joblib.dump(label_encoders, label_encoders_path)

print(f"✅ Encoders saved successfully at: {label_encoders_path}")
