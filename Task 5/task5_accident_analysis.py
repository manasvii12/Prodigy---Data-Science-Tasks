import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# -----------------------------
# Load Dataset
# -----------------------------
# Use the correct filename you have in your folder
data = pd.read_csv("US_Accidents_March23.csv")

print("Dataset shape:", data.shape)
print(data.head())

# -----------------------------
# Fix Date Parsing
# -----------------------------
# Let pandas infer mixed formats safely
data["Start_Time"] = pd.to_datetime(data["Start_Time"], errors="coerce")

# -----------------------------
# Analyze Patterns
# -----------------------------

# 1. Accidents by weather condition
plt.figure(figsize=(10, 5))
sns.countplot(y="Weather_Condition",
              data=data,
              order=data["Weather_Condition"].value_counts().head(10).index)
plt.title("Top 10 Weather Conditions during Accidents")
plt.savefig("task5_weather_conditions.png", dpi=300)
plt.close()

# 2. Accidents by hour of day
data["Hour"] = data["Start_Time"].dt.hour
plt.figure(figsize=(10, 5))
sns.countplot(x="Hour", data=data, palette="coolwarm")
plt.title("Accidents by Hour of Day")
plt.savefig("task5_accidents_by_hour.png", dpi=300)
plt.close()

# 3. Accidents by day of week
data["DayOfWeek"] = data["Start_Time"].dt.day_name()
plt.figure(figsize=(10, 5))
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]
sns.countplot(x="DayOfWeek", data=data, order=day_order)
plt.title("Accidents by Day of Week")
plt.savefig("task5_accidents_by_day.png", dpi=300)
plt.close()

# -----------------------------
# Accident Hotspot Map
# -----------------------------
# Sample 1000 points for speed
subset_cols = ["Start_Lat", "Start_Lng"]
sample_data = data.dropna(subset=subset_cols).sample(
    1000, random_state=42)

# USA center coordinates
map_accidents = folium.Map(
    location=[37.0902, -95.7129], zoom_start=4)

for _, row in sample_data.iterrows():
    folium.CircleMarker(
        location=[row["Start_Lat"], row["Start_Lng"]],
        radius=2,
        color="red",
        fill=True
    ).add_to(map_accidents)

map_accidents.save("task5_accident_hotspots.html")

print("Analysis complete. Outputs saved:")
print("- task5_weather_conditions.png")
print("- task5_accidents_by_hour.png")
print("- task5_accidents_by_day.png")
print("- task5_accident_hotspots.html")
