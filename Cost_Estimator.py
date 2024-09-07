
import streamlit as st

def display_cost_estimator():
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