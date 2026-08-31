try:
    import pandas as pd  # type: ignore
    from sklearn.model_selection import train_test_split  # type: ignore
    from sklearn.tree import DecisionTreeClassifier, plot_tree  # type: ignore
    from sklearn.metrics import (  # type: ignore
        accuracy_score,
        classification_report,
        confusion_matrix,
    )
    import matplotlib.pyplot as plt  # type: ignore
except ImportError as e:
    print(f"Error: Missing required module. Please install dependencies: {e}")
    print("Run: pip install pandas scikit-learn matplotlib")
    exit(1)


# -----------------------------
# Function to process dataset
# -----------------------------
def run_decision_tree(file_name, output_prefix):
    print(f"\n--- Running Decision Tree on {file_name} ---\n")

    # Load dataset (semicolon separator)
    data = pd.read_csv(file_name, sep=";")

    # Drop 'duration' (leaks target info)
    if "duration" in data.columns:
        data = data.drop("duration", axis=1)

    # Encode categorical variables
    data_encoded = pd.get_dummies(data, drop_first=True)

    # Features and Target
    X = data_encoded.drop("y_yes", axis=1)
    y = data_encoded["y_yes"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build Decision Tree
    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Evaluation
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy:", acc)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Save results to text file
    with open(f"{output_prefix}_results.txt", "w") as f:
        f.write("Accuracy: " + str(acc) + "\n")
        f.write("\nClassification Report:\n" +
                str(classification_report(y_test, y_pred)))
        f.write("\nConfusion Matrix:\n" +
                str(confusion_matrix(y_test, y_pred)))

    # Visualize Decision Tree
    plt.figure(figsize=(20, 10))
    plot_tree(
        clf,
        filled=True,
        feature_names=X.columns,
        class_names=["No", "Yes"]
    )
    plt.savefig(f"{output_prefix}_decision_tree.png")
    plt.close()

    results_file = f"{output_prefix}_results.txt"
    tree_file = f"{output_prefix}_decision_tree.png"
    print(f"Outputs saved: {results_file}, {tree_file}")


# -----------------------------
# Run on both datasets
# -----------------------------
run_decision_tree("bank-additional.csv", "task3_small")
run_decision_tree("bank-additional-full.csv", "task3_full")
