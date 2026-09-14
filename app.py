import streamlit as st

import pandas as pd

from discovery_engine import AutonomousDiscoveryEngine

st.set_page_config(page_title="TVB Lead Sourcing Agent", layout="wide")

st.title("🚀 TVB Autonomous Lead Sourcing & Screening")

st.markdown("Operator VC Tool for $1M-$5M Scale-ups entering the US Market.")

# Initialize Engine

engine = AutonomousDiscoveryEngine()

leads_df = engine.get_verified_leads()

# Metric Cards

col1, col2, col3 = st.columns(3)

col1.metric("Total Leads", len(leads_df))

col2.metric("Avg. Funding", f"${leads_df['Funding Raised ($ USD)'].mean():,.0f}")

col3.metric("Tech Platforms", "100%")

# Interactive Filters

st.sidebar.header("Filter Leads")

sector_filter = st.sidebar.multiselect("Select Sector", options=leads_df['Sector/Industry'].unique(), default=leads_df['Sector/Industry'].unique())

funding_range = st.sidebar.slider("Funding Range ($ USD)", 1000000, 5000000, (1000000, 5000000))

filtered_df = leads_df[

    (leads_df['Sector/Industry'].isin(sector_filter)) & 

    (leads_df['Funding Raised ($ USD)'].between(funding_range[0], funding_range[1]))

]

# Lead Table

st.subheader("Verified Target Dataset")

st.dataframe(filtered_df, use_container_width=True)

# Validation Sandbox

st.subheader("🛠️ Interactive Validation Sandbox")

with st.expander("Test Lead Against TVB Thesis"):

    test_funding = st.number_input("Enter Funding Amount", value=2000000)

    test_region = st.selectbox("Select Region", ["Europe", "India", "Southeast Asia", "USA"])

    

    if st.button("Validate"):

        is_valid = engine.validator.validate(test_funding, test_region)

        if is_valid:

            st.success("Target matches TVB Thesis: Proceed with outreach.")

        else:

            st.error("Target disqualified: Outside thesis parameters.")

# Downloads

st.sidebar.subheader("Export Data")

st.sidebar.download_button("Download CSV", filtered_df.to_csv(index=False), "tvb_leads.csv", "text/csv")

st.sidebar.download_button("Download JSON", filtered_df.to_json(orient="records"), "tvb_leads.json", "application/json")
