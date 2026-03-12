# AI-Based Phishing Email Detection System 🔐

## 📌 Project Overview

This project is an **AI-powered phishing detection system** that analyzes email content to identify potential phishing attacks.

It combines **Machine Learning and rule-based cybersecurity techniques** to detect suspicious emails, URLs, domains, and email addresses.

The system also calculates a **risk score** and assigns a **threat level**.

---

## 🚀 Features

* AI-based phishing email detection
* Suspicious URL detection
* Suspicious domain detection
* Suspicious email address detection
* Risk score calculation
* Threat level classification
* Security scan logging

---

## 🛠 Technologies Used

* Python
* Machine Learning
* Natural Language Processing (NLP)

---

## 📚 Python Libraries

* pandas
* scikit-learn
* re (Regular Expressions)

Install required libraries:

```bash
pip install pandas scikit-learn
```

---

## 🧠 Machine Learning Model

Algorithm Used:

**Logistic Regression**

Feature Extraction:

**TF-IDF Vectorizer**

---

## ⚙ How the System Works

1. The user enters an email message.
2. The system checks for:

   * Suspicious URLs
   * Suspicious domains
   * Suspicious email addresses
3. The AI model analyzes the email text.
4. The system calculates a **risk score**.
5. A **threat level** is assigned:

   * LOW
   * MEDIUM
   * HIGH

---

## 📂 Project Structure

AI_Phishing_Detection
│
├── dataset
│   └── phishing_email.csv
│
├── phishing_detector.py
│
├── scan_log.txt
│
└── README.md

---

## ▶ Example Usage

Run the program:

```bash
python3 phishing_detector.py
```

Example Input:

```
verify your bank account immediately
```

Example Output:

```
⚠ Phishing Email Detected
Risk Score: 58%
Threat Level: MEDIUM
```

---

## 👩‍💻 Author

**Safwana Nasrin**

---

## 🔮 Future Improvements

* Larger phishing dataset
* Graphical user interface (GUI)
* Real email file scanning
* Integration with email clients
