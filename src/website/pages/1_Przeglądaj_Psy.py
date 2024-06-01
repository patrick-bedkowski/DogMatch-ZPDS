# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def main():
    st.set_page_config(page_title="DogMatch", page_icon="🐶")

    f.add_page_header()
    f.adjust_primary_buttons_colors()

    breeds = f.get_breeds_db()
    breeds.insert(0, "")
    st.session_state.breed = st.selectbox(
        'Rasa',
        breeds
    )

    st.write("TODO")


if __name__ == "__main__":
    main()
