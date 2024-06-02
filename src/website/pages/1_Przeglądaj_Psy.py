# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st
import pandas as pd
import random
from BE import animal

import functions as f


def update_dogs_list():
    # https://discuss.streamlit.io/t/selectbox-gives-me-the-previous-value-instead-of-the-current-value/63132
    breed = st.session_state.breed_selectbox
    dogs_of_breed = f.get_dogs_of_breed_db(breed)

    df = [
        [dog.name, dog.description]
        for dog in dogs_of_breed
    ]

    # dogs_of_breed = [dog.name for dog in dogs_of_breed]

    # # print(data)
    # df = pd.DataFrame(
    #     data,
    #     columns=["Name", "Photo", "Description"]
    # )
    st.session_state.dogs_list = df
    # # for dog in dogs_of_breed:
    #     # add_dog_to_list(dog)


def main():
    st.set_page_config(page_title="DogMatch", page_icon="🐶")

    f.add_page_header()
    f.adjust_primary_buttons_colors()

    breeds = f.get_breeds_db()
    breeds.insert(0, "")
    st.selectbox(
        'Rasa',
        breeds,
        on_change=update_dogs_list,
        key="breed_selectbox"
    )

    if "dogs_list" not in st.session_state:
        st.session_state.dogs_list = None

    st.dataframe(st.session_state.dogs_list)


if __name__ == "__main__":
    main()
