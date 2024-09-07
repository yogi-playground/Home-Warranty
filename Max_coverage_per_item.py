import streamlit as st

# Your existing imports and functions here...

def display_max_coverage():
    st.header("Maximum Coverage per Item")
    
    st.markdown("""
    Based on the CHOICE Home Warranty document, here are the maximum coverage amounts for specific items:

    | Item | Maximum Coverage |
    |------|------------------|
    | General Coverage Limit | Up to $3,000 per covered item per year |
    | Well Pump | Up to $500 for access, diagnosis, and repair/replacement |
    | Limited Roof Leak (Single Family Homes Only) | Up to $500 for access, diagnosis, and repair/replacement |
    | Septic Tank Pumping | Up to $250 per Agreement term |
    | Septic System | Up to $500 for access, diagnosis, and repair/replacement |
    | Sprinkler System | Up to $500 for access, diagnosis, and repair/replacement |

    **Note:** For many other covered items, specific dollar limits are not mentioned. Instead, the document lists which components are covered or excluded. Always refer to the full agreement for detailed coverage information and any additional terms or conditions that may apply.
    """)