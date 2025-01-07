import streamlit as st

# Predefined username and password
USER_CREDENTIALS = {
    "user1": "password123",
    "admin": "adminpass",
}

# Set the page title
st.set_page_config(page_title="Login Example")

# Define a function to show the login page
def show_login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            # Store login status in session state
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()  # Refresh to show the main page
        else:
            st.error("Invalid username or password.")

# Define a function to show the main page
def show_main_page():
    if "logged_in" in st.session_state and st.session_state.logged_in:
        username = st.session_state.username
        st.title(f"Welcome back, {username}!")
        st.write("This is your main page content available after login.")
        st.button("Perform some action")

    else:
        st.error("You are not logged in. Please log in first.")
        if st.button("Go to Login Page"):
            st.session_state.page = "Login"
            st.experimental_rerun()

# Main logic to handle navigation based on login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    # If not logged in, show the login page
    show_login_page()
else:
    # If logged in, show the main page
    show_main_page()
