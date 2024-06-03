# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


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

    row_1 = st.columns(2)
    row_2 = st.columns(2)
    row_3 = st.columns(2)
    row_4 = st.columns(2)
    row_5 = st.columns(2)

    st.session_state.dogs_list = []
    for i, col in enumerate(row_1 + row_2 + row_3 + row_4 + row_5):
        container = col.container(height=250, border=False)
        st.session_state.dogs_list.append(container)


if __name__ == "__main__":
    main()
