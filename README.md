# Emotion Detection (Text)

A machine learning project that classifies text into three emotions: **sadness, joy, and anger**.

The model uses **TF-IDF** for text feature extraction and **Logistic Regression** for classification.

## Results

The model achieved **96.42% accuracy on the test set**.

* **Dataset size:** 319,571 text samples
* **Test set:** 63,915 samples
* **Sadness F1-score:** 0.96
* **Joy F1-score:** 0.98
* **Anger F1-score:** 0.93

## Technologies Used

* Python
* Pandas
* NLTK
* Scikit-learn
* TF-IDF
* Logistic Regression

## How It Works

The project follows this pipeline:

**Text → Preprocessing → TF-IDF → Logistic Regression → Emotion Prediction**

The text is cleaned by:

* converting text to lowercase
* removing URLs
* removing numbers and punctuation
* removing English stopwords

The cleaned text is then converted into numerical features using TF-IDF before being used to train the Logistic Regression model.

## Dataset

The dataset contains text samples with emotion labels.

This project uses three classes:

* `0` = sadness
* `1` = joy
* `3` = anger

The original dataset may contain additional emotion classes, but this project filters the data to these three.

The dataset file is not included in this repository.

## Files

* `emotion_detection.py` — main Python script
* `requirements.txt` — required Python packages
* `text.xlsx` — dataset file used locally

## Dataset Format

The script expects an Excel file named `text.xlsx` with these columns:

* `text` — the text sample
* `label` — the emotion label

Example:

```text
text                                      label
I feel very happy today                   1
I am so lonely and tired                  0
I am angry about this                     3
```

## How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Place the dataset in the project folder

Make sure `text.xlsx` is in the same folder as `emotion_detection.py`.

### 3. Run the script

```bash
python emotion_detection.py
```

The script will download the required NLTK stopwords dataset if it is not already installed.

## What the Script Does

The script:

1. Reads the dataset
2. Selects the required columns
3. Filters the dataset to three emotion classes
4. Cleans the text
5. Splits the data into training and testing sets
6. Converts text into numerical features using TF-IDF
7. Trains a Logistic Regression model
8. Evaluates the model
9. Predicts emotions for sample sentences

## Evaluation

The script outputs:

* Dataset shape
* Class distribution
* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Sample predictions

### Example Predictions

| Text                                                  | Prediction |
| ----------------------------------------------------- | ---------- |
| "I feel very happy today and everything is wonderful" | Joy        |
| "I am really upset and frustrated right now"          | Anger      |
| "I feel so lonely and broken inside"                  | Sadness    |

## What I Learned

Through this project, I practiced:

* Text preprocessing
* Feature extraction using TF-IDF
* Training a classification model
* Evaluating machine learning models
* Working with a large dataset
* Using Python libraries such as Pandas, NLTK, and Scikit-learn

## Future Improvements

* Add more emotion classes
* Experiment with other machine learning models
* Improve text preprocessing
* Build a web interface for real-time emotion predictions
