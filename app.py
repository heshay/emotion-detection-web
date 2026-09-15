from flask import Flask, render_template, request, jsonify
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

app = Flask(__name__)

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

label_names = {
    0: "sadness",
    1: "joy",
    3: "anger"
}


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    cleaned_text = clean_text(text)
    text_vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(text_vector)[0]

    probabilities = model.predict_proba(text_vector)[0]

    emotion_probabilities = {
        label_names[int(class_id)]: float(probability)
        for class_id, probability in zip(model.classes_, probabilities)
    }

    confidence = float(max(probabilities))

    return jsonify({
        "emotion": label_names[int(prediction)],
        "confidence": confidence,
        "probabilities": emotion_probabilities
    })


if __name__ == "__main__":
    app.run(debug=True)
    