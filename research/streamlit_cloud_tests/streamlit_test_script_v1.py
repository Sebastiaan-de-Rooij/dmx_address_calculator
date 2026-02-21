# import streamlit as st

# st.title("Button Test")


# button_1 = False


# def button_1_press():
#     global button_1
#     button_1 = not button_1


# def print_line_1():
#     global button_1
#     if button_1:
#         st.write("active")
#     else:
#         st.write("inactive")


# print_line_1()
# button_1_press()
# print_line_1()


import streamlit as st

st.title("Button Test")

# Initialize state (only once)
if "button_1" not in st.session_state:
    st.session_state.button_1 = False


def button_1_press():
    st.session_state.button_1 = not st.session_state.button_1


def print_line_1():
    if st.session_state.button_1:
        st.write("active")
    else:
        st.write("inactive")


# UI
st.button("Toggle Button 1", on_click=button_1_press)

print_line_1()
