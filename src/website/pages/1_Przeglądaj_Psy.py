# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def main():

    # st.title("Page two")

    # st.set_page_config(layout="wide")
    st.set_page_config(page_title="DogMatch", page_icon="🐶")

    # Streamlit UI
    st.markdown(
        """
        <div style="background-color:orange;">
        <h2 style="color:black;text-align:center;">DogMatch</h2>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )

    breeds = f.get_breeds()
    breeds.insert(0, "")
    st.session_state.breed = st.selectbox(
        'Rasa',
        breeds
    )

    st.write("TODO")


if __name__ == "__main__":
    main()
