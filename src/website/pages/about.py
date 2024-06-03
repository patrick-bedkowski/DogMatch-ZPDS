# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""


import streamlit as st

import functions as f


def main():
    f.setup_page()
    # f.add_app_header()
    f.add_back_button()

    st.header("O aplikacji")
    st.write("TODO")  # TODO: provide information about the app


if __name__ == "__main__":
    main()
