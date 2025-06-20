import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load your dataset (update filename if needed)
df = pd.read_csv("Crop_recommendation.csv")

# Select input features (update column names if needed)
X = df.drop(columns=["label"])  # If "label" is the target column

# Train StandardScaler
scaler = StandardScaler()
scaler.fit(X)

# Save the scaler to standscaler.pkl
with open("standscaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ standscaler.pkl created successfully!")
