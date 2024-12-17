import streamlit as st

# Dictionary of patient operation budgets by country
operation_budgets = {
    "USA": {
        "heart surgery": 60000,
        "knee replacement": 35000,
        "appendix removal": 15000,
        "cancer treatment": 90000,
        "eye surgery": 20000,
        "dental surgery": 10000,
        "organ transplant": 130000,
        "childbirth (normal delivery)": 7000,
        "childbirth (c-section)": 15000,
        "emergency care": 25000,
    },
    "UK": {
        "heart surgery": 40000,
        "knee replacement": 20000,
        "appendix removal": 10000,
        "cancer treatment": 70000,
        "eye surgery": 12000,
        "dental surgery": 5000,
        "organ transplant": 90000,
        "childbirth (normal delivery)": 5000,
        "childbirth (c-section)": 10000,
        "emergency care": 15000,
    },
    "Pakistan": {
        "heart surgery": 8000,
        "knee replacement": 6000,
        "appendix removal": 3000,
        "cancer treatment": 12000,
        "eye surgery": 2500,
        "dental surgery": 1500,
        "organ transplant": 25000,
        "childbirth (normal delivery)": 1000,
        "childbirth (c-section)": 2500,
        "emergency care": 2000,
    },
}

# Function to query operation budgets
def query_operation_budget(country, user_input):
    user_input = user_input.lower()
    for operation, budget in operation_budgets[country].items():
        if operation in user_input:
            return f"The budget for **{operation}** in **{country}** is **${budget:,}**."
    return "Sorry, I couldn't find that operation. Please ask about a specific procedure or operation."

# Streamlit UI
st.title("🏥 Patient Operations Budget Chatbot")
st.write("Ask me about the budgets for various patient operations and procedures!")

# Country selection dropdown
country = st.selectbox("Select your country:", ["USA", "UK", "Pakistan"])

# User query input
user_query = st.text_input(f"What operation budget would you like to know for {country}?", "")

# Button to respond
if st.button("Submit"):
    if user_query:
        response = query_operation_budget(country, user_query)
        st.success(response)
    else:
        st.warning("Please enter a query to get a response!")
