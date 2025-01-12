import streamlit as st

def home():
    st.title("Developer Tools Hub")

    # Brief Introduction
    st.write("Welcome to the Developer Tools Hub! Below are the descriptions of the available tools:")

    # Tool Descriptions
    st.subheader("Available Tools")

    st.markdown("""
    - **JSON Formatter**: A tool to format and pretty-print JSON data. It helps you to make your raw JSON readable and properly structured.
    - **XML Formatter**: This tool allows you to format and beautify your XML data for better readability.
    - **YAML Formatter**: A tool to format YAML data. It ensures your YAML files are neatly organized and error-free.
    - **CSV to JSON Converter**: Convert CSV files to JSON format easily with this tool. It automatically handles the transformation with proper mapping.
    - **Text to MD5 Hasher**: This tool hashes your input text into an MD5 hash, commonly used for data integrity verification.
    - **Regex Tester**: A utility to test your regular expressions (regex) with sample inputs. It helps you debug and fine-tune your regex patterns.
    """)

if __name__ == "__main__":
    home()
