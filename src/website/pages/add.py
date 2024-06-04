# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def add_dog():
    if st.session_state.name and st.session_state.breed in f.get_breeds_db() and st.session_state.photo:
        result = f.add_dog_to_db(
            st.session_state.name,
            st.session_state.breed,
            st.session_state.description,
            st.session_state.photo.read(),
            0  # TODO
        )

        if result:
            st.session_state.success_message = "Dodano psa"
            st.session_state.error_message = ""
        else:
            st.session_state.success_message = ""
            st.session_state.error_message = "Wystąpił błąd"
    else:
        st.session_state.success_message = ""
        st.session_state.error_message = "Wprowadź rasę, imię oraz zdjęcie"


def main():
    f.setup_page()
    f.add_back_button()

    st.header("Dodawanie psa")

    if "name" not in st.session_state:
        st.session_state.name = ""
    if "success_message" not in st.session_state:
        st.session_state.success_message = ""
    if "error_message" not in st.session_state:
        st.session_state.error_message = ""

    breeds = f.get_breeds_db()
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

    st.button("Dodaj", on_click=add_dog, type="primary", use_container_width=True)

    success_placeholder = st.empty()
    error_placeholder = st.empty()

    if st.session_state.success_message:
        success_placeholder.success(st.session_state.success_message)
    if st.session_state.error_message:
        error_placeholder.error(st.session_state.error_message)


if __name__ == "__main__":
    main()
