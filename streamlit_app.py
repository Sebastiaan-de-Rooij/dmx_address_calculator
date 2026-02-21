import streamlit as st
import pandas as pd

from dmx_address_calculator import (
    check_range,
    generate_address_table,
    calculate_last_channel,
    VERSION,
)

# ---- PAGE CONFIG ----

st.set_page_config(
    page_title="DMX Address Calculator",
    layout="centered",
)

# ---- GLOBAL CSS ----

st.markdown(
    """
<style>

/* Center and constrain main content width */
.block-container {
    max-width: 700px;
    padding-top: 2rem;
}

/* Hide table index */
thead tr th:first-child {display:none}
tbody th {display:none}

/* Tight table */
div[data-testid="stTable"] > div {
    width: fit-content !important;
}

table {
    width: auto !important;
}

thead th, tbody td {
    text-align: left !important;
    padding: 6px 12px !important;
}

/* Reduce column gap */
div[data-testid="stHorizontalBlock"] {
    gap: 12px !important;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---- TITLE ----

st.title("DMX Address Calculator")
st.caption(f"Version {VERSION}")

st.divider()

# ---- INPUT SECTION (compact container) ----

group_name = st.text_input(
    "Group name",
    value="Group 1",
    max_chars=25,
)

st.markdown("")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    universe = st.number_input("Universe", min_value=1, value=1, step=1)

with col2:
    first_fixture_nr = st.number_input(
        "First fixture number", min_value=1, value=1, step=1
    )

with col3:
    nr_of_fixtures = st.number_input("Number of fixtures", min_value=1, value=1, step=1)

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    first_address = st.number_input("First address", min_value=1, value=1, step=1)

with col5:
    nr_of_channels = st.number_input(
        "Channels per fixture", min_value=1, value=1, step=1
    )

with col6:
    universe_size = st.number_input("Universe size", min_value=1, value=512, step=1)

st.divider()

# ---- CALCULATION ----

if st.button("Calculate"):

    range_warning = check_range(
        first_address,
        nr_of_channels,
        nr_of_fixtures,
        universe_size,
    )

    address_table = generate_address_table(
        group_name,
        first_fixture_nr,
        universe,
        first_address,
        nr_of_channels,
        nr_of_fixtures,
    )

    last_channel = calculate_last_channel(
        first_address,
        nr_of_channels,
        nr_of_fixtures,
    )

    if range_warning:
        st.error("⚠ Out of range for this universe size.")
    else:
        st.subheader("Address Table")

        df_raw = pd.DataFrame(address_table)

        df = pd.DataFrame(
            {
                "Group": df_raw[0],
                "Fixture": df_raw[1],
                "Universe": df_raw[3],
                "Address": df_raw[5],
            }
        )

        df.index = [""] * len(df)

        st.table(df)

        st.subheader("Last Channel Used")
        st.write(last_channel)
