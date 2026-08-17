import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
df = pd.read_csv("data/messages.csv")

X = df["message"]
y = df["label"]


# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# TF-IDF
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=5000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}


results = {}
best_model = None
best_accuracy = 0


# Train and evaluate
for name, model in models.items():

    model.fit(X_train_tfidf, y_train)

    predictions = model.predict(X_test_tfidf)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    results[name] = accuracy

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print(f"Accuracy: {accuracy:.4f}")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=["SAFE", "SCAM"]
        )
    )

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model


# Save best model
joblib.dump(
    best_model,
    "models/scam_message_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)


print("\n" + "=" * 50)
print("BEST MODEL")
print("=" * 50)

print(f"Model: {type(best_model).__name__}")
print(f"Accuracy: {best_accuracy:.4f}")

print("\nModels saved successfully!")