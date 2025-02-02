import streamlit as st
from utils.set_page_config import set_page_config
from utils.calculate import calculate

def main() -> None:
    set_page_config()
    st.title("Calculator")
    circumference = st.number_input("Insert a circumference between 1 and 1000", min_value=1, max_value=1000)
    results = calculate(circumference)

    if st.button("Calculate", type="primary"):
        st.header("C10 results", divider=True)
        st.markdown(results['c10_results'], unsafe_allow_html=True)
        st.header("C8 results", divider=True)
        st.markdown(results['c8_results'], unsafe_allow_html=True)
        st.header("C6 results", divider=True)
        st.markdown(results['c6_results'], unsafe_allow_html=True)

if __name__ == "__main__":
    main()
