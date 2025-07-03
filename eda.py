# EDA for Google Stock Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("GOOG.csv")

# Step 1: View first few rows
print("🔹 First 5 Rows:")
print(df.head())

# Step 2: Dataset info
print("\n🔹 Info:")
print(df.info())

# Step 3: Summary statistics
print("\n🔹 Summary:")
print(df.describe())

# Step 4: Missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())

# Step 5: Convert 'Date' column to datetime if it exists
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

# Step 6: Visualize Close Price over Time
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price')
plt.title('GOOG Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 7: Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Step 8: Moving Average (Optional)
df['MA50'] = df['Close'].rolling(window=50).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['MA50'], label='50-day MA', linestyle='--')
plt.title('GOOG Price with 50-Day Moving Average')
plt.legend()
plt.show()

# step 9: Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set as index for time-series plotting
df.set_index('Date', inplace=True)

# Confirm
print(df.index)

import matplotlib.pyplot as plt

# Plot Close Price
plt.figure(figsize=(12,6))
plt.plot(df['Close'], color='blue', label='Close Price')
plt.title('GOOG Stock Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

import seaborn as sns

# Plot heatmap of numeric correlation
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
