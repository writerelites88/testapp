import streamlit as st

# This must be the first command in your app to avoid the StreamlitSetPageConfigMustBeFirstCommandError
st.set_page_config(page_title="Your App Title", page_icon="🤖", layout="wide")

# App title
st.title("Welcome to My Streamlit App!")

# Input section
name = st.text_input("What's your name?")

# Display greeting
if name:
    st.write(f"Hello, {name}! 👋")

# Simple chart
st.write("Here's a simple chart:")
st.line_chart([1, 2, 3, 4, 5])
st.markdown(
    """
    <style>
    iframe { visibility: visible; }
    </style>
    """,
    unsafe_allow_html=True,
)
