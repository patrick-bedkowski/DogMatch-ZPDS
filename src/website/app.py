# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:47:00 2024

@author: dogmatch.team.co
"""

import numpy as np
import pickle
import pandas as pd
# from flasgger import Swagger
import streamlit as st
import json

from PIL import Image

# Load recommender
pickle_in = open("../recommender/model.pkl", "rb")
recommender = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_breed(user_input: np.array):
    with open("../recommender/code_to_breed.json", "r") as json_file:
        code_to_breed = json.load(json_file)
    prediction = recommender.predict(user_input)[0]
    breed = code_to_breed[prediction]
    print(breed)
    return breed


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    import streamlit as st

    affectionate_with_family = st.text_input("Affectionate With Family", "Type Here")
    good_with_young_children = st.text_input("Good With Young Children", "Type Here")
    good_with_other_dogs = st.text_input("Good With Other Dogs", "Type Here")
    shedding_level = st.text_input("Shedding Level", "Type Here")
    coat_grooming_frequency = st.text_input("Coat Grooming Frequency", "Type Here")
    drooling_level = st.text_input("Drooling Level", "Type Here")
    coat_type = st.text_input("Coat Type", "Type Here")
    coat_length = st.text_input("Coat Length", "Type Here")
    openness_to_strangers = st.text_input("Openness To Strangers", "Type Here")
    playfulness_level = st.text_input("Playfulness Level", "Type Here")
    watchdog_protective_nature = st.text_input("Watchdog/Protective Nature", "Type Here")
    adaptability_level = st.text_input("Adaptability Level", "Type Here")
    trainability_level = st.text_input("Trainability Level", "Type Here")
    energy_level = st.text_input("Energy Level", "Type Here")
    barking_level = st.text_input("Barking Level", "Type Here")
    mental_stimulation_needs = st.text_input("Mental Stimulation Needs", "Type Here")

    result = ""

    user_input = np.array([affectionate_with_family, good_with_young_children, good_with_other_dogs, shedding_level,
                            coat_grooming_frequency, drooling_level, coat_type, coat_length, openness_to_strangers,
                            playfulness_level, watchdog_protective_nature, adaptability_level, trainability_level,
                            energy_level, barking_level, mental_stimulation_needs])

    if st.button("Predict"):
        result = predict_breed(user_input)
    st.success('Most suitable breed is is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()


