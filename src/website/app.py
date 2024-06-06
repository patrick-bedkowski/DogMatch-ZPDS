# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import functions as f


def main():

    if 'initialized' not in st.session_state:
        # Perform initialization steps
        f.prepare_db()        
        # Set up the session state flag to indicate initialization is done
        st.session_state.initialized = True

    f.setup_page()
    f.add_app_header()

    global fields

    col_1, col_2 = st.columns(2)

    with col_1:
        if st.button(":white[🔎Szukam Psa]", use_container_width=True):
            st.switch_page("pages/recommend.py")

    with col_2:
        if st.button(":white[➕Dodaję Psa]", use_container_width=True):
            st.switch_page("pages/add.py")

    # TODO: add some dogs here probably
    if st.button(":white[🗃️Przeglądaj Psy]", use_container_width=True):
        st.switch_page("pages/browse.py")

    if st.button(":white[ℹ️O aplikacji]", use_container_width=True):
        st.switch_page("pages/about.py")


if __name__ == "__main__":
    main()
