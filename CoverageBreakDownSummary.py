import streamlit as st

# Your existing imports and functions here...

def display_coverage_summary():
    st.header("Coverage Summary")
    st.markdown("""
    ### Breakdown of what's covered:

    #### Major Systems
    - **Air Conditioning System:** All components and parts of ducted, central, electric, split and package units are covered.
    - **Heating System:** Coverage includes forced air (gas, electric, oil), geothermal, wall-mounted units, mini-splits, heat pumps, floor furnace, hot water or steam circulating heat, and electric baseboard.
    - **Ductwork:** Ducts from the unit to the point of attachment at registers or grills are covered, unless collapsed or clogged.
    - **Electrical System:** Covered items include electrical panels, light switches, electric outlets, wiring, light fixtures, and wiring from the electrical panel to any covered item.
    - **Plumbing System/Stoppage:** The plan covers leaks, breaks, stoppages, and various plumbing components.

    #### Appliances
    - **Built-in Microwave:** All components and parts are covered.
    - **Clothes Dryer and Washer:** All components and parts for both appliances are included.
    - **Cooktop/Oven/Stove:** All components and parts are covered.
    - **Dishwasher:** All components and parts are included.
    - **Garbage Disposal:** All components and parts are covered.
    - **Refrigerator:** All components and parts, including the integral freezer unit, are covered.
    - **Water Heater:** All components and parts, including tankless water heaters and circulating pumps, are covered.

    #### Other Covered Items
    - **Ceiling and Exhaust Fans:** All components and parts are included.
    - **Garage Door Opener:** All components and parts are covered, except for the door and door track assemblies.
    - **Whirlpool Bathtub:** Built-in bathtub whirlpool motor, pump, and air switch assemblies are covered.

    #### Additional Notes
    - **Drywall:** While not explicitly mentioned in the coverage details, some drywall repairs might be covered if they're necessary to access and repair covered systems.
    - **Service Requests:** You can make unlimited service calls during your contract term.
    - **Service Fee:** You'll need to pay a service fee for each service request, as specified in your coverage details.

    Remember, all covered items must be in proper working condition at the start of the agreement and become inoperative due to normal wear and tear. It's important to review your specific agreement for any limitations, exclusions, or additional terms that may apply to your coverage.
    """)
