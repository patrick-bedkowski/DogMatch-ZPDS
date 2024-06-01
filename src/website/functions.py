# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import pandas as pd
import streamlit as st

import sys
sys.path.append('../DogMatch')
from BE import database
from BE import configuration
from BE import seed_data


# def get_breeds() -> list:
#     df = pd.read_csv("./data/breed_rank.csv")
#     return df['Breed'].unique().tolist()


def get_breeds_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    breeds = database.get_table(session, seed_data.DictDogBreed)
    return [breed.token for breed in breeds]


# class Dog:
#     def __init__(self, name, breed, image):
#         self.name = name
#         self.breed = breed
#         self.image = image


def get_dogs_of_breed_db() -> list:
    # TODO
    return None


def get_traits_pl_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    traits = database.get_table(session, seed_data.Trait)
    return [
        trait.name_pl
        for trait in traits
    ]


def get_breed_image_url(breed: str) -> str:
    df = pd.read_csv("./data/breed_rank.csv")
    breed_row = df[df["Breed"] == breed]
    return breed_row.iloc[0]["Image"]


def get_breed_image_url_db(breed: str) -> str:
    # TODO
    return "TODO"


def add_page_header():
    st.markdown(
        """
        <div style="background-color:orange;">
        <h2 style="color:black;text-align:center;">DogMatch</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def adjust_primary_buttons_colors():
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
