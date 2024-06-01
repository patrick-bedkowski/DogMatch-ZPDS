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


def get_breeds() -> list:
    df = pd.read_csv("./data/breed_rank.csv")
    return df['Breed'].unique().tolist()


def get_breeds_db() -> list:
    sessionmaker = database.createConnection()
    session = sessionmaker()
    breeds = database.get_table(session, seed_data.DictDogBreed)
    return [breed.token for breed in breeds]


def get_traits() -> list:
    return [
        "Affectionate With Family",
        "Good With Young Children",
        "Good With Other Dogs",
        "Shedding Level",
        "Coat Grooming Frequency",
        "Drooling Level",
        "Coat Type",
        "Coat Length",
        "Openness To Strangers",
        "Playfulness Level",
        "Watchdog/Protective Nature",
        "Adaptability Level",
        "Trainability Level",
        "Energy Level",
        "Barking Level",
        "Mental Stimulation Needs"
    ]


def get_traits_db() -> list:
    return [
        "Affectionate With Family",
        "Good With Young Children",
        "Good With Other Dogs",
        "Shedding Level",
        "Coat Grooming Frequency",
        "Drooling Level",
        "Coat Type",
        "Coat Length",
        "Openness To Strangers",
        "Playfulness Level",
        "Watchdog/Protective Nature",
        "Adaptability Level",
        "Trainability Level",
        "Energy Level",
        "Barking Level",
        "Mental Stimulation Needs"
    ]


def get_traits_PL() -> list:
    return [
        "Czułość w kontaktach z rodziną",
        "Przyjazność w kontaktach z małymi dziećmi",
        "Przyjazność w kontaktach z innymi psami",
        "Linienie",
        "Częstotliwość pielęgnacji sierści",
        "Ślinienie",
        "Rodzaj sierści",
        "Długość sierści",
        "Otwartość na obcych",
        "Zabawowość",
        "Charakter stróżujący/opiekuńczy",
        "Adpatacyjność",
        "Podatność na szkolenie",
        "Energiczność",
        "Szczekanie",
        "Potrzeba stymulacji psychicznej"
    ]


def get_breed_image_url(breed: str) -> str:
    df = pd.read_csv("./data/breed_rank.csv")
    breed_row = df[df["Breed"] == breed]
    return breed_row.iloc[0]["Image"]


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
