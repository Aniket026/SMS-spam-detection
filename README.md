Spam Detection Using Naive Bayes Machine Learning Algorithms
Project Overview
The spam detection project leverages machine learning techniques to identify spam in SMS and email messages. Using the Scikit-Learn library, three Naive Bayes classifiers—GaussianNB, MultinomialNB, and BernoulliNB—are implemented to detect and classify messages as spam or not spam.

Objectives
To build a robust system that can automatically classify SMS and email messages as spam or non-spam.
To compare the performance of different Naive Bayes classifiers for this task.
Dataset
The dataset used for this project includes labeled SMS and email messages. Each message is categorized as either "spam" or "ham" (non-spam). The dataset is split into training and testing sets to evaluate the performance of the classifiers.

Methodology
Data Preprocessing:

Text Cleaning: Removing punctuation, stop words, and performing stemming or lemmatization.
Feature Extraction: Converting text data into numerical features using techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) or Count Vectorization.
Model Implementation:

Gaussian Naive Bayes (GaussianNB): Suitable for continuous data, assuming the features follow a Gaussian (normal) distribution.
Multinomial Naive Bayes (MultinomialNB): Best for discrete data, particularly useful for text classification problems where word frequencies or occurrences are considered.
Bernoulli Naive Bayes (BernoulliNB): Designed for binary/boolean features, indicating the presence or absence of a feature (word).
Model Training:

Each classifier is trained using the training dataset.
Hyperparameters are tuned to optimize performance.
Model Evaluation:

Models are evaluated using metrics such as accuracy, precision, recall, and F1-score.
Confusion matrix is used to visualize the performance of each classifier.
