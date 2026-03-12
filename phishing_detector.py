import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ---------------- LOAD DATASET ----------------

data = pd.read_csv("dataset/phishing_email.csv")

print("Dataset Loaded:")
print(data.head())


# convert labels to numbers
data['label'] = data['label'].map({'safe':0,'phishing':1})


# ---------------- PREPARE DATA ----------------

X = data['text']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)


# ---------------- FEATURE EXTRACTION ----------------

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# ---------------- TRAIN MODEL ----------------

model = LogisticRegression()

model.fit(X_train, y_train)


# ---------------- TEST MODEL ----------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# =====================================================
#                SECURITY FUNCTIONS
# =====================================================

def check_email_domain(email):

    suspicious_domains = [
        "amaz0n",
        "paypa1",
        "secure-login",
        "verify-account",
        "bank-security"
    ]

    for domain in suspicious_domains:
        if domain in email.lower():
            print("⚠ Suspicious email domain detected:", domain)
            return True

    return False


def detect_url(text):

    urls = re.findall(r'(https?://\S+)', text)

    if urls:
        print("⚠ URL detected:", urls)
        return True

    return False


def detect_email_address(text):

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    if emails:

        print("📧 Email address detected:", emails)

        suspicious_patterns = [
            "amaz0n",
            "paypa1",
            "verify",
            "secure-login"
        ]

        for e in emails:
            for pattern in suspicious_patterns:
                if pattern in e.lower():
                    print("⚠ Suspicious email address detected:", e)
                    return True

    return False


# =====================================================
#                 USER INPUT
# =====================================================

email = input("Enter email text to check: ")

domain_flag = check_email_domain(email)
url_flag = detect_url(email)
email_flag = detect_email_address(email)


# ---------------- AI PREDICTION ----------------

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)


# hybrid detection logic

if domain_flag or url_flag or email_flag:
    prediction[0] = 1


# ---------------- RISK SCORE ----------------

probability = model.predict_proba(email_vector)

risk_score = probability[0][1] * 100


# ---------------- THREAT LEVEL ----------------

if risk_score < 30:
    threat = "LOW"

elif risk_score < 70:
    threat = "MEDIUM"

else:
    threat = "HIGH"


# ---------------- FINAL RESULT ----------------

if prediction[0] == 1:
    print("⚠ Phishing Email Detected")

else:
    print("✅ Legitimate Email")


print("Risk Score:", round(risk_score,2), "%")

print("Threat Level:", threat)


# ---------------- SAVE SCAN LOG ----------------

with open("scan_log.txt","a") as log:

    log.write(email + " -> " + str(prediction[0]) + " -> " + threat + "\n")
