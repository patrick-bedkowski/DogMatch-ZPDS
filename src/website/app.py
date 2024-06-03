# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def main():
    f.setup_page()
    f.add_app_header()

    global fields

    col_1, col_2 = st.columns(2)

    with col_1:
        if st.button(":green[Szukam Psa]", use_container_width=True):
            st.switch_page("pages/recommend.py")

    with col_2:
        if st.button(":blue[Dodaję Psa]", use_container_width=True):
            st.switch_page("pages/add.py")

    # TODO: add some dogs here probably
    if st.button(":orange[Przeglądaj Psy]", use_container_width=True):
        st.switch_page("pages/browse.py")


if __name__ == "__main__":
    main()
