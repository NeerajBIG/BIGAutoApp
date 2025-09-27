import streamlit as st

# Define valid usernames and passwords
VALID_USERS = {
    'admin': 'admin123',  # Admin username and password
    'user': 'user123'     # Regular user username and password
}

def login():
    """Handles user login logic."""
    st.title("Login Page")

    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # If the login button is clicked
    if st.button("Login"):
        # Check if the username and password are valid
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.experimental_rerun()  # Rerun to show personalized page after login
        else:
            st.error("Invalid username or password")

def display_content():
    """Displays content based on the logged-in user."""
    username = st.session_state.username

    # Display different content based on the username
    if username == 'admin':
        st.header("Admin Dashboard")
        st.write("Welcome, Admin!")
        # Admin specific functionalities can go here
        st.write("You have full access to all features.")
    elif username == 'user':
        st.header("User Dashboard")
        st.write("Welcome, User!")
        # Regular user specific functionalities can go here
        st.write("You have limited access.")
    else:
        st.write("Welcome! Please log in to access your dashboard.")

def logout():
    """Handles user logout logic."""
    if st.session_state.get("logged_in", False):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.experimental_rerun()  # Rerun to show the login page after logout

def main():
    # Initialize session state variables if they don't exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None

    # If the user is not logged in, show the login form
    if not st.session_state.logged_in:
        login()
    else:
        # If the user is logged in, show personalized content
        display_content()
        logout_button = st.button("Logout")
        if logout_button:
            logout()

if __name__ == "__main__":
    main()
