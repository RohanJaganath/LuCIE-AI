import streamlit as st
from chatbot import chatapp as app1
from yolo import detectapp as app2

# Initialize a session state variable to track the current app
if 'current_app' not in st.session_state:
    st.session_state.current_app = 'App 1'

# Function to change the current app
def change_app(app_name):
    st.session_state.current_app = app_name

# Setting up the sidebar navigation with links
st.sidebar.title("Navigation")
st.sidebar.markdown("Select an app:")
st.sidebar.button("CT Analyzer", on_click=change_app, args=('App 1',))
st.sidebar.button("Assistant", on_click=change_app, args=('App 2',))

# Display the selected app based on session state
if st.session_state.current_app == 'App 1':
    app2()
elif st.session_state.current_app == 'App 2':
    app1()
