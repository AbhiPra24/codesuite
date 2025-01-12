import streamlit as st
import base64

# Set up the page title
st.set_page_config(page_title="Base64 Converter", page_icon="🔐")

# Title of the tool
st.title("Base64 Converter 🛠️")

# Description of the tool
st.markdown("""
Enter text to encode it to Base64, or enter a Base64 string to decode it.
""")

# Input section for encoding (left side)
encode_text = st.text_area("Enter Text to Encode", height=150)

# Input section for decoding (left side)
decode_text = st.text_area("Enter Base64 String to Decode", height=150)

# Button to encode text to Base64
if st.button("Encode to Base64"):
    if encode_text:
        encoded = base64.b64encode(encode_text.encode('utf-8')).decode('utf-8')
        st.subheader("Encoded Base64")
        st.code(encoded)
    else:
        st.warning("Please enter text to encode.")

# Button to decode Base64
if st.button("Decode Base64"):
    if decode_text:
        try:
            decoded = base64.b64decode(decode_text).decode('utf-8')
            st.subheader("Decoded Text")
            st.write(decoded)
        except Exception as e:
            st.error(f"Invalid Base64 string! Error: {e}")
    else:
        st.warning("Please enter a Base64 string to decode.")
