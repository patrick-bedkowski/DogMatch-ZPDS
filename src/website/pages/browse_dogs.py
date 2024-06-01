# -*- coding: utf-8 -*-
"""
@author: dogmatch.team.co
"""

import streamlit as st

import functions as f


def main():

    # st.title("Page two")

    # st.set_page_config(layout="wide")
    st.set_page_config(page_title="DogMatch", page_icon="🐕")

    # Streamlit UI
    title = """
    <div style="background-color:tomato;">
    <h2 style="color:white;text-align:center;">DogMatch</h2>
    </div>
    """
    st.markdown(title, unsafe_allow_html=True)

    st.session_state.breed = st.selectbox(
        'Rasa',
        f.get_breeds()
    )

    st.write("TODO")


if __name__ == "__main__":
    main()
