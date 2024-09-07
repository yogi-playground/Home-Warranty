import streamlit as st
import re
import question_db as qdb
from google_analytics import add_google_analytics
from CoverageBreakDownSummary import display_coverage_summary
from Cost_Estimator import display_cost_estimator
from Max_coverage_per_item import display_max_coverage
# List of questions and answers
def display_qa(qa):
    st.subheader(qa['question'])
    st.markdown(qa['answer'])
    st.write("---")
    
def display_qa_collapsible(qa_list):
    for qa in qa_list:
        with st.expander(f"**{qa['question']}**", expanded=False):  # Make the question bold
            st.write(qa['answer'])
            
def search_qa(query):
    results = []
    for qa in qdb.question_db():
        if re.search(query, qa['question'], re.IGNORECASE) or re.search(query, qa['answer'], re.IGNORECASE):
            results.append(qa)
    return results
def sidebar_summary():
    st.sidebar.header("Coverage Cost Summary")
    
    st.sidebar.subheader("Service Fee")
    st.sidebar.write("$100 per service call")
    
    st.sidebar.subheader("Total Max Coverage")
    st.sidebar.write("$3,000 per year")
    
    st.sidebar.subheader("Example: If a repair costs $600:")
    st.sidebar.write("""    
    1. You pay: $100 (service fee)
    2. CHW covers: $500 (repair cost)
    3. Total used: $500
    4. Remaining coverage: $2,500
    """)
    
    st.sidebar.write("Note: The service fee is always paid, but doesn't count towards your coverage limit.")
    
def main():
    tracking_id = st.secrets["google_credentials"]["tracking_id"]
    add_google_analytics(tracking_id)  # Add this at the beginning of your main function    
    st.title("Home Warranty Q&A")
    #st.write(tracking_id)
        
     # Create buttons for navigation in a row at the top
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("View All Question"):
            st.session_state.page = "View All Q&A"
    with col2:
        if st.button("Search Information"):
            st.session_state.page = "Search Q&A"
    with col3:
        if st.button("Your Cost Estimator"):
            st.session_state.page = "Cost Estimator"
    with col4:
        if st.button("Coverage Summary"):
            st.session_state.page = "Coverage Summary"
    with col5:
        if st.button("Max Coverage / Item"):
            st.session_state.page = "Max Coverage" 
     
     # Use session state to keep track of the current page
    if 'page' not in st.session_state:
        st.session_state.page = "View All Q&A"
    
    # Display content based on the selected page
    if st.session_state.page == "View All Q&A":
        st.header("All Questions and Answers")
        display_qa_collapsible(qdb.question_db())

    elif st.session_state.page == "Search Q&A":
        st.header("Search Questions and Answers")
        search_query = st.text_input("Enter your search query:")
        if search_query:
            results = search_qa(search_query)
            if results:
                display_qa_collapsible(results)
            else:
                st.write("No results found.")

    elif st.session_state.page == "Cost Estimator":
        display_cost_estimator()
    elif st.session_state.page == "Coverage Summary":
       display_coverage_summary()
    elif st.session_state.page == "Max Coverage":
        display_max_coverage()


    # Sidebar summary section
    sidebar_summary()
    
    # Disclaimer footer
    st.markdown("---")
    st.write("Disclaimer: This app is for educational purposes only and may contain inaccuracies; always verify information with the your warranty provider.")

if __name__ == "__main__":
    main()