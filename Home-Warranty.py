import streamlit as st
import re
import question_db as qdb
from google_analytics import add_google_analytics
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
    st.sidebar.header("Coverage Summary")
    
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
    # Sidebar for navigation
     # Sidebar for navigation
    st.sidebar.header("Navigate")
    
     
     # Use session state to keep track of the current page
    if 'page' not in st.session_state:
        st.session_state.page = "View All Q&A"
    
    # Create buttons for navigation
    if st.sidebar.button("View All Q&A"):
        st.session_state.page = "View All Q&A"
    if st.sidebar.button("Search Q&A"):
        st.session_state.page = "Search Q&A"
    if st.sidebar.button("Cost Estimator"):
        st.session_state.page = "Cost Estimator"

    # Sidebar summary section
    sidebar_summary()
    
    if st.session_state.page == "View All Q&A":
        st.header("All Questions and Answers")
        display_qa_collapsible(qdb.question_db())

    elif st.session_state.page == "Search Q&A":
        st.header("Search Questions and Answers")
        search_query = st.text_input("Enter your search query:")
        if search_query:
            results = search_qa(search_query)
            if results:
                for qa in results:
                    display_qa(qa)
            else:
                st.write("No results found.")

    elif  st.session_state.page == "Cost Estimator":
        st.header("Cost Estimator")
        st.write("Estimate your potential costs based on the information provided:")
        service_fee = st.number_input("Service Fee", min_value=100, value=100)
        repair_cost = st.slider("Estimated Repair Cost:", min_value=1, max_value=3000, value=0, step=25)
        replacement_cost = st.slider("Estimated Replacement Cost:", min_value=1, max_value=10000, value=0, step=50)
        previously_used = st.number_input("Previously Used Amount (if any but service not incldued)", min_value=0, max_value=3000, value=00, step=50)
        total_coverage_limit = 3000
        remaining_coverage = total_coverage_limit - previously_used
        current_repair_cost=0
        current_replacement_cost=0
        current_cost = 0
        if repair_cost > 0:
            current_repair_cost = min(repair_cost, remaining_coverage)
        elif replacement_cost > 0:
            current_replacement_cost = min(replacement_cost, remaining_coverage)
        else:
            current_cost = 0

        total_cost =  current_repair_cost +current_replacement_cost
        
        new_total_used = previously_used + total_cost-service_fee
        new_remaining_coverage = total_coverage_limit - new_total_used

        st.write(f"Estimated Total Cost for This Service: ${total_cost}")
        st.write(f"Amount you need to inclduing Service Fee: ${service_fee}")
        st.write(f"Estimated Total Cost covered: ${total_cost-service_fee}")
        
        st.write(f"Total Amount Used (Including This Service): ${new_total_used}")
        st.write(f"Remaining Coverage: ${new_remaining_coverage}")

        st.write("""
        **Note:** 
        - The total coverage limit is $3000 per year.
        - You always pay the service fee for each service call.
        - The warranty covers repair or replacement costs up to the remaining coverage limit.
        - This is a rough estimate based on the information provided. Actual costs may vary.
        """)

        if new_total_used > total_coverage_limit:
            st.warning(f"Warning: You have exceeded the annual coverage limit by ${new_total_used - total_coverage_limit}. This amount will be your responsibility.")
    # Disclaimer footer
    st.markdown("---")
    st.write("Disclaimer: This app is for educational purposes only and may contain inaccuracies; always verify information with the your warranty provider.")

if __name__ == "__main__":
    main()