"""Home page of the Streamlit app."""

import streamlit as st
from utils.set_page_config import set_page_config

def main() -> None:
    """Home page of the Streamlit app."""
    set_page_config()
    st.title("Welcome to Temari calculator")
    st.image("streamlit_app/images/temari.jpg", caption="Temari")
    st.write("This application is a calculator for temari balls. It calculates the number of divisions for a temari ball based on the circumference of the ball.")
    st.write("To get started, navigate to the Calculator page using the sidebar on the left.")


if __name__ == "__main__":
    main()
