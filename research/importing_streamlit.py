"""
Docstring for importing_streamlit

just seeing if i have streamlit installed

also found out that methods are attributes too, just callable ones
and i've not forgotten they're object-tied functions too

"""

# import streamlit as st

# print(st.__version__)
# # __version__ is just an attribute, not a method, so no parentheses!

# test = "test string"

# st.write(test)

import streamlit as st

st.title("DMX Address Calculator")

name = st.text_input("Enter fixture name")

if name:
    st.write(f"Fixture: {name}")
