import streamlit as st
import datetime

# Function to display the Home page
def show_home_page():
    st.title("Welcome to the Fitness App!")
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    st.subheader(f"Today's date is {current_date}")
    st.write("Hello Huzz!")

# Display the Add Workout page
def show_add_workout_page():
    st.title("Add a New Workout")
    st.write("Hello Huzz!")

# Display the Edit Workout page
def show_edit_workout_page():
    st.title("Edit a Workout")
    st.write("Hello Huzz!")

# Display the View Workouts page
def show_view_workouts_page():
    st.title("View Workouts")
    st.write("Hello Huzz!")

# Main function to manage page content based on sidebar selection
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Home", "Add Workout", "Edit Workout", "View Workouts"])

    # Show content based on selected page
    if page == "Home":
        show_home_page()
    elif page == "Add Workout":
        show_add_workout_page()
    elif page == "Edit Workout":
        show_edit_workout_page()
    elif page == "View Workouts":
        show_view_workouts_page()

# Run the app
if __name__ == "__main__":
    main()
