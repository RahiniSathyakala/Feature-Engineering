# ================================
# LEVEL 2 - TASK 3
# Feature Engineering
# ================================

import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# -------------------------------
# 1. Length of Restaurant Name
# -------------------------------

if 'Restaurant Name' in df.columns:
    df['Name Length'] = df['Restaurant Name'].apply(len)
    print("\nName Length Feature Created")
else:
    print("\n'Restaurant Name' column not found")

# -------------------------------
# 2. Length of Address
# -------------------------------

if 'Address' in df.columns:
    df['Address Length'] = df['Address'].apply(len)
    print("Address Length Feature Created")
else:
    print("'Address' column not found")

# -------------------------------
# 3. Encode Table Booking
# -------------------------------

if 'Has Table booking' in df.columns:
    df['Table Booking (Encoded)'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
    print("Table Booking Encoded")
else:
    print("'Has Table booking' column not found")

# -------------------------------
# 4. Encode Online Delivery
# -------------------------------

if 'Has Online delivery' in df.columns:
    df['Online Delivery (Encoded)'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
    print("Online Delivery Encoded")
else:
    print("'Has Online delivery' column not found")

# -------------------------------
# 5. Show updated dataset
# -------------------------------

print("\nUpdated Dataset Preview:")
print(df.head())

# -------------------------------
# 6. Save new dataset (important 🔥)
# -------------------------------

df.to_csv("processed_dataset.csv", index=False)

print("\nNew dataset saved as 'processed_dataset.csv'")