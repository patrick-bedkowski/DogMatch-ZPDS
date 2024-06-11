# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import numpy as np
import pickle
import streamlit as st
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from website import functions as f


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
        1, 6, size=len(st.session_state.traits)
    ).tolist()

    st.session_state.user_input[7] = np.random.randint(1, 4)


def reset_inputs():
    st.session_state.user_input = [3] * len(st.session_state.traits)
    st.session_state.user_input[6] = None
    st.session_state.user_input[7] = 2


def toogle_traits():
    for trait_id in range(len(st.session_state.traits)):
        st.session_state.traits_disabled[trait_id] = not st.session_state[f"toogle_{trait_id}"]


def add_slider(trait_id: int, max_value: int = 5):
    st.session_state.user_input[trait_id] = st.slider(
        label=st.session_state.traits[trait_id][0],
        min_value=1,
        max_value=max_value,
        value=st.session_state.user_input[trait_id],
        help=st.session_state.traits[trait_id][1],
        key=f"slider_{trait_id}",
        disabled=st.session_state.traits_disabled[trait_id]
    )
    st.toggle("Toogle", label_visibility="hidden", key=f"toogle_{trait_id}", on_change=toogle_traits, value=True)


def add_coat_type_selectbox():
    trait_id = 6

    st.session_state.user_input[trait_id] = st.selectbox(
        label=st.session_state.traits[trait_id][0],
        options=f.get_coat_types_pl_db(),
        help=st.session_state.traits[trait_id][1],
        placeholder="Wybierz",
        index=None,
        key=f"selectbox_{trait_id}",
        disabled=st.session_state.traits_disabled[trait_id]
    )
    st.toggle("Toogle", label_visibility="hidden", key=f"toogle_{trait_id}", on_change=toogle_traits, value=True)


# Recommend the breed based on user input
def recommend():
    if st.session_state.user_input[6]:
        # get numeric value of coat type
        st.session_state.user_input[6] = f.get_coat_type_id_db(st.session_state.user_input[6])

    user_input_converted = st.session_state.user_input

    # Disable some traits
    for trait_id in range(len(user_input_converted)):
        if st.session_state.traits_disabled[trait_id]:
            user_input_converted[trait_id] = None

    print("\n===PROCESSED INPUT===")
    for trait, value in zip(st.session_state.traits, user_input_converted):
        print(value)

    recommender = load_model()
    code_to_breed = load_code_to_breed()

    prediction = recommender.predict([user_input_converted])[0]
    breed = code_to_breed.get(str(prediction), "")

    if breed:
        st.session_state.breed_image_url = f.get_breed_image_url_db(breed)
        print(f"\nRecommended breed: {breed}")
        st.session_state.recommendation = (
            f"Rekomendowana rasa to: \"{breed}\" ({f.get_breed_info_url_db(breed)})"
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
    if 'traits_disabled' not in st.session_state:
        st.session_state.traits_disabled = {
            trait_id: False
            for trait_id, trait
            in enumerate(st.session_state.traits)
        }

    with st.container():
        st.write("na podstawie Twoich preferencji dotyczących cech psa")

        f.add_header("Cechy społeczne")
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

        f.add_header("Psychika i zabawa")
        with st.container():
            col_1, col_2 = st.columns(2)
            with col_1:
                add_slider(13)
                add_slider(9)
                add_slider(15)
            with col_2:
                add_slider(12)
                add_slider(11)

        f.add_header("Cechy fizyczne")
        with st.container():
            col_1, col_2 = st.columns(2)
            with col_1:
                add_slider(5)
                add_coat_type_selectbox()
                add_slider(7, max_value=3)
            with col_2:
                add_slider(3)
                add_slider(4)

        st.button("Domyślne", on_click=reset_inputs, use_container_width=True)
        st.button("Losowe", on_click=randomize_inputs, use_container_width=True)
        if st.button("Rekomenduj", type="primary", use_container_width=True):
            with st.spinner('Przygotowywanie rekomendacji...'):
                recommend()

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
