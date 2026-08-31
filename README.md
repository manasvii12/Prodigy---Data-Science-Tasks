# Task-04: Sentiment Analysis on Twitter Data

## 📌 Overview
This task focuses on analyzing and visualizing **sentiment patterns in social media data** to understand public opinion and attitudes.  
The dataset used is the **Twitter Training Dataset**, which contains tweets labeled with sentiment categories.  
The goal is to compute sentiment scores, classify tweets into Positive, Negative, or Neutral, and visualize the results.

---

## 🛠️ Steps Performed
1. **Data Preparation**
   - Loaded `twitter_training.csv` (no headers, added custom column names).
   - Columns: `id`, `category`, `sentiment_label`, `text`.
   - Converted text values to strings and handled missing values.

2. **Sentiment Analysis**
   - Used **TextBlob** to compute sentiment polarity scores.
   - Classified tweets into `Positive`, `Negative`, or `Neutral`.

3. **Visualization**
   - Distribution plot of sentiment categories.
   - WordClouds for positive and negative tweets.

4. **Results Export**
   - Saved processed dataset with sentiment scores and computed labels.
   - Exported plots as PNG files.

---

## 📊 Outputs
Generated files include:
- `task4_sentiment_distribution.png` → bar chart of sentiment distribution.  
- `task4_positive_wordcloud.png` → word cloud of positive tweets.  
- `task4_negative_wordcloud.png` → word cloud of negative tweets.  
- `task4_sentiment_results.csv` → dataset with sentiment scores and computed labels.  

---

## 🔑 Key Insights
- Tweets show a mix of positive, negative, and neutral sentiments.  
- WordClouds highlight the most frequent words used in positive vs negative tweets.  
- Sentiment distribution helps visualize overall public opinion trends.  

---

## 📂 Files
- `twitter_training.csv` → dataset.  
- `task4_sentiment_analysis.py` → Python script for sentiment analysis.  
- Results (`.csv`) and visualizations (`.png`).  

---

## 🚀 Tools Used
- **Python**  
- **pandas** for data handling  
- **TextBlob** for sentiment scoring  
- **matplotlib** & **seaborn** for visualization  
- **wordcloud** for text visualization  

---

## 📝 Author
Manasvi — B.Tech CSE student, Data Science Intern at Prodigy InfoTech
