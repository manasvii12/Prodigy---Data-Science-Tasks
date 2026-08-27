# task01_population_viz.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams.update({"figure.dpi": 150})

# Filenames (adjust if your filenames differ)
POP_FILE = "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
META_COUNTRY_FILE = "Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
META_INDICATOR_FILE = (
    "Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
)

# 1. Load population data (skip header metadata rows)
pop = pd.read_csv(POP_FILE, skiprows=4)

# 2. Load metadata files
meta_country = pd.read_csv(META_COUNTRY_FILE)
meta_indicator = pd.read_csv(META_INDICATOR_FILE)

# 3. Basic cleaning and merge
# Ensure consistent column names
pop.rename(
    columns={"Country Name": "Country Name", "Country Code": "Country Code"},
    inplace=True,
)
merged = pd.merge(pop, meta_country, on="Country Code", how="left")

# Convert year columns to numeric where needed
years = [c for c in merged.columns if c.isdigit()]
for y in years:
    merged[y] = pd.to_numeric(merged[y], errors="coerce")

# Choose year for analysis
YEAR = "2024"
if YEAR not in merged.columns:
    # fallback to latest numeric year column
    YEAR = sorted(years)[-1]

# Create output folder
out_dir = "task01_outputs"
os.makedirs(out_dir, exist_ok=True)

# 4. Histogram of country populations (millions)
plt.figure(figsize=(8, 5))
plt.hist(merged[YEAR].dropna()/1e6, bins=30, color="orange", edgecolor="black")
plt.title(f"Distribution of Country Populations ({YEAR})")
plt.xlabel("Population (millions)")
plt.ylabel("Number of countries")
plt.tight_layout()
hist_path = os.path.join(out_dir, f"hist_population_{YEAR}.png")
plt.savefig(hist_path)
plt.close()

# 5. Population by IncomeGroup (sum)
income_pop = merged.groupby("IncomeGroup")[YEAR].sum().dropna().sort_values()
plt.figure(figsize=(8, 5))
income_pop.plot(kind="barh", color="teal", edgecolor="black")
plt.title(f"Total Population by Income Group ({YEAR})")
plt.xlabel("Population")
plt.tight_layout()
income_path = os.path.join(out_dir, f"population_by_incomegroup_{YEAR}.png")
plt.savefig(income_path)
plt.close()

# 6. Top 10 countries by population
top10 = (
    merged[["Country Name", YEAR]]
    .dropna()
    .sort_values(by=YEAR, ascending=False)
    .head(10)
)
plt.figure(figsize=(10, 6))
sns.barplot(x=top10[YEAR]/1e6, y=top10["Country Name"], palette="viridis")
plt.xlabel(f"Population ({YEAR}) in millions")
plt.title(f"Top 10 Countries by Population ({YEAR})")
plt.tight_layout()
top10_path = os.path.join(out_dir, f"top10_countries_{YEAR}.png")
plt.savefig(top10_path)
plt.close()

# 7. Save a small CSV summary
summary = {
    "year": YEAR,
    "total_world_population": merged[YEAR].sum(skipna=True),
    "num_countries": merged["Country Code"].nunique(),
    "top_country": top10.iloc[0]["Country Name"],
    "top_country_population": top10.iloc[0][YEAR]
}
pd.DataFrame([summary]).to_csv(
    os.path.join(out_dir, "summary.csv"), index=False
)

print("Done. Outputs saved to folder:", out_dir)
print("Files:", os.listdir(out_dir))
