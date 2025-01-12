import streamlit as st
import json

# Set up the page title
st.set_page_config(page_title="JSON Formatter", page_icon="📄")

# Title of the tool
st.title("JSON Formatter 🛠️")

# Description of the tool
st.markdown("""
Paste your raw JSON into the left box, then click **Format JSON** to see it beautified in the right box.
""")

# Input section (Left side)
raw_json = st.text_area("Enter Raw JSON", height=300)

# Button to format the JSON
if st.button("Format JSON"):
    # Try to parse and pretty print the JSON
    try:
        formatted_json = json.dumps(json.loads(raw_json), indent=4)
        st.subheader("Formatted JSON")
        st.code(formatted_json, language="json")
    except ValueError as e:
        st.error("Invalid JSON! Please check your input.")
