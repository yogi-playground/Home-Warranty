import streamlit as st
import re

# List of questions and answers
qa_list = [
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

def search_qa(query):
    results = []
    for qa in qa_list:
        if re.search(query, qa['question'], re.IGNORECASE) or re.search(query, qa['answer'], re.IGNORECASE):
            results.append(qa)
    return results

def main():
    st.title("CHOICE Home Warranty Q&A")

    # Sidebar for navigation
    page = st.sidebar.radio("Navigate", ["View All Q&A", "Search Q&A", "Cost Estimator"])

    if page == "View All Q&A":
        st.header("All Questions and Answers")
        for qa in qa_list:
            st.subheader(qa['question'])
            st.write(qa['answer'])
            st.write("---")

    elif page == "Search Q&A":
        st.header("Search Questions and Answers")
        search_query = st.text_input("Enter your search query:")
        if search_query:
            results = search_qa(search_query)
            if results:
                for qa in results:
                    st.subheader(qa['question'])
                    st.write(qa['answer'])
                    st.write("---")
            else:
                st.write("No results found.")

    elif page == "Cost Estimator":
        st.header("Cost Estimator")
        st.write("Estimate your potential costs based on the information provided:")

        service_fee = st.number_input("Service Fee", min_value=0, value=100)
        repair_cost = st.number_input("Estimated Repair Cost", min_value=0, max_value=2000, value=0)
        replacement_cost = st.number_input("Estimated Replacement Cost", min_value=0, max_value=3000, value=0)

        total_cost = service_fee
        if repair_cost > 0:
            total_cost += min(repair_cost, 2000)
        elif replacement_cost > 0:
            total_cost += min(replacement_cost, 3000)

        st.write(f"Estimated Total Cost: ${total_cost}")
        st.write("Note: This is a rough estimate based on the information provided in the document. Actual costs may vary.")

if __name__ == "__main__":
    main()