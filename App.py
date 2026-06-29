import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="My Original Forex Trading Bot", layout="wide")
st.title("🤖 My Personal Forex Bot Control Panel")
st.write("Is link se aap apne bot ko kahin se bhi control kar sakte hain.")

# 1. Sidebar - Broker Connection Settings
st.sidebar.header("🔑 Broker Connection Settings")
broker_login = st.sidebar.number_input("MT5 Account Number", value=12345678, step=1)
broker_password = st.sidebar.text_input("MT5 Password", type="password")
broker_server = st.sidebar.text_input("Broker Server Name", value="Exness-MT5-Trial9")

# 2. Bot Main Controls (ON / OFF System)
st.subheader("⚙️ Bot Controls")
col1, col2 = st.columns(2)

if "bot_running" not in st.session_state:
    st.session_state.bot_running = False

with col1:
    if st.button("▶️ START BOT", use_container_width=True):
        st.session_state.bot_running = True
        st.success("Bot Background mein active ho gaya hai!")

with col2:
    if st.button("⏹️ STOP BOT", use_container_width=True):
        st.session_state.bot_running = False
        st.error("Bot ko rok diya gaya hai.")

# Status Indicator
if st.session_state.bot_running:
    st.markdown("### 🟢 Status: **BOT IS TRADING LIVE**")
else:
    st.markdown("### 🔴 Status: **BOT IS IDLE (STOPPED)**")

# 3. Live Account Market Monitoring
st.subheader("📊 Live Account Data (Demo Display)")
metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric("Account Balance", "$10,000.00")
metric_col2.metric("Equity", "$10,000.00")
metric_col3.metric("Free Margin", "$10,000.00")
