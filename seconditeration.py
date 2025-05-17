import streamlit as st

st.set_page_config(page_title="Greenhouse Project Input", page_icon="🌱", layout="wide")

st.title("🌱 Greenhouse Project Input Form")

with st.form("project_form"):
    st.markdown("### 📋 Please fill in the details for each category below and submit at the end.")

    # Site & Soil
    with st.expander("🏞️ Site & Soil"):
        col1, col2, col3 = st.columns(3)
        area = col1.number_input("Area (sq.m)", min_value=0.0)
        slope = col2.text_input("Slope (e.g., gentle, steep)")
        drainage = col3.selectbox("Drainage", ["Good", "Moderate", "Poor"])
        pH = col1.number_input("Soil pH", min_value=0.0, max_value=14.0)
        EC = col2.number_input("Soil EC (dS/m)", min_value=0.0)
        accessibility = col3.selectbox("Accessibility", ["Easy", "Moderate", "Difficult"])
        utilities = col1.multiselect("Utilities Available", ["Water", "Electricity", "Road", "Internet"])

    # Climate
    with st.expander("🌦️ Climate"):
        wind_speed = st.slider("Wind Speed (km/h)", 0, 100, 10)
        sunlight = st.slider("Sunlight (hours/day)", 0, 24, 8)
        temperature = st.slider("Temperature (°C)", -10, 50, 25)
        humidity = st.slider("Humidity (%)", 0, 100, 60)
        rainfall = st.number_input("Rainfall (mm/year)", min_value=0.0)

    # Design & Layout
    with st.expander("📐 Design & Layout"):
        dtype = st.selectbox("Type", ["Gothic", "Quonset", "Sawtooth", "Other"])
        size = st.text_input("Size (L x W x H in meters)")
        orientation = st.selectbox("Orientation", ["East-West", "North-South"])
        bay_width = st.number_input("Bay Width (meters)", min_value=0.0)
        internal_layout = st.text_area("Internal Layout Description")

    # Structure
    with st.expander("🏗️ Structure"):
        foundation = st.selectbox("Foundation Type", ["Concrete", "Steel", "Wood", "Other"])
        columns = st.text_input("Columns (Material/Spec)")
        trusses = st.text_input("Trusses (Material/Spec)")
        purlins = st.text_input("Purlins (Material/Spec)")
        bracing = st.text_input("Bracing (Type/Spec)")
        gutters = st.text_input("Gutters (Type/Spec)")
        fasteners = st.text_input("Fasteners (Type/Spec)")

    # Cladding
    with st.expander("🪟 Cladding"):
        cladding = st.multiselect("Cladding Materials", ["Polyfilm", "Nets", "Shade Net", "Polycarbonate", "Glass"])

    # Ventilation
    with st.expander("🌬️ Ventilation"):
        ridge_vents = st.checkbox("Ridge Vents")
        side_vents = st.checkbox("Side Vents")
        rollup_sides = st.checkbox("Roll-up Sides")
        doors = st.text_input("Doors (Type/Spec)")
        netting = st.checkbox("Netting")

    # Environmental Control
    with st.expander("🌡️ Environmental Control"):
        fans = st.checkbox("Fans")
        pads = st.checkbox("Pads")
        heaters = st.checkbox("Heaters")
        foggers = st.checkbox("Foggers")
        sensors = st.checkbox("Sensors")
        automation = st.checkbox("Automation")

    # Irrigation & Fertigation
    with st.expander("💧 Irrigation & Fertigation"):
        water_source = st.text_input("Water Source")
        drip_system = st.checkbox("Drip System")
        fert_unit = st.checkbox("Fertigation Unit")
        pumps = st.checkbox("Pumps")
        filters = st.checkbox("Filters")

    # Crop Planning
    with st.expander("🌱 Crop Planning"):
        crop_type = st.text_input("Crop Type(s)")
        crop_layout = st.text_area("Crop Layout")
        crop_height = st.number_input("Crop Height (cm)", min_value=0.0)
        rotation = st.text_input("Crop Rotation Plan")

    # Operations & Safety
    with st.expander("🛡️ Operations & Safety"):
        pathways = st.text_input("Pathways (Spec/Material)")
        lighting = st.checkbox("Lighting")
        emergency_exits = st.checkbox("Emergency Exits")
        fire_safety = st.checkbox("Fire Safety")
        security = st.checkbox("Security Measures")

    # Regulatory
    with st.expander("📑 Regulatory"):
        standards = st.text_area("Applicable Standards")
        certificates = st.text_area("Required Certificates")
        permits = st.text_area("Permits Needed")
        training = st.text_area("Training Requirements")

    submitted = st.form_submit_button("Submit All Details")

if submitted:
    st.success("✅ All details submitted! You can now process or display the results as needed.")
    # Here you can add code to process, display, or save the collected data.
