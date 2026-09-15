import re
import string
import os
import joblib

import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


nltk.download('stopwords')

# Read dataset
df = pd.read_excel('text.xlsx')

# Keep only needed columns
df = df[['text', 'label']]

# Keep only 3 classes: sadness (0), joy (1), anger (3)
df = df[df['label'].isin([0, 1, 3])]

# Convert numbers to emotion names
label_names = {
    0: 'sadness',
    1: 'joy',
    3: 'anger'
}

# Clean text
stop_words = set(stopwords.words('english'))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


df['clean_text'] = df['text'].apply(clean_text)

print(df.head())
print('\nDataset shape:', df.shape)
print('\nClass distribution:')
print(df['label'].value_counts())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'],
    df['label'],
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

# Convert text into numbers
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Save model and vectorizer
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model saved successfully.")

# Predict
y_pred = model.predict(X_test_vec)

# Results
print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nClassification Report:\n')
print(classification_report(
    y_test,
    y_pred,
    target_names=['sadness', 'joy', 'anger']
))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))

# Test custom messages
test_messages = [
    'I feel very happy today and everything is wonderful',
    'I am really upset and frustrated right now',
    'I feel so lonely and broken inside',
    'This is the best day of my life',
    'I am angry about what happened'
]

print('\nSample Predictions:')
for msg in test_messages:
    msg_clean = clean_text(msg)
    msg_vec = vectorizer.transform([msg_clean])
    prediction = model.predict(msg_vec)[0]

    print('\nText:', msg)
    print('Predicted Emotion:', label_names[prediction])
