# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import numpy as np
import pickle
import streamlit as st
import json

import functions as f


# Load the recommender model
def load_model():
    with open("./src/recommender/model.pkl", "rb") as file:
        return pickle.load(file)


# Load the breed code to name mapping
def load_code_to_breed():
    with open("./src/recommender/code_to_breed.json", "r") as file:
        return json.load(file)


def randomize_inputs():
    st.session_state.user_input = np.random.randint(
        1, 3, size=len(st.session_state.traits)
    ).tolist()


def reset_inputs():
    st.session_state.user_input = [2] * len(st.session_state.traits)


def add_slider(trait_id: int, help_text: str = "TODO"):
    st.session_state.user_input[trait_id] = st.slider(
        label=st.session_state.traits[trait_id],
        min_value=1,
        max_value=3,
        value=st.session_state.user_input[trait_id],
        help=help_text
    )


# Recommend the breed based on user input
def recommend():
    # TODO: convert to use DB
    recommender = load_model()
    code_to_breed = load_code_to_breed()

    # map from 1-3 range to 1-5 range
    user_input_converted = [
        (x-1) * (4/2) + 1
        for x in st.session_state.user_input
    ]

    prediction = recommender.predict([user_input_converted])[0]
    breed = code_to_breed.get(str(prediction), "")

    if breed:
        st.session_state.breed_image_url = f.get_breed_image_url_db(breed)
        print(f"Recommended breed: {breed}")
        st.session_state.recommendation = (
            f"Rekomendowana rasa to: \"{breed}\""
            # "[Przeglądaj dostępne psy](Przeglądaj_Psy)"
        )
        st.session_state.error_message = ""
    else:
        st.session_state.breed_image_url = ""
        st.session_state.recommendation = ""
        st.session_state.error_message = "Wystąpił błąd"


def main():
    f.setup_page()
    f.add_back_button()

    st.header("Rekomendowanie rasy")

    st.session_state.traits = f.get_traits_pl_db()

    if "user_input" not in st.session_state:
        reset_inputs()
    if "recommendation" not in st.session_state:
        st.session_state.recommendation = ""
    if "error_message" not in st.session_state:
        st.session_state.error_message = ""
    if "breed_image_url" not in st.session_state:
        st.session_state.breed_image_url = ""

    with st.container():
        st.write("na podstawie Twoich preferencji dotyczących cech psa")

        f.add_header("Charakter: Cechy społeczne")
        with st.container():
            col_1, col_2 = st.columns(2)
            with col_1:
                add_slider(0)
                add_slider(1)
                add_slider(2)
            with col_2:
                add_slider(8)
                add_slider(10)
                add_slider(14)

        f.add_header("Charakter: Psychika i zabawa")
        with st.container():
            col_1, col_2 = st.columns(2)
            with col_1:
                add_slider(13)
                add_slider(9)
                add_slider(15)
            with col_2:
                add_slider(12)
                add_slider(11)

        f.add_header("Cechy fizyczne ")
        with st.container():
            col_1, col_2 = st.columns(2)
            with col_1:
                add_slider(5)
                add_slider(6)
                add_slider(7)
            with col_2:
                add_slider(3)
                add_slider(4)

        st.button("Domyślne", on_click=reset_inputs, use_container_width=True)
        st.button("Losowe (DEV)", on_click=randomize_inputs, use_container_width=True)
        st.button("Rekomenduj", on_click=recommend, type="primary", use_container_width=True)

        # Placeholders
        recommendation_placeholder = st.empty()
        error_placeholder = st.empty()
        breed_image = st.empty()

        # Display the recommendation or error message
        if st.session_state.recommendation:
            recommendation_placeholder.success(st.session_state.recommendation)
        if st.session_state.error_message:
            error_placeholder.error(st.session_state.error_message)
        if st.session_state.breed_image_url:
            breed_image.image(st.session_state.breed_image_url)


if __name__ == "__main__":
    main()
