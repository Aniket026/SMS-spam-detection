# SMS and Email spam detection

<h4>Project Overview : </h4>
The spam detection project leverages machine learning techniques to identify spam in SMS and email messages. Using the Scikit-Learn library, three Naive Bayes classifiers—GaussianNB, MultinomialNB, and BernoulliNB—are implemented to detect and classify messages as spam or not spam.

<h4>Objectives :</h4>
To build a robust system that can automatically classify SMS and email messages as spam or non-spam.
To compare the performance of different Naive Bayes classifiers for this task.
<h4></h4>Dataset :</h4><br>
The dataset used for this project includes labeled SMS and email messages. Each message is categorized as either "spam" or "ham" (non-spam). The dataset is split into training and testing sets to evaluate the performance of the classifiers.

<h4>Methodology :</h4>
<h3></h3>Data Preprocessing: </h3><br>

<h5>1] Text Cleaning:</h5> Removing punctuation, stop words, and performing stemming or lemmatization.
<h5>2] Feature Extraction:</h5> Converting text data into numerical features using techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) or Count Vectorization.
<h5>Model Implementation: </h5>

<h5>Gaussian Naive Bayes (GaussianNB):</h5> Suitable for continuous data, assuming the features follow a Gaussian (normal) distribution.
<h5>Multinomial Naive Bayes (MultinomialNB):</h5> Best for discrete data, particularly useful for text classification problems where word frequencies or occurrences are considered.
<h5>Bernoulli Naive Bayes (BernoulliNB): </h5>Designed for binary/boolean features, indicating the presence or absence of a feature (word).
<h3></h3>Model Training:<h/3><br>

Each classifier is trained using the training dataset.
Hyperparameters are tuned to optimize performance.
<h3>Model Evaluation:</h3><br>

Models are evaluated using metrics such as accuracy, precision, recall, and F1-score.
Confusion matrix is used to visualize the performance of each classifier.
