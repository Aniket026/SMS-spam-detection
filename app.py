import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer 

ps = PorterStemmer()

# Function to transform input text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# App title and description
st.title("📧 Email/SMS Spam Classifier")
st.markdown("""
### Identify whether a message is spam or not
This application uses Natural Language Processing (NLP) techniques and a machine learning model to classify messages.
""")

# Input text area
st.markdown("#### Enter the message below:")
input_sms = st.text_area("", height=150)

# Predict button
if st.button('🔍 Predict'):
    if input_sms.strip() != "":
        # Preprocess the input
        transformed_sms = transform_text(input_sms)
        # Vectorize the input
        vector_input = tfidf.transform([transformed_sms])
        # Predict the result
        result = model.predict(vector_input)[0]
        # Display the result
        if result == 1:
            st.markdown("### 📛 **Spam**")
        else:
            st.markdown("### ✅ **Not Spam**")
    else:
        st.error("Please enter a message to classify.")

# Footer
st.markdown("""
---
Developed by [Aniket Borawake](https://www.linkedin.com/in/aniket-borawake-547535236)
""")
