import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.title("Portfolio & Risk Management Platform")

# Fetch and display users
st.subheader("Traders")
users_response = requests.get(f"{API_BASE_URL}/users")
if users_response.status_code == 200:
    users = users_response.json().get("users", [])
    selected_user = st.selectbox("Select a trader", [user[1] for user in users])
else:
    st.error("Failed to fetch users")

# Fetch and display portfolios for selected trader
if selected_user:
    st.subheader(f"Portfolios of {selected_user}")
    portfolios_response = requests.get(f"{API_BASE_URL}/portfolios/{selected_user}")
    if portfolios_response.status_code == 200:
        portfolios = portfolios_response.json().get("portfolios", [])
        selected_portfolio = st.selectbox("Select a portfolio", [p[0] for p in portfolios])
    else:
        st.error("Failed to fetch portfolios")

    # Fetch and display holdings for selected portfolio
    if selected_portfolio:
        st.subheader(f"Holdings in {selected_portfolio}")
        holdings_response = requests.get(f"{API_BASE_URL}/holdings/{selected_portfolio}")
        if holdings_response.status_code == 200:
            holdings = holdings_response.json().get("holdings", [])
            st.table(holdings)
        else:
            st.error("Failed to fetch holdings")

# Execute stored procedure button
st.subheader("Execute Stored Procedure")
procedure_name = st.text_input("Enter procedure name")
if st.button("Execute"):
    procedure_response = requests.post(f"{API_BASE_URL}/execute_procedure/{procedure_name}")
    if procedure_response.status_code == 200:
        st.success(procedure_response.json().get("message"))
    else:
        st.error("Failed to execute procedure")
