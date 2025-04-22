import os
import joblib
from sklearn.preprocessing import LabelEncoder

# Dummy label encoder example (replace with your actual encoder)
le_target = LabelEncoder()
le_target.classes_ = ["Healthy", "Insomnia", "Sleep Apnea"]  # Add correct class names

# Define the directory and file paths
save_dir = "C:\\Users\\Ramya\\Downloads\\Major Project"
target_encoder_path = os.path.join(save_dir, "target_encoder.pkl")

# Ensure the directory exists
os.makedirs(save_dir, exist_ok=True)

# Save the LabelEncoder
joblib.dump(le_target, target_encoder_path)

print(f"Target encoder saved at: {target_encoder_path}")
