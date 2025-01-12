import streamlit as st
import xml.dom.minidom

# Set up the page title
st.set_page_config(page_title="XML Formatter", page_icon="📄")

# Title of the tool
st.title("XML Formatter 🛠️")

# Description of the tool
st.markdown("""
Paste your raw XML into the left box, then click **Format XML** to see it beautified in the right box.
""")

# Input section (Left side)
raw_xml = st.text_area("Enter Raw XML", height=300)

# Button to format the XML
if st.button("Format XML"):
    # Try to parse and pretty print the XML
    try:
        dom = xml.dom.minidom.parseString(raw_xml)
        formatted_xml = dom.toprettyxml(indent="  ")
        st.subheader("Formatted XML")
        st.code(formatted_xml, language="xml")
    except Exception as e:
        st.error("Invalid XML! Please check your input.")
