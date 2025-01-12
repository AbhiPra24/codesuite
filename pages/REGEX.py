import streamlit as st
import re

# Set up the page title
st.set_page_config(page_title="Regex Tester", page_icon="🔍")

# Title of the tool
st.title("Regex Tester 🛠️")

# Description of the tool
st.markdown("""
Enter a regular expression pattern and a sample text. The tool will show you matches from the sample text.
""")

# Input section (Left side)
regex_pattern = st.text_input("Enter Regex Pattern")
sample_text = st.text_area("Enter Sample Text", height=300)

# Button to test the regex
if st.button("Test Regex"):
    if regex_pattern:
        try:
            matches = re.findall(regex_pattern, sample_text)
            if matches:
                st.subheader("Matches Found")
                st.write(matches)
            else:
                st.write("No matches found.")
        except re.error as e:
            st.error(f"Invalid Regex pattern! Error: {e}")
    else:
        st.warning("Please enter a regex pattern to test.")
