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

    with open('./src/website/pages/about.md', 'r', encoding="utf-8") as file:
        st.markdown(file.read())

    with st.popover(":white[Opcje deweloperskie]"):
        st.button(label=":red[Czyszczenie tabeli \"Animals\"]", on_click=f.clear_animals_table_db)


if __name__ == "__main__":
    main()
