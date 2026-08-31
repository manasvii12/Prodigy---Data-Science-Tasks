# Task-05: Traffic Accident Data Analysis

## 📌 Overview
This task focuses on analyzing **traffic accident data** to identify patterns related to **road conditions, weather, and time of day**.  
The dataset used is the **US Accidents Dataset (March 2023)** from Kaggle.  
The goal is to uncover accident trends, visualize contributing factors, and highlight accident hotspots.

---

## 🛠️ Steps Performed
1. **Data Preparation**
   - Loaded `US_Accidents_March23.csv`.
   - Handled missing values and converted timestamps to datetime format.
   - Extracted features such as `Hour` and `DayOfWeek`.

2. **Pattern Analysis**
   - Accidents by weather conditions.
   - Accidents by hour of day.
   - Accidents by day of week.

3. **Visualization**
   - Bar charts for weather, time, and weekday patterns.
   - Interactive hotspot map using **Folium**.

4. **Results Export**
   - Saved plots as `.png` files.
   - Exported hotspot map as `.html`.

---

## 📊 Outputs
Generated files include:
- `task5_weather_conditions.png` → Top 10 weather conditions during accidents.  
- `task5_accidents_by_hour.png` → Distribution of accidents by hour of day.  
- `task5_accidents_by_day.png` → Distribution of accidents by weekday.  
- `task5_accident_hotspots.html` → Interactive map showing accident hotspots.  

---

## 🔑 Key Insights
- Certain weather conditions (e.g., rain, fog) are linked to higher accident counts.  
- Accidents peak during **rush hours** (morning and evening).  
- Weekdays show more accidents compared to weekends.  
- Hotspot maps reveal clusters in urban and high‑traffic regions.  

---

## 📂 Files
- `US_Accidents_March23.csv` → dataset.  
- `task5_accident_analysis.py` → Python script for analysis.  
- Results (`.png`) and hotspot map (`.html`).  

---

## 🚀 Tools Used
- **Python**  
- **pandas** for data handling  
- **matplotlib** & **seaborn** for visualization  
- **folium** for interactive maps  

---

## 📝 Author
Manasvi — B.Tech CSE student, Data Science Intern at Prodigy InfoTech
