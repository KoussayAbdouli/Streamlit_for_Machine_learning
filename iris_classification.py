import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.write('''
# Simple Iris Flower Prediction App
This App predicts the Iris Flower Type !
''')

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length' , 4.3 , 7.9 , 5.4)
    sepal_width = st.sidebar.slider('Sepal Width' , 4.3 , 7.9 , 5.4)
    petal_length = st.sidebar.slider('Petal Length' , 4.3 , 7.9 , 5.4)
    petal_width = st.sidebar.slider('Petal Width' , 4.3 , 7.9 , 5.4)
    data = {
        'Sepal Length' :sepal_length,
        'Sepal Width' :sepal_width,
        'Petal Length' :petal_length ,
        'Petal Width' :petal_width
    }
    input_features = pd.DataFrame(data , index = ['INPUT'])
    return input_features

data = user_input_features()
st.subheader('User Input Parameters')
st.dataframe(data)

###Machine Learning

iris = load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)
print(clf.score(X,Y))

prediction = clf.predict(data)
prediction_proba = clf.predict_proba(data)

st.subheader('Class Label and their Corresponding index Number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
