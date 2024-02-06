# Hate Speech Detection

This repository contains code for building a Hate Speech Detection model using a labeled dataset. The goal is to classify text data into categories such as "Hate Speech," "Offensive Language," or "Neither" using machine learning algorithms.

## Dataset
The dataset used in this project is loaded from the file labeled_data.csv. The data consists of text samples labeled with classes: 0 for "Hate Speech," 1 for "Offensive Language," and 2 for "Neither."

## Libraries Used
The project utilizes the following Python libraries:

- `pandas` and `numpy` for data manipulation and analysis.
- `nltk` for natural language processing tasks, including text cleaning and stemming.
- `scikit-learn` for machine learning algorithms and evaluation metrics.
- `seaborn` and `matplotlib` for data visualization.

## Project Steps
### 1. Data Exploration:
- Descriptive statistics of the dataset.
- Mapping label values to numerical values (0 for "Hate Speech," 1 for "Offensive Language," and 2 for "Neither").
- Balancing the dataset by creating a new "labels" column.

### 2. Text Preprocessing:
- Removing special characters, numbers, and website links from the text.
- Converting text to lowercase.
- Removing stopwords (common words with little significance).
- Stemming words to their base or root form.

### 3. Feature Extraction:
- Using the Bag-of-Words approach with CountVectorizer to convert text data into numerical feature vectors.

### 4. Model Building and Evaluation:
- Splitting the dataset into training and testing sets.
- Training a Decision Tree model for Hate Speech Detection.
- Evaluating the model's performance using confusion matrix, heatmap, and accuracy score.
- Providing a sample example to demonstrate how to use the model for predictions.

## Technical Information
- The code is implemented in Python 3.7+ using Jupyter Notebook.
- Machine learning models are built using the scikit-learn library.
- Natural language processing tasks leverage the Natural Language Toolkit (nltk).
- Text data is converted into numerical feature vectors using CountVectorizer.

## Usage
Follow the steps outlined in the Jupyter Notebook to preprocess the data, extract features, and train the Hate Speech Detection model. Modify the code as needed to suit your requirements.

## Conclusion
By building and evaluating the Hate Speech Detection model, you can effectively categorize text into different classes, aiding in the identification of potentially harmful content. The results and insights gained from this project can be applied to various applications, such as content moderation and online safety.

## Credits
- The labeled dataset used in this project was obtained from [kaggle](https://www.kaggle.com/datasets).
- The code in this repository was written by Sai Saketh Motamarry.
