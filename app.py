import streamlit as st

# Set up page config
st.set_page_config(page_title="Multi-Tab Streamlit App", layout="wide")

# App title
st.title("Streamlit App with Multiple Tabs")

# Define tab names
tabs = ["Home", "Data Upload", "Visualization", "Analysis", "Settings", "Reports", "Help", "About"]

# Create tab navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tabs)

# Define content for each tab
with tab1:
    st.header("Home")
    st.write("Welcome to the app! Navigate using the tabs above.")

with tab2:
    st.header("Data Upload")
    uploaded_file = st.file_uploader("Upload your file here")
    if uploaded_file:
        st.success("File uploaded successfully!")

with tab3:
    st.header("Visualization")
    st.write("Generate charts and graphs based on data.")

with tab4:
    st.header("Analysis")
    st.write("Perform statistical or machine learning analysis.")

with tab5:
    st.header("Settings")
    st.write("Configure app settings and preferences.")

with tab6:
    st.header("Reports")
    st.write("Generate reports and export findings.")

with tab7:
    st.header("Help")
    st.write("Find FAQs, documentation, and support.")

with tab8:
    st.header("About")
    st.write("Learn more about this application and its creators.")