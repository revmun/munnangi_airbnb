from PIL import Image
import streamlit as st


def get_profile_pic():
    return Image.open('profile.png')


def write():

    st.sidebar.image(get_profile_pic(), use_column_width=False, width=250)
    st.sidebar.header("Welcome!")
    st.sidebar.markdown(
        "*I am a student for Data Analytics at Bentley University.*")

    st.sidebar.markdown("**Author**: Rev Munnangi")
    st.sidebar.markdown("**Mail**: Munnang_reva@bentley.edu")
