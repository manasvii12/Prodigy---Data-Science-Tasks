import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("twitter_training.csv", header=None)

# Assign column names
data.columns = ["id", "category", "sentiment_label", "text"]

print("Dataset shape:", data.shape)
print(data.head())

# -----------------------------
# Sentiment Analysis
# -----------------------------
# Function to calculate sentiment polarity


def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity


# Apply sentiment scoring
data["sentiment_score"] = data["text"].apply(get_sentiment)

# Categorize sentiment
data["sentiment_label_computed"] = data["sentiment_score"].apply(
    lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
)

# -----------------------------
# Visualization 1: Sentiment Distribution
# -----------------------------------------------
sns.countplot(x="sentiment_label", data=data, hue="sentiment_label",
              palette="coolwarm", legend=False)
plt.title("Sentiment Distribution")
plt.savefig("task4_sentiment_distribution.png", dpi=300)
plt.close()

# Visualization 2: WordClouds
# -----------------------------------------------
# Positive sentiment wordcloud
positive_text = " ".join(
    data[data["sentiment_label"] == "Positive"]["text"]
)
if positive_text.strip():
    wordcloud_pos = WordCloud(
        width=800, height=400, background_color="white"
    ).generate(positive_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_pos, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("task4_positive_wordcloud.png", dpi=300)
    plt.close()
else:
    print("No positive sentiment text found")

# Negative sentiment wordcloud
negative_text = " ".join(
    data[data["sentiment_label"] == "Negative"]["text"]
)
if negative_text.strip():
    wordcloud_neg = WordCloud(
        width=800,
        height=400,
        background_color="black",
        colormap="Reds"
    ).generate(negative_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_neg, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("task4_negative_wordcloud.png", dpi=300)
    plt.close()
else:
    print("No negative sentiment text found")

# -----------------------------
# Save Results
# -----------------------------
data.to_csv("task4_sentiment_results.csv", index=False)

print("Analysis complete. Outputs saved:")
print("- task4_sentiment_distribution.png")
print("- task4_positive_wordcloud.png")
print("- task4_negative_wordcloud.png")
print("- task4_sentiment_results.csv")
