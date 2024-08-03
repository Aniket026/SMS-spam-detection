# SMS and Email spam detection
 <h1>SMS and Email Spam Detection</h1>

    <h4>Project Overview:</h4>
    <p>The spam detection project leverages machine learning techniques to identify spam in SMS and email messages. Using the Scikit-Learn library, three Naive Bayes classifiers—GaussianNB, MultinomialNB, and BernoulliNB—are implemented to detect and classify messages as spam or not spam.</p>

    <h4>Objectives:</h4>
    <p>To build a robust system that can automatically classify SMS and email messages as spam or non-spam. To compare the performance of different Naive Bayes classifiers for this task.</p>

    <h4>Dataset:</h4>
    <p>The dataset used for this project includes labeled SMS and email messages. Each message is categorized as either "spam" or "ham" (non-spam). The dataset is split into training and testing sets to evaluate the performance of the classifiers.</p>

    <h4>Methodology:</h4>

    <h3>Data Preprocessing:</h3>

    <h2>1] Text Cleaning:</h2>
    <p>Removing punctuation, stop words, and performing stemming or lemmatization.</p>

    <h2>2] Feature Extraction:</h2>
    <p>Converting text data into numerical features using techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) or Count Vectorization.</p>

    <h3>Model Implementation:</h3>

    <h2>Gaussian Naive Bayes (GaussianNB):</h2>
    <p>Suitable for continuous data, assuming the features follow a Gaussian (normal) distribution.</p>

    <h2>Multinomial Naive Bayes (MultinomialNB):</h2>
    <p>Best for discrete data, particularly useful for text classification problems where word frequencies or occurrences are considered.</p>

    <h2>Bernoulli Naive Bayes (BernoulliNB):</h2>
    <p>Designed for binary/boolean features, indicating the presence or absence of a feature (word).</p>

    <h3>Model Training:</h3>
    <p>Each classifier is trained using the training dataset. Hyperparameters are tuned to optimize performance.</p>

    <h3>Model Evaluation:</h3>
    <p>Models are evaluated using metrics such as accuracy, precision, recall, and F1-score. Confusion matrix is used to visualize the performance of each classifier.</p>
