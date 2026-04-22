import streamlit as st
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("rail_data.db")

# Load data
df = pd.read_sql("SELECT * FROM journeys", conn)

st.title("UK Rail Delay Monitoring Dashboard")

st.metric("Total Journeys", len(df))

delay_rate = (df["delay_status"] != "On Time").mean()
st.metric("Delay Rate", f"{delay_rate:.2%}")

st.subheader("Delay Distribution")
st.bar_chart(df["delay_status"].value_counts())

st.subheader("Top Delay Reasons")
st.write(df["reason_for_delay"].value_counts().head(5))

st.subheader("Filter by Delay Type")
delay_filter = st.selectbox("Select delay type", df["delay_status"].unique())

filtered_df = df[df["delay_status"] == delay_filter]

st.write(filtered_df.head())