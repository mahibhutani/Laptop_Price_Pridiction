import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model and dataset
# -----------------------------
model = joblib.load("model.pkl")
df = pd.read_csv("Cleaned_data.csv")

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop specifications to estimate its price.")

st.divider()

# -----------------------------
# Input fields
# -----------------------------

company = st.selectbox(
    "Company",
    sorted(df["Company"].dropna().unique())
)

typename = st.selectbox(
    "Laptop Type",
    sorted(df["TypeName"].dropna().unique())
)

cpu = st.selectbox(
    "CPU",
    sorted(df["Cpu"].dropna().unique())
)

ram = st.selectbox(
    "RAM (GB)",
    sorted(df["Ram"].dropna().unique())
)

gpu = st.selectbox(
    "GPU",
    sorted(df["Gpu"].dropna().unique())
)

opsys = st.selectbox(
    "Operating System",
    sorted(df["OpSys"].dropna().unique())
)

weight = st.number_input(
    "Weight (kg)",
    min_value=float(df["Weight"].min()),
    max_value=float(df["Weight"].max()),
    value=float(df["Weight"].median()),
    step=0.1
)

touchscreen = st.selectbox(
    "TouchScreen",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

ips = st.selectbox(
    "IPS Display",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

ppi = st.number_input(
    "PPI",
    min_value=float(df["ppi"].min()),
    max_value=float(df["ppi"].max()),
    value=float(df["ppi"].median()),
    step=1.0
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Price", use_container_width=True):

    input_data = pd.DataFrame({
        "Company": [company],
        "TypeName": [typename],
        "Cpu": [cpu],
        "Ram": [ram],
        "Gpu": [gpu],
        "OpSys": [opsys],
        "Weight": [weight],
        "TouchScreen": [touchscreen],
        "IPS": [ips],
        "ppi": [ppi]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"### Estimated Laptop Price: ₹{prediction:,.0f}"
    )
    