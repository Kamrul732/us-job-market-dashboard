import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="U.S. Job Market Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 U.S. Job Market Dashboard")
st.markdown("Analyzing 10 years of U.S. labor market data from the **Bureau of Labor Statistics**")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/bls_cleaned.csv", parse_dates=["date"])
    return df

df = load_data()

# Split series
unemployment = df[df["series"] == "unemployment_rate"]
payrolls = df[df["series"] == "nonfarm_payrolls"]
participation = df[df["series"] == "labor_force_participation"]

# KPI Cards
st.subheader("Latest Snapshot")
col1, col2, col3 = st.columns(3)

latest_u = unemployment.sort_values("date").iloc[-1]["value"]
latest_p = payrolls.sort_values("date").iloc[-1]["value"]
latest_l = participation.sort_values("date").iloc[-1]["value"]

prev_u = unemployment.sort_values("date").iloc[-2]["value"]
prev_p = payrolls.sort_values("date").iloc[-2]["value"]
prev_l = participation.sort_values("date").iloc[-2]["value"]

col1.metric("Unemployment Rate", f"{latest_u}%", f"{round(latest_u - prev_u, 1)}%")
col2.metric("Nonfarm Payrolls", f"{latest_p:,.0f}K", f"{round(latest_p - prev_p, 0):,.0f}K")
col3.metric("Labor Force Participation", f"{latest_l}%", f"{round(latest_l - prev_l, 1)}%")

st.divider()

# Year range filter
st.subheader("Explore the Data")
min_year = int(df["date"].dt.year.min())
max_year = int(df["date"].dt.year.max())

year_range = st.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Filter data
mask = (df["date"].dt.year >= year_range[0]) & (df["date"].dt.year <= year_range[1])
filtered = df[mask]

unemployment_f = filtered[filtered["series"] == "unemployment_rate"]
payrolls_f = filtered[filtered["series"] == "nonfarm_payrolls"]
participation_f = filtered[filtered["series"] == "labor_force_participation"]

# Chart 1 - Unemployment
st.subheader("Unemployment Rate")
fig1 = px.line(
    unemployment_f, x="date", y="value",
    labels={"value": "Rate (%)", "date": "Date"},
    color_discrete_sequence=["#185FA5"]
)
fig1.add_vrect(x0="2020-02-01", x1="2020-04-01",
               fillcolor="#FAEEDA", opacity=0.5,
               annotation_text="COVID", annotation_position="top left")
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 - Payrolls
st.subheader("Monthly Nonfarm Payrolls")
payrolls_f = payrolls_f.copy()
payrolls_f["monthly_change"] = payrolls_f["value"].diff()
payrolls_f["color"] = payrolls_f["monthly_change"].apply(
    lambda x: "Job Gains" if x >= 0 else "Job Losses"
)
fig2 = px.bar(
    payrolls_f, x="date", y="monthly_change",
    color="color",
    color_discrete_map={"Job Gains": "#2E7D32", "Job Losses": "#C62828"},
    labels={"monthly_change": "Jobs Added/Lost", "date": "Date"}
)
fig2.add_vrect(x0="2020-02-01", x1="2020-04-01",
               fillcolor="#FAEEDA", opacity=0.5,
               annotation_text="COVID", annotation_position="top left")
st.plotly_chart(fig2, use_container_width=True)

# Chart 3 - Participation
st.subheader("Labor Force Participation Rate")
fig3 = px.line(
    participation_f, x="date", y="value",
    labels={"value": "Rate (%)", "date": "Date"},
    color_discrete_sequence=["#0F6E56"]
)
fig3.add_hline(y=63.3, line_dash="dash", line_color="gray",
               annotation_text="Pre-COVID level (63.3%)")
fig3.add_vrect(x0="2020-02-01", x1="2020-04-01",
               fillcolor="#FAEEDA", opacity=0.5,
               annotation_text="COVID", annotation_position="top left")
fig3.update_layout(showlegend=False)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Key Insights
st.subheader("Key Insights")
col1, col2 = st.columns(2)

with col1:
    st.info("📈 **COVID Peak** — Unemployment hit 14.8% in April 2020, the highest since the Great Depression")
    st.info("💼 **Record Jobs** — Nonfarm payrolls hit an all-time high of 158,316K in 2024")

with col2:
    st.warning("⚠️ **Participation Gap** — Labor force participation remains below pre-COVID levels, ~3M Americans haven't returned")
    st.warning("📉 **2024 Uptick** — Unemployment crept from 3.7% to 4.2% through 2024 — worth monitoring")

st.divider()
st.caption("Data source: U.S. Bureau of Labor Statistics (BLS) Public API | Series: LNS14000000, CES0000000001, LNS12300000")