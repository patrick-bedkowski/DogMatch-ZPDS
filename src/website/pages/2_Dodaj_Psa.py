# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def add_dog():
    if st.session_state.name and st.session_state.breed in f.get_breeds():
        st.session_state.success_message = "Dodano psa"
        st.session_state.error_message = ""

        # TODO: actual adding to DB
    else:
        st.session_state.success_message = ""
        st.session_state.error_message = "Wprowadź rasę oraz imię"


def main():

    # st.title("Page two")

    # st.set_page_config(layout="wide")
    st.set_page_config(page_title="DogMatch", page_icon="🐶")

    # Streamlit UI
    st.markdown(
        """
        <div style="background-color:orange;">
        <h2 style="color:black;text-align:center;">DogMatch</h2>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        button[kind="primary"] {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if "name" not in st.session_state:
        st.session_state.name = ""
    if "success_message" not in st.session_state:
        st.session_state.success_message = ""
    if "error_message" not in st.session_state:
        st.session_state.error_message = ""

    breeds = f.get_breeds()
    breeds.insert(0, "")
    st.session_state.breed = st.selectbox(
        'Rasa',
        breeds
    )

    st.session_state.name = st.text_input(
        label="Imię"
    )

    st.session_state.description = st.text_area(
        label="Opis", max_chars=1000
    )

    st.session_state.photo = st.file_uploader(
        label="Zdjęcie", type=["png", "jpg", "bmp", "tiff"]
    )

    st.button("Dodaj", on_click=add_dog, type="primary")

    success_placeholder = st.empty()
    error_placeholder = st.empty()

    if st.session_state.success_message:
        success_placeholder.success(st.session_state.success_message)
    if st.session_state.error_message:
        error_placeholder.error(st.session_state.error_message)


if __name__ == "__main__":
    main()
