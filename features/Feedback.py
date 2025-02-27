import streamlit as st

st.header("Feedback", divider='rainbow')

with st.form("feedback_form"):
    name = st.text_input("Full Name*", value=None, placeholder="John Doe")
    email = st.text_input("Email*", value=None, placeholder="johndoe@gmail.com")
    rating = st.slider("Rating*", min_value=1, max_value=5, value=3)
    easy_to_use = st.selectbox("Easy to Use*", options=["Yes", "No", "Somewhat"], help="Select if the application is easy to use")
    challenges = st.text_area("Challenges Faced*", help="Enter the challenges faced by you", value=None, placeholder=None)
    general_feedback = st.text_area("Any other feedback", help="Enter any other feedback", value=None)
    st.markdown("**Required*")
    submit = st.form_submit_button("Submit")

if submit:
    if not name or not email or not rating or not easy_to_use or not challenges:
        st.error("Please fill all the required fields.")
        st.stop()
    else:
        st.success("Thank you for your feedback!") 