def question_db():
    qa_list = [
        {
                "question": "What is the process for determining if an item is repairable or needs replacement?",
                "answer": """
        The process involves several steps:
        1. Diagnosis: A service technician will diagnose the claim.
        2. Reporting: The technician contacts CHOICE Home Warranty with the details.
        3. Assessment: The company determines coverage eligibility.
        4. Decision: CHOICE Home Warranty decides on the best course of action:
        - Repair
        - Replacement
        - Possibly a claim buyout
                """
            },
            {
                "question": "How do you handle repairs for items that are no longer under manufacturer warranty?",
                "answer": """
        CHOICE Home Warranty covers all systems and appliances that:
        1. Were in proper working condition at the start of the agreement
        2. Are covered regardless of:
        - Age
        - Make
        - Model

        Note: The coverage is subject to the terms and conditions of the agreement.
                """
            },
            {
                "question": "What happens if parts for my covered item are no longer available?",
                "answer": """
        The document doesn't explicitly address this scenario. However, based on general practices:

        1. Assessment: The technician would likely report this to CHOICE Home Warranty.
        2. Options: The company might consider:
        - Sourcing parts from alternative suppliers
        - Offering a replacement if repair is not possible
        - Providing a claim buyout

        It's best to contact CHOICE Home Warranty directly for specific information on such cases.
                """
            },
            {
                "question": "Are there any out-of-pocket costs beyond the service fee for repairs or replacements?",
                "answer": """
        The document mentions the following:

        1. Service Fee: You pay a service fee (deductible) for each service request.
        2. Coverage Limits: There are coverage limits, generally up to $3,000 per covered item per year.
        3. Additional Costs: The document doesn't specify additional out-of-pocket costs.

        However, you might incur additional costs if:
        - The repair or replacement exceeds the coverage limit
        - The issue involves non-covered components or is due to excluded causes

        Always refer to your specific agreement for detailed information on potential additional costs.
                """
            },
            {
                "question": "How much will it cost me if something stops working?",
                "answer": """
        The cost breakdown for a covered item that stops working is as follows:

        1. Service Fee: $100 
        - Paid when the technician arrives to assess the issue
        - Applicable for each service request

        2. Repair Costs: 
        - Typically range from $65 to $2,000
        - Covered by CHOICE Home Warranty up to the coverage limits

        3. Replacement Costs:
        - Average replacement cost is around $1,085
        - Covered up to $3,000 per item per year

        4. Your Financial Responsibility:
        - Service Fee: $100
        - Any costs exceeding the coverage limits
        - Any costs for non-covered items or excluded issues

        Note: Always refer to your specific agreement for exact coverage details and limits.
                """
            },
            {
                "question": "Who will manage repair costs if it's under $2000?",
                "answer": """
        For repair costs under $2,000 on covered items:

        1. Your Responsibility:
        - Pay the $100 service fee when the technician arrives

        2. CHOICE Home Warranty's Responsibility:
        - Manage and cover the remaining repair costs
        - Arrange for a qualified Service Provider to perform the repair

        3. Coverage Conditions:
        - The item must be covered under your plan
        - The repair must fall within the terms and conditions of your agreement
        - The total cost must be within the coverage limits (generally up to $3,000 per item per year)

        4. Process:
        - The technician diagnoses the issue
        - CHOICE Home Warranty approves the repair
        - The repair is completed at the company's expense, minus your service fee

        Always refer to your specific agreement for exact coverage details and limits.
                """
            },
            {
                "question": "In a scenario where an item was initially repaired at a cost of $1200, for which I paid only a $100 service fee, but the item fails again after just 2 weeks and is now deemed irreparable, with a replacement product costing $2900, what would be my financial responsibility?",
                "answer": """
        In this scenario, here's how it would likely be handled:

        1. Initial Repair:
        - You paid: $100 service fee
        - CHOICE Home Warranty covered: $1200 repair cost

        2. Failure after 2 weeks:
        - No additional service fee required (failure within 30 days)

        3. Replacement Cost:
        - Total cost: $2900
        - Covered by CHOICE Home Warranty: Full $2900 (assuming it's within the $3,000 per item per year limit)

        4. Your Financial Responsibility:
        - No additional out-of-pocket costs beyond the initial $100 service fee

        5. Important Notes:
        - The document doesn't address how prior repair costs factor into replacement coverage limits
        - There's no mention of depreciation or pro-rating applied to replacements
        - This assumes the replacement is within your agreement's coverage limits

        Always confirm these details directly with CHOICE Home Warranty, as specific terms can vary between individual agreements.
                """
            }
        ]
    return qa_list