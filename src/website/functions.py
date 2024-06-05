# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import pandas as pd
import streamlit as st

import sys
sys.path.append('../../../DogMatch')
from BE import database
# from BE import configuration
from BE import seed_data, animal
from BE.seed_data import seedData
from deprecated import deprecated  # type: ignore
from BE.configuration import BREED_TRAITS_PATH


def prepare_db():
    sessionmaker = database.createConnection()
    session = sessionmaker()
    seedData(session, BREED_TRAITS_PATH)
    session.close()


def clear_animals_table_db():
    sessionmaker = database.createConnection()
    session = sessionmaker()
    database.clear_table(session, animal.Animal)
    session.close()


@deprecated
def get_breeds() -> list:
    df = pd.read_csv("./data/breed_rank.csv")
    return df['Breed'].unique().tolist()


def get_breeds_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    breeds = database.get_table(session, seed_data.DictDogBreed)
    session.close()
    return [breed.token for breed in breeds]


def get_dogs_of_breed_db(breed_name: str) -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    all_dogs = database.get_table(session, animal.Animal)
    session.close()
    dogs_of_breed = [
        dog for dog in all_dogs
        if dog.breed.split() == breed_name.split()
    ]
    return dogs_of_breed


def get_traits_pl_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    traits = database.get_table(session, seed_data.Trait)
    session.close()
    return [
        trait.name_pl
        for trait in traits
    ]


def get_coat_types_pl_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    types = database.get_table(session, seed_data.DictCoatType)
    session.close()
    return [
        type.token_pl
        for type in types
    ]


def get_coat_type_id_db(coat_type: str) -> int:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    types = database.get_table(session, seed_data.DictCoatType)
    session.close()
    for type in types:
        if type.token == coat_type or type.token_pl == coat_type:
            return type.id
    return None


@deprecated
def get_breed_image_url(breed: str) -> str:
    df = pd.read_csv("./data/breed_rank.csv")
    breed_row = df[df["Breed"] == breed]
    return breed_row.iloc[0]["Image"]


def get_breed_id_db(breed_name: str) -> int:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    breeds = database.get_table(session, seed_data.DictDogBreed)
    session.close()
    for breed in breeds:
        # added the "split()" becasue it seems that the spaces are somehow different in DB
        if breed.token.split() == breed_name.split():
            return breed.id
    return None


def get_breed_image_url_db(breed_name: str) -> str:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    breed_id = get_breed_id_db(breed_name)
    breeds = database.get_table(session, seed_data.DogBreed)
    session.close()
    for breed in breeds:
        if breed.dict_breed_id == breed_id:
            return breed.photo_url
    return None


def add_dog_to_db(name, breed, description, photo, owner_id):
    sessionmaker = database.createConnection()
    session = sessionmaker()
    dog = animal.Animal(name, breed, description, photo, owner_id)
    session.add(dog)
    session.commit()
    session.close()
    return True


def add_app_header():
    st.markdown(
        """
        <div style="background-color:orange;">
        <h2 style="color:black;text-align:center;">🐶DogMatch</h2>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )


def adjust_primary_buttons_text_color():
    # you can use ":color[text to be colored]" in streamlit
    # but let's use this to change all buttons from one place
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


def adjust_buttons():
    st.markdown(
        """
        <style>
        button {
            height: auto;
            padding-top: 15px !important;
            padding-bottom: 15px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def disable_sidebar():
    # remember to also set "initial_sidebar_state="collapsed"" in st.set_page_config()
    st.markdown(
        """
        <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def adjust_padding():
    # remember to also set "initial_sidebar_state="collapsed"" in st.set_page_config()
    st.markdown(
        """
        <style>
        [data-testid="stAppViewBlockContainer"] {
            padding-top: 0%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def setup_page():
    # st.set_page_config(layout="wide")
    st.set_page_config(page_title="DogMatch", page_icon="🐶", initial_sidebar_state="collapsed")
    adjust_primary_buttons_text_color()
    disable_sidebar()
    adjust_buttons()
    adjust_padding()


def add_back_button(pl: bool = True):
    if pl:
        if st.button("⬅️ Powrót", use_container_width=True):
            st.switch_page("app.py")


def add_header(text: str):
    st.markdown(
        f"""
        <br>
        <h3 style="color:white;text-align:center;">{text}</h3>
        <br>
        """,
        unsafe_allow_html=True
    )
