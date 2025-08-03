#Import libraries
import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

#create function to perform text preprocessing steps
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

#Load pickle
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model_tfidf.pkl','rb'))

#Create display button
st.title("Spam Detector")
input_message = st.text_area("Input your message")

if st.button('Predict'):
    transformed_message = transform_text(input_message) #1. text preprocess
    vector_input = tfidf.transform([transformed_message]) #2. vectorize
    result = model.predict(vector_input)[0] #3. predict
    if result == 1:
        st.markdown("<h2 style='color: red;'>Spam</h2>", unsafe_allow_html=True)
        
    else:
        st.markdown("<h2 style='color: green;'>Not Spam</h2>", unsafe_allow_html=True)
        
