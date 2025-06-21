import streamlit as st
import pandas as pd
import os
from datetime import datetime
import plotly.express as px

# File path
DATA_FILE = "data/player_stats.csv"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        df = pd.DataFrame(columns=[
            "Date", "Player", "Sprint", "Juggles", "Dribble", "Goals", "Assists", "Notes"
        ])
        df.to_csv(DATA_FILE, index=False)
        return df

# Save data
def save_data(new_entry):
    df = load_data()
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# --- UI Starts ---
st.set_page_config(page_title="NextPlay Tracker", layout="wide")
st.title("⚽ NextPlay: Project Mbappé Tracker")

st.sidebar.header("Enter Player Stats")

player = st.sidebar.text_input("Player Name")
sprint = st.sidebar.number_input("Sprint Speed (m/s)", min_value=0.0, step=0.1)
juggles = st.sidebar.number_input("Juggling Count", min_value=0)
dribble = st.sidebar.slider("Dribbling Level", 1, 10)
goals = st.sidebar.number_input("Goals Scored", min_value=0)
assists = st.sidebar.number_input("Assists", min_value=0)
notes = st.sidebar.text_area("Training Notes")
date = datetime.now().strftime("%Y-%m-%d")

if st.sidebar.button("Save Entry"):
    entry = pd.DataFrame([{
        "Date": date, "Player": player, "Sprint": sprint,
        "Juggles": juggles, "Dribble": dribble,
        "Goals": goals, "Assists": assists, "Notes": notes
    }])
    save_data(entry)
    st.sidebar.success("Saved ✅")

# Load and display data
df = load_data()
st.subheader("📊 Player Progress Data")
st.dataframe(df.tail(10), use_container_width=True)

# Plot graphs
if not df.empty:
    player_selected = st.selectbox("Select Player for Graph", df["Player"].unique())

    player_df = df[df["Player"] == player_selected]

    col1, col2 = st.columns(2)

    with col1:
        fig = px.line(player_df, x="Date", y="Sprint", title="Sprint Speed Over Time")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.bar(player_df, x="Date", y="Juggles", title="Juggling Count Over Time")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = px.line(player_df, x="Date", y="Dribble", title="Dribbling Skill Over Time")
        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.bar(player_df, x="Date", y=["Goals", "Assists"], barmode="group",
                      title="Goals & Assists Over Time")
        st.plotly_chart(fig4, use_container_width=True)

else:
    st.info("No data yet. Use the sidebar to add player stats.")

