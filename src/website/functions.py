# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st
import pandas as pd


def get_breeds():
    df = pd.read_csv("./data/breed_rank.csv")
    return df['Breed'].unique().tolist()


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
        "Protective Nature",  # original: Watchdog/Protective Nature
        "Adaptability Level",
        "Trainability Level",
        "Energy Level",
        "Barking Level",
        "Mental Stimulation Needs"
    ]


def get_breed_image_url(breed: str) -> str:
    df = pd.read_csv("./data/breed_rank.csv")
    breed_row = df[df["Breed"] == breed]
    st.session_state.breed_image_url = breed_row.iloc[0]["Image"]
