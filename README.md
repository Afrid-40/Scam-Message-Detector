# 🛡️ Scam Message Detector

**Machine Learning powered scam and phishing message detection**

Detect whether a message is likely to be **SAFE** or **SCAM** using Natural Language Processing and Machine Learning.

**Built with:** Python • Scikit-Learn • TF-IDF • Streamlit

---

## 🚀 Overview

**Scam Message Detector** is an NLP-based Machine Learning classification project that analyzes text messages and predicts whether they contain patterns commonly associated with scams.

The project follows a complete ML workflow:

**Dataset → Text Preprocessing → TF-IDF → Model Training → Evaluation → Prediction → Streamlit Dashboard**

> **Important:** The current dataset is synthetic. The reported 100% test accuracy is a demonstration result and should not be interpreted as real-world scam-detection performance.

---

## ✨ Features

- 📨 Scam/Safe message classification
- 🧠 TF-IDF text feature extraction
- 🤖 Multiple Machine Learning classification algorithms
- 📊 Model performance evaluation
- 🎯 Prediction confidence score
- 🖥️ Interactive Streamlit dashboard
- 🚨 Scam warning and safety guidance
- 💾 Saved trained model and TF-IDF vectorizer
- 🌙 Dark-themed dashboard UI

---

## 🧠 Machine Learning Models

| Model | Accuracy |
|---|---:|
| **Logistic Regression** | **100%** |
| Naive Bayes | **100%** |
| Random Forest | **100%** |

### 🏆 Selected Model

**Logistic Regression** is used as the deployed prediction model.

The models were evaluated using Accuracy, Precision, Recall, and F1-score.

---

## 📊 Dataset

The dataset contains **1,000 messages** with two columns:

| Feature | Description |
|---|---|
| `message` | Text message to classify |
| `label` | `0` = SAFE, `1` = SCAM |

**Distribution:** 500 SAFE messages and 500 SCAM messages.

Dataset location:

```text
data/messages.csv
```

---

## 🔬 Machine Learning Workflow

```text
┌──────────────────────┐
│    Message Dataset   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Text Preprocessing  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    TF-IDF Vectorizer │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────────┐
│      Train ML Models       │
│                            │
│  • Logistic Regression     │
│  • Naive Bayes             │
│  • Random Forest           │
└─────────────┬──────────────┘
              │
              ▼
┌──────────────────────┐
│   Model Evaluation   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Logistic Regression │
│   Selected Model     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Streamlit Dashboard  │
└──────────────────────┘
```

---

## 🖥️ Dashboard

The Streamlit application provides:

- 🚨 Scam/Safe prediction
- 📈 Prediction confidence
- 🤖 Model information
- ⚠️ Security guidance
- 📊 Analysis summary

### Dashboard Screenshot

Add your screenshot as:

```text
screenshots/dashboard.png
```

Then it will appear here:

<p align="center">
  <img src="screenshots/Dashboard.png" width="900" alt="Scam Message Detector Dashboard">
</p>

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| NLP | TF-IDF |
| Machine Learning | Scikit-Learn |
| Models | Logistic Regression, Naive Bayes, Random Forest |
| Model Persistence | Joblib |
| Application | Streamlit |

---

## 📁 Project Structure

```text
SCAM-MESSAGE-DETECTOR/
│
├── app/
│   └── app.py
│
├── data/
│   ├── generate_data.py
│   └── messages.csv
│
├── models/
│   ├── scam_message_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── predict.py
│   └── train.py
│
├── screenshots/
│   └── dashboard.png
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Afrid-40/Scam-Message-Detector.git
cd Scam-Message-Detector
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```powershell
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Train the Model

```bash
python src/train.py
```

The trained model and TF-IDF vectorizer are saved inside:

```text
models/
```

---

## 🎯 Command-Line Prediction

Run:

```bash
python src/predict.py
```

### Scam example

```text
> Congratulations! You have won ₹50,000. Click this link to claim your prize.

🚨 SCAM DETECTED
Confidence: 92.79%
```

### Safe example

```text
> Hey, are we still meeting tomorrow?

✅ SAFE MESSAGE
Confidence: 91.72%
```

---

## ▶️ Run the Streamlit Dashboard

```bash
streamlit run app/app.py
```

Open:

```text
http://localhost:8501
```

---

## 🔮 Future Improvements

- 🌐 Deploy the dashboard online
- 📚 Train on larger real-world SMS and phishing datasets
- 🔗 Detect suspicious URLs
- 🧠 Add explainable AI
- 📊 Add prediction history and analytics
- 🚨 Detect phishing-specific patterns
- 🌍 Support multiple languages
- 📱 Improve mobile responsiveness
- 🔄 Continuously retrain with new scam patterns

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The current dataset is synthetic, and the model's predictions should **not** be treated as definitive proof that a message is safe or malicious.

Always verify suspicious messages through official channels. Never share passwords, OTPs, banking information, or other sensitive information with unknown sources.

---

## 👨‍💻 Author

**Mohammed Shahed Afrid Khan**

Machine Learning • Artificial Intelligence • Python • Data Science

GitHub: [Afrid-40](https://github.com/Afrid-40)

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐.

<p align="center">

**Built with Python • Scikit-Learn • TF-IDF • Streamlit**

</p>
