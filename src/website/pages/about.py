# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from website import functions as f


def main():
    f.setup_page()
    # f.add_app_header()
    f.add_back_button()

    st.header("O aplikacji")
    st.markdown("""
    DogMatch jest aplikacją stworzoną aby rozwiązywać odwieczny lecz niedawno coraz bardziej zauważany problem. Osoby poszukujące psa do adopcji lub kupna,
    często nie wiedzą jakie rasy psów są dla nich odpowiednie, nie znają ich potrzeb, charakteru i wymagań.
    Z tego powodu, nierzadko zdarza się, że niezadowoleni właściciele dość szybko zwracają psy, bądź nawet porzucają je na ulicy.
    Z drugiej strony, psy których potrzeby nie są zaspokajane stają się nieszczęśliwe, co często jeszcze bardziej pogarsza świeżo nawiązaną relację z nową rodziną.
    Aby temu zapobiec, powstała nowatorska aplikacja DogMatch! Na podstawie autorskiego modelu sztucznej inteligencji pomaga ona w doborze odpowiedniej rasy psa 
    po zadaniu kilku prostych pytań na które odpowiada użytkownik. Procedura rekomendacji z perspektywy przyszłego właściciela jest szybka, prosta i intuicyjna.

    Ponadto, aplikacja jest swoistą platformą łączącą schroniska, przytułki, domy tymczasowe oraz hodowle z osobami poszukującymi psa.
    Dzięki intuicyjnemu mechanizmowi dodawania i przeglądania psów, użytkownicy po zdecydowaniu się na daną rasę, mogą wygodnie przejrzeć psy czekające na dom w całej Polsce.
    Wszystko to po to, aby jak najwięcej psów znalazło swoje nowe, kochające domy, a nowi właściciele byli zadowoleni z podjętej decyzji.

    Funkcje aplikacji obejmują:

    - Rekomendacja rasy psa na podstawie odpowiedzi na proste pytania
    - Edukacja na temat cech i potrzeb danej rasy
    - Dodawanie psów czekających na nowy dom do bazy danych
    - Przeglądanie psów poszukujących domu w całej Polsce

    Nasz zespół składa się z 5 osób, inżynierów z różnych dziedzin, pasjonatów, programistów ze świetnymi umiejętnościami i doświadczeniem:
    - Piotr Gręda
    - Szymon Skarzyński
    - Łukasz Szarejko
    - Patryk Będkowski
    - Paweł Baran

    Model został oparty o bibliotekę  [Recommenders Github](https://github.com/recommenders-team/recommenders). Wykorzystywany zbiór danych to [Dog Breeds](https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds).
                
    Aplikacja DogMatch powstała w ramach przedmiotu Zarządzanie Produktami Data science na Wydziale Elektroniki i Technik Informacyjnych Politechniki Warszawskiej. 
    """)

    with st.popover(":orange[Opcje deweloperskie]"):
        st.button(label=":red[Czyszczenie tabeli \"Animals\"]", on_click=f.clear_animals_table_db)

if __name__ == "__main__":
    main()
