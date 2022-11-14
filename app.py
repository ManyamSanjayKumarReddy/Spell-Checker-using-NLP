import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
from checker import SpellChecker

pickle_in = open("checker.pkl", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def checker_app(word ):
    classifier = SpellChecker("./big.txt")
    prediction = classifier.check(
        word)
    print(prediction)
    return prediction


def main():

    st.set_page_config(
        page_title="Spell Checker using Regular Expressions",
        layout="wide",
    )

    image = Image.open("spellchecker.jpg")
    st.image(image)

    st.title("Spell Checker using NLP  ")
    html_temp = """
            <div style="background-color:tomato;padding:0px">
            <h3 style="color:white;text-align:center;"> Enter the Word to get the Spell Checked Word</h3>
            </div>
            <br>
    """

    st.markdown(
        'Our app gives the best spelling for the word that is given by the **USER...**')

    st.markdown(html_temp, unsafe_allow_html=True)
    word = st.text_input(
        "Word", placeholder="Enter the Word to be checked ")
   

    result = ""
    if st.button("Check the Spelling"):
        result = checker_app(
            word)
    st.success('The word after the spell checking is {}'.format(result))



if __name__ == '__main__':
    main()
