# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st

from website import functions as f


def update_dogs_list():
    # https://discuss.streamlit.io/t/selectbox-gives-me-the-previous-value-instead-of-the-current-value/63132
    breed = st.session_state.breed_selectbox
    dogs_of_breed = f.get_dogs_of_breed_db(breed)

    i = 0
    for dog in dogs_of_breed:
        st.session_state.dogs_list[i].image(dog.photo, width=200, caption=dog.name)
        st.session_state.dogs_list[i+1].markdown(dog.description)
        i += 2


def main():
    f.setup_page()
    f.add_back_button()

    st.header("Przeglądanie psów")

    breeds = f.get_breeds_db()
    breeds.insert(0, "")
    st.selectbox(
        'Rasa',
        breeds,
        on_change=update_dogs_list,
        key="breed_selectbox"
    )

    col_1, col_2 = st.columns(2)
    with col_1:
        st.write("Zdjęcie i imię")
    with col_2:
        st.write("Opis")

    if "dogs_list" not in st.session_state:
        st.session_state.dogs_list = []

    rows = [
        st.columns(2) for _ in range(10)
    ]

    st.session_state.dogs_list = []
    for i, row in enumerate(rows):
        for col in row:
            dogs_number = len(f.get_dogs_of_breed_db(st.session_state.breed_selectbox))
            if dogs_number < 1 or i >= dogs_number:
                height = 0
            else:
                height = 250
            container = col.container(height=height, border=False)
            st.session_state.dogs_list.append(container)


if __name__ == "__main__":
    main()
