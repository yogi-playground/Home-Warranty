import streamlit as st
import re
import question_db as qdb
# List of questions and answers
qa_list1 = [
    {
        "question": "What is the process for determining if an item is repairable or needs replacement?",
        "answer": "The service technician will diagnose the claim and contact CHOICE Home Warranty with the details. The company then determines coverage eligibility and the best course of action - repair, replacement, or possibly a claim buyout."
    },
    {
        "question": "How do you handle repairs for items that are no longer under manufacturer warranty?",
        "answer": "CHOICE Home Warranty covers all systems and appliances that were in proper working condition at the start of the agreement, regardless of age, make, or model."
    },
    {
        "question": "In what situations would I be eligible for a full replacement rather than a repair?",
        "answer": "The document doesn't specify exact situations, but mentions that replacement is one possible outcome after the technician's diagnosis and the company's assessment."
    },
    {
        "question": "How do you determine the age and condition of an item when assessing repair vs. replacement?",
        "answer": "The document doesn't provide specific information on this process."
    },
    {
        "question": "What happens if parts for my covered item are no longer available?",
        "answer": "The document doesn't explicitly address this scenario."
    },
    {
        "question": "Are there any out-of-pocket costs beyond the service fee for repairs or replacements?",
        "answer": "The document mentions a service fee (deductible) but doesn't specify additional out-of-pocket costs."
    },
    {
        "question": "How do you determine the value of a replacement item if mine cannot be repaired?",
        "answer": "The document doesn't provide specific information on this process."
    },
    {
        "question": "If a more expensive model is the only available replacement, who covers the difference in cost?",
        "answer": "The document doesn't address this specific scenario."
    },
    {
        "question": "Are there any coverage limits for high-end or luxury appliances?",
        "answer": "The document doesn't mention specific limits for high-end appliances."
    },
    {
        "question": "Do you offer any options for upgrading to a better model when replacing an item?",
        "answer": "The document doesn't mention upgrade options."
    },
    {
        "question": "What is your typical response time for emergency vs. non-emergency service requests?",
        "answer": "The document states that they begin contacting Service Providers within 4 hours of a service request."
    },
    {
        "question": "How long does it usually take from the initial service request to the completion of a repair?",
        "answer": "The document doesn't provide a specific timeframe for completion of repairs."
    },
    {
        "question": "Are there different SLAs for different types of covered items (e.g., HVAC vs. appliances)?",
        "answer": "The document doesn't mention different SLAs for various items."
    },
    {
        "question": "What factors might cause delays in service, and how are these communicated to customers?",
        "answer": "The document mentions that in some circumstances, it could take more than 48 hours for a Service Provider to accept the request."
    },
    {
        "question": "Do you offer any guarantees on the quality or durability of repairs?",
        "answer": "The document states that if work performed fails within 30 days, they will correct the failure without an additional Service Fee."
    },
    {
        "question": "If a repair takes longer than expected, do you offer any compensation or temporary solutions?",
        "answer": "The document doesn't mention compensation or temporary solutions for extended repair times."
    },
    {
        "question": "What options do I have if I'm not satisfied with the quality of a repair or replacement?",
        "answer": "The document doesn't specifically address options for dissatisfaction with repairs or replacements."
    },
    {
        "question": "In case of a major system failure (e.g., HVAC), do you provide alternative accommodations?",
        "answer": "The document doesn't mention providing alternative accommodations."
    },
    {
        "question": "How do you handle situations where multiple service visits are required to fix an issue?",
        "answer": "The document doesn't address scenarios requiring multiple service visits."
    },
    {
        "question": "Is there a limit to how many times the same item can be repaired before it's replaced?",
        "answer": "The document doesn't specify a limit on repairs before replacement."
    },
    {
        "question": "What happens if damage occurs to my property during a repair?",
        "answer": "The document doesn't address property damage during repairs."
    },
    {
        "question": "How do you handle pre-existing conditions that are discovered during a service call?",
        "answer": "The agreement states that known or unknown pre-existing conditions are not covered."
    },
    {
        "question": "Are there any circumstances where a claim might be denied after a technician has been dispatched?",
        "answer": "The document doesn't specify circumstances for claim denial after dispatch."
    },
    {
        "question": "What is your policy on items that fail shortly after a repair has been completed?",
        "answer": "If work fails within 30 days, they will correct the failure without an additional Service Fee."
    },
    {
        "question": "How do you ensure the security and safety of my home during service visits?",
        "answer": "The document states that all Service Vendors are pre-screened, licensed, and independently insured."
    }
]
def display_qa(qa):
    st.subheader(qa['question'])
    st.markdown(qa['answer'])
    st.write("---")
    
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
    st.title("Home Warranty Q&A")
    
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
        for qa in qdb.question_db():
            display_qa(qa)

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

if __name__ == "__main__":
    main()