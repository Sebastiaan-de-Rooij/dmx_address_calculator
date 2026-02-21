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

# ---- MA STYLE CSS ----

st.markdown(
    """
<style>

/* Constrain layout width */
.block-container {
    max-width: 650px;
    padding-top: 2rem;
}

/* Typography */
html, body, [class*="css"]  {
    font-family: "Inter", sans-serif;
}

/* Input styling */
div[data-baseweb="input"] input {
    background-color: #1a1c22 !important;
    border: 1px solid #2c2f36 !important;
    color: #e5e7eb !important;
    border-radius: 4px !important;
}

/* Button styling */
button[kind="secondary"] {
    background-color: #1a1c22 !important;
    border: 1px solid #2c2f36 !important;
    color: #e5e7eb !important;
    border-radius: 4px !important;
}

button[kind="secondary"]:hover {
    border: 1px solid #3a3f47 !important;
}

/* Column spacing */
div[data-testid="stHorizontalBlock"] {
    gap: 14px !important;
}

/* ---- TABLE ---- */

/* Hide index */
thead tr th:first-child {display:none}
tbody th {display:none}

/* Tight table */
div[data-testid="stTable"] > div {
    width: fit-content !important;
}

table {
    width: auto !important;
    border: 1px solid #2c2f36 !important;
}

thead th, tbody td {
    text-align: left !important;
    padding: 6px 14px !important;
    border-color: #2c2f36 !important;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---- HEADER ----

st.markdown("## DMX Address Calculator")
st.caption(f"v{VERSION}")

st.markdown("---")

# ---- INPUTS ----

group_name = st.text_input("Group Name")

st.markdown("")

col1, col2, col3 = st.columns(3)

with col1:
    universe = st.number_input("Universe", min_value=1, value=1)

with col2:
    first_fixture_nr = st.number_input("First Fixture", min_value=1, value=1)

with col3:
    nr_of_fixtures = st.number_input("Fixtures", min_value=1, value=1)

col4, col5, col6 = st.columns(3)

with col4:
    first_address = st.number_input("Start Address", min_value=1, value=1)

with col5:
    nr_of_channels = st.number_input("Channels", min_value=1, value=1)

with col6:
    universe_size = st.number_input("Universe Size", min_value=1, value=512)

st.markdown("---")

# ---- CALCULATE ----

if st.button("CALCULATE"):

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
        st.error("Out of range for this universe size.")
    else:
        st.markdown("### Address Table")

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

        # ---- INLINE LAST CHANNEL (tight spacing) ----

        st.markdown(
            f"""
        <div style="
            width: fit-content;
            margin-top: 14px;
            display: flex;
            gap: 12px;
            font-size: 15px;
        ">
            <span style="font-weight: 600; color: #cbd5e1;">
                Last Channel
            </span>
            <span style="font-weight: 700; color: #ffffff;">
                {last_channel}
            </span>
        </div>
        """,
            unsafe_allow_html=True,
        )
