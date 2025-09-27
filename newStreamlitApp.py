import streamlit as st


# Define valid usernames and passwords
VALID_USERS = {
    'admin': 'admin123',
    'user1': 'password1',
    'user2': 'password2',
}


def login():
    """Handles user login logic."""
    st.title("Login Page")

    # Initialize session state variables if they don't exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None

    # Username and password input fields
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    # If the login button is clicked
    if st.button("Login"):
        # Check if the username and password are valid
        if username in VALID_USERS and VALID_USERS[username] == password:
            # Successful login: Set session state variables
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()  # Rerun the script to show content after login
        else:
            st.error("Invalid username or password")


def display_content():
    """Displays content based on the logged-in user."""
    username = st.session_state.username

    # Display different content based on the username
    if username == 'admin':
        st.header("Admin Dashboard")
        st.write("Welcome to the Admin dashboard!")
        # You can add admin-specific functionalities here
    elif username == 'user1':
        st.header("User1's Page")
        st.write("Hello User1! Here is your content.")
        # Add user1-specific functionalities here
    elif username == 'user2':
        st.header("User2's Page")
        st.write("Hello User2! Here is your content.")
        # Add user2-specific functionalities here
    else:
        st.write("Welcome, please log in to see the content.")


def logout():
    """Handles user logout logic."""
    if st.session_state.get("logged_in", False):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()  # Rerun the script to show the login form after logout


def main():
    # If the user is not logged in, show the login form
    if not st.session_state.get('logged_in', False):
        login()
    else:
        # If the user is logged in, show personalized content
        display_content()
        logout_button = st.button("Logout")
        if logout_button:
            logout()


if __name__ == "__main__":

    main()


