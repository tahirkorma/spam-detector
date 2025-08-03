# 📧 Spam Detector Classifier

This project is an end-to-end **Spam Message Classifier** that uses NLP techniques like text preprocessing and TF-IDF vectorization, along with classification models like Multinomial Naive Bayes. It's built in Python and deployed using Streamlit for an interactive web app.

---

## 🚀 Features

- Detects whether a given message is **Spam** or **Not Spam (Ham)**
- Text preprocessing (tokenization, stopword removal, stemming)
- TF-IDF based feature extraction
- **13+ ML algorithms** tested (Logistic Regression, SVM, Random Forest, etc.)
- Advanced ensemble techniques: **Voting Classifier** and **Stacking Classifier**
- Performance comparison using **accuracy** and **precision**
- **Multinomial Naive Bayes (MNB)** selected as final model due to **highest precision**
- Deployment-ready with `pickle` serialization
- Interactive web interface via Streamlit

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn (for EDA)
- Pickle

---

## 📁 Project Structure
  ```bash
  📦 spam-detector/
  ├── app.py # Streamlit app
  ├── model.pkl # Final trained MultinomialNB model
  ├── vectorizer.pkl # Trained TF-IDF vectorizer
  ├── spam.csv # Dataset (SMS Spam Collection)
  ├── requirements.txt # List of dependencies
  └── README.md # Project description
  ```
---

## ✅ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/tahirkorma/spam-detector.git
   cd spam-detector

2. **Create and activate a virtual environment**
   ```bash
   # Create venv
   python -m venv venv

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the app**
    ```bash
    streamlit run app.py

## 🚀 Live Demo

🎯 Check out the live working app here:

👉 [Click to Open Live Spam Detector](https://spamdetectorbytahirkorma.streamlit.app)

💡 You can input your own text and instantly see if it's classified as **Spam** or **Not Spam**.
