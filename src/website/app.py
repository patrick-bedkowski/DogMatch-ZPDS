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

# Load recommender
pickle_in = open("./src/recommender/model.pkl", "rb")
recommender = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_breed(user_input: np.array):
    with open("./src/recommender/code_to_breed.json", "r") as json_file:
        code_to_breed = json.load(json_file)
    prediction = recommender.predict([user_input])[0]
    breed = code_to_breed[str(prediction)]
    print(breed)
    return breed


def main():
    st.title("DogMatch")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit DogMatch ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    affectionate_with_family = st.number_input("Affectionate With Family", 3)
    good_with_young_children = st.number_input("Good With Young Children", 3)
    good_with_other_dogs = st.number_input("Good With Other Dogs", 3)
    shedding_level = st.number_input("Shedding Level", 2)
    coat_grooming_frequency = st.number_input("Coat Grooming Frequency", 3)
    drooling_level = st.number_input("Drooling Level", 2)
    coat_type = st.number_input("Coat Type", 3)
    coat_length = st.number_input("Coat Length", 2)
    openness_to_strangers = st.number_input("Openness To Strangers", 3)
    playfulness_level = st.number_input("Playfulness Level", 2)
    watchdog_protective_nature = st.number_input("Watchdog/Protective Nature", 3)
    adaptability_level = st.number_input("Adaptability Level", 2)
    trainability_level = st.number_input("Trainability Level", 2)
    energy_level = st.number_input("Energy Level", 3)
    barking_level = st.number_input("Barking Level", 2)
    mental_stimulation_needs = st.number_input("Mental Stimulation Needs", 2)

    result = ""

    user_input = np.array([affectionate_with_family, good_with_young_children, good_with_other_dogs, shedding_level,
                            coat_grooming_frequency, drooling_level, coat_type, coat_length, openness_to_strangers,
                            playfulness_level, watchdog_protective_nature, adaptability_level, trainability_level,
                            energy_level, barking_level, mental_stimulation_needs])

    if st.button("Predict"):
        result = predict_breed(user_input)
    st.success('Most suitable breed is {}'.format(result))
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
