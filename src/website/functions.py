# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

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
        "Przyjazność w kontaktach z innymi Psami",
        "Poziom linienia",
        "Częstotliwość pielęgnacji sierści",
        "Poziom ślinienia",
        "Rodzaj sierści",
        "Długość sierści",
        "Otwartość na obcych",
        "Poziom zabawowości",
        "Charakter stróżujący/opiekuńczy",
        "Zdolności adpatacyjne",
        "Podatność na szkolenie",
        "Energiczność",
        "Szczekanie",
        "Potrzeba stymulacji psychicznej"
    ]


def get_breed_image_url(breed: str) -> str:
    df = pd.read_csv("./data/breed_rank.csv")
    breed_row = df[df["Breed"] == breed]
    return breed_row.iloc[0]["Image"]
