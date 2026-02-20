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

st.title("DMX Address Calculator")
st.caption(f"Version {VERSION}")

st.divider()

# ---- INPUT SECTION ----

group_name = st.text_input("Group name", value="Group 1")

col1, col2 = st.columns(2)

with col1:
    universe = st.number_input("Universe", min_value=1, value=1, step=1)
    first_fixture_nr = st.number_input(
        "First fixture number", min_value=1, value=1, step=1
    )
    nr_of_fixtures = st.number_input("Number of fixtures", min_value=1, value=1, step=1)

with col2:
    first_address = st.number_input("First address", min_value=1, value=1, step=1)
    nr_of_channels = st.number_input(
        "Channels per fixture", min_value=1, value=1, step=1
    )
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
        st.success("Addresses generated successfully.")

        st.subheader("Address Table")

        # Convert backend output to DataFrame
        df_raw = pd.DataFrame(address_table)

        # Based on your backend structure:
        # 0 = Group
        # 1 = Fixture number
        # 3 = Universe number
        # 5 = Address
        df = pd.DataFrame(
            {
                "Group": df_raw[0],
                "Fixture": df_raw[1],
                "Universe": df_raw[3],
                "Address": df_raw[5],
            }
        )

        # Remove index (no row numbers)
        df = df.reset_index(drop=True)

        # Left align everything
        styled_df = df.style.set_properties(**{"text-align": "left"})

        st.table(styled_df)

        st.subheader("Last Channel Used")
        st.write(last_channel)
