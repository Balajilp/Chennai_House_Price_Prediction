import pandas as pd
df = pd.read_csv('app_create')
X = df.drop('price', axis=1)
y = df['price']

import numpy as np
import pickle
import streamlit as st


pickle_in = open("banglore_home_prices_model.pickle","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_price(location, sqft, bath, bhk):
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index]=1
    return classifier.predict([x])[0]


def main():
    st.title("BANGALORE HOME PRICE PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit HOME PRICE ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    location = st.text_input("location","Type Here")
    sqft = st.text_input("sqft","Type Here")
    bath = st.text_input("bath","Type Here")
    bhk = st.text_input("bhk","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_price(location, sqft, bath, bhk)
    st.success('The Price is {} Laks'.format(result))


if __name__=='__main__':
    main()