import joblib


# Load trained model and TF-IDF vectorizer
model = joblib.load("models/scam_message_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_message(message):

    # Convert message into TF-IDF features
    message_tfidf = vectorizer.transform([message])

    # Prediction
    prediction = model.predict(message_tfidf)[0]

    # Probability
    probabilities = model.predict_proba(message_tfidf)[0]

    confidence = max(probabilities) * 100

    if prediction == 1:
        label = "SCAM"
    else:
        label = "SAFE"

    return label, confidence


if __name__ == "__main__":

    print("=" * 50)
    print("       SCAM MESSAGE DETECTOR")
    print("=" * 50)

    message = input("\nEnter a message to analyze:\n> ")

    label, confidence = predict_message(message)

    print("\n" + "=" * 50)

    if label == "SCAM":
        print("🚨 SCAM DETECTED")
    else:
        print("✅ SAFE MESSAGE")

    print(f"Confidence: {confidence:.2f}%")

    print("=" * 50)