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
            },
                {
        "question": "When does coverage begin and when does it end?",
        "answer": "Coverage begins 30 days after enrollment and receipt of applicable contract fees and continues for 365 days from your start date. If you can provide proof of prior coverage through another warranty carrier, showing no lapse of warranty coverage, CHW may start your new coverage when your old policy expires."
    },
    {
        "question": "How many service calls can I make?",
        "answer": "You can make as many service calls as you need. There is no limit to the number of times you can call for covered repairs during your contract term."
    },
    {
        "question": "Does a home warranty cover older systems and appliances?",
        "answer": "Yes, a home warranty provides repair or replacement of all covered systems and appliances that were in the home and in proper operating condition on the agreement effective date, and that have been properly installed and maintained, regardless of their age, make, or model."
    },
    {
        "question": "How do I know my service technician is qualified?",
        "answer": "All CHW Service Vendors are pre-screened, licensed, and independently insured. Performance is constantly monitored to ensure quality work and professionalism. Your satisfaction is their biggest priority."
    },
    {
        "question": "Can I renew each year?",
        "answer": "Yes, the plan may be renewable. In that event, you will be notified of the prevailing rate and terms of renewal."
    },
    {
        "question": "Why should I renew my CHW Warranty if I haven't made any service calls?",
        "answer": "Your home systems or appliances can break down at any time - usually when you need them most. That's why it's important to continue the protection and peace of mind you get from your Choice Home Warranty."
    },
    {
        "question": "What is the process for making a service request?",
        "answer": "When a covered system or appliance breaks down, simply contact the Claims Department at (888) 531-5403 or file your claim online at www.ChoiceHomeWarranty.com."
    },
    {
        "question": "How is a service appointment scheduled?",
        "answer": "Once you submit your claim, you will be assigned a pre-screened, licensed, and insured service technician to handle your request. CHW will provide you with their contact information so you can schedule a mutually convenient appointment."
    },
    {
        "question": "How does the service fee work?",
        "answer": "The service technician will collect the deductible from you upon arrival. If your service request covers more than one item, or if more than one trade is needed to complete your repair (e.g. electrician and plumber), multiple deductibles may apply."
    },
    {
        "question": "What happens after the service technician diagnoses the issue?",
        "answer": "The service technician will diagnose the claim and contact CHW with the details. CHW will then determine coverage eligibility and the best course of action - repair, replacement, or possibly a claim buyout."
    },
    {
        "question": "Is there a feedback process after the service is completed?",
        "answer": "Yes, after your service has been completed, you will receive a survey asking for feedback about your experience. Your feedback allows CHW to improve their business and promote the quality of their service to potential customers."
    },
    {
        "question": "What is the average life expectancy of critical appliances/home systems?",
        "answer": "According to Home Repair and Remodel, Marshall & Swift L.P. (2004), the average life expectancy of nine critical appliances/home systems is 13 years, and the likelihood of failure of one of these systems in a given year is 68%."
    },
    {
        "question": "How does a home warranty affect home sales?",
        "answer": "According to the National Home Warranty Association, homes on the market with a home warranty included sell on average 50% faster than homes without. Business Week Magazine reports that homes with home warranties return a sales price that averages 3% higher."
    },
    {
        "question": "Do buyers prefer homes with warranties?",
        "answer": "According to a Gallup Poll, 8 out of 10 buyers prefer to buy a home with a home warranty."
    },
    {
        "question": "What is the average cost range for home system or appliance repairs?",
        "answer": "According to Home Repair and Remodel, Marshall & Swift L.P. (2004), a home system or appliance repair can range from $65 to $2,000, and replacement averages $1,085."
    },
    {
        "question": "What is the square footage limit for covered homes?",
        "answer": "This Agreement covers occupied homes under 5,000 square feet, unless an appropriate fee is paid."
    },
    {
        "question": "Are pre-existing conditions covered?",
        "answer": "No, known or unknown pre-existing conditions are not covered."
    },
    {
        "question": "How quickly does CHW begin contacting Service Providers after a service request?",
        "answer": "Upon request for service, CHW will begin contacting Service Provider(s) within 4 hours."
    },
    {
        "question": "Does CHW reimburse for services performed without prior approval?",
        "answer": "No, CHW will not reimburse for services performed without prior approval."
    },
    {
        "question": "What happens if work performed under the Agreement fails within 30 days?",
        "answer": "If work performed under this Agreement should fail within 30 days, CHW will correct the failure without a Service Fee."
    },
    {
        "question": "Who selects the Service Provider?",
        "answer": "CHW has the sole right to select the Service Provider."
    },
    {
        "question": "What is excluded from the refrigerator coverage?",
        "answer": "Audio/Visual equipment and internet connection components are excluded from refrigerator coverage."
    },
    {
        "question": "What is the coverage limit for well pump repairs?",
        "answer": "CHW will pay up to $500 for access, diagnosis and repair and/or replacement of well pump components."
    },
    {
        "question": "What is the coverage limit for septic tank pumping?",
        "answer": "CHW will pay up to $250 per Agreement term for access, diagnosis and repair and/or replacement related to septic tank pumping."
    },
    {
        "question": "What is the coverage limit for sprinkler system repairs?",
        "answer": "CHW will pay up to $500 for access, diagnosis and repair and/or replacement of sprinkler system components."
    }
          
        ]
    return qa_list