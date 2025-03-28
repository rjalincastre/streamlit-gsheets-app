import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the sheet into a DataFrame
df = conn.read()

# Print each row
st.title("My Google Sheet Viewer")
for row in df.itertuples():
    st.write(f"{row.name} has a {row.pet}")
