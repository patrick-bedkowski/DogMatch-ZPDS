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
        1, 6, size=len(st.session_state.fields)
    ).tolist()


def reset_inputs():
    st.session_state.user_input = [3] * len(st.session_state.fields)


# Recommend the breed based on user input
def recommend():
    # TODO: convert to use DB
    recommender = load_model()
    code_to_breed = load_code_to_breed()
    prediction = recommender.predict([st.session_state.user_input])[0]
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

    col_1, col_2 = st.columns(2)

    # Input fields
    st.session_state.fields = f.get_traits_pl_db()

    # Initialize session state for input values if not present
    if "user_input" not in st.session_state:
        st.session_state.user_input = [3] * len(st.session_state.fields)
    if "recommendation" not in st.session_state:
        st.session_state.recommendation = ""
    if "error_message" not in st.session_state:
        st.session_state.error_message = ""
    if "breed_image_url" not in st.session_state:
        st.session_state.breed_image_url = ""

    with st.container():
        st.markdown(
            """
            <br>
            <h3 style="color:white;text-align:center;">Preferowane cechy psa</h3>
            <br>
            """,
            unsafe_allow_html=True
        )

        # Input collection with sliders arranged in columns
        col_1, col_2, col_3, col_4 = st.columns(4)
        for i, field in enumerate(st.session_state.fields):
            col_index = i // 4
            user_input = [col_1, col_2, col_3, col_4][col_index].slider(
                field, 1, 5, st.session_state.user_input[i]
            )
            st.session_state.user_input[i] = user_input

        # Buttons with callbacks
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
