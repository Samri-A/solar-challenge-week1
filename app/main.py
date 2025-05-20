import streamlit as st
from utils import Utils  # Capitalized class name
import pandas as pd

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("Solar Radiation Dashboard")

# Sidebar for country selection
country = st.sidebar.selectbox("🌍 Select a Country", ("Benin-malanville", "Sierraleone", "Togo"))

# Instantiate the Utils class
util = Utils(country)
df = util.load_data()

# Sidebar checkboxes
st.sidebar.header("Show")
show_summary = st.sidebar.checkbox("Show Summary Statistics", True)
show_corr = st.sidebar.checkbox("Show Correlation Heatmap", True)
show_GHI = st.sidebar.checkbox("Show GHI", True)
show_DNI = st.sidebar.checkbox("Show DNI", True)
show_DHI = st.sidebar.checkbox("Show DHI", True)
show_comparison = st.sidebar.checkbox("Compare GHI Between Countries", False)

# Display summary
if show_summary:
    st.subheader("📊 Summary Statistics")
    st.dataframe(util.show_summary(df))

# Correlation heatmap
if show_corr:
    st.subheader("🔗 Correlation Heatmap")
    fig_corr = util.show_corr(df)
    st.pyplot(fig_corr)


# Individual irradiance plots
if show_GHI:
    st.subheader("🌤 Global Horizontal Irradiance (GHI)")
    fig_GHI = util.show_GHI(df)
    st.pyplot(fig_GHI)

if show_DNI:
    st.subheader("🔆 Direct Normal Irradiance (DNI)")
    fig_DNI = util.show_DNI(df)
    st.pyplot(fig_DNI)

if show_DHI:
    st.subheader("🌥 Diffuse Horizontal Irradiance (DHI)")
    fig_DHI = util.show_DHI(df)
    st.pyplot(fig_DHI)
    
# Cross-country comparison boxplot
if show_comparison:
    st.subheader("🌍 Cross-Country GHI Comparison")
    fig_cmp = util.show_comparison()
    st.pyplot(fig_cmp)
