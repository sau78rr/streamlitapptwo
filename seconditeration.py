import streamlit as st

st.set_page_config(page_title="Greenhouse Project Input", page_icon="🌱", layout="wide")
st.title("🌱 Greenhouse Project Input Form")

with st.form("project_form"):
    st.markdown("### 📋 Please fill in the details for each category below and submit at the end.")

    # Site & Soil
    with st.expander("🏞️ Site & Soil"):
        st.markdown("#### Site Characteristics")
        c1, c2, c3 = st.columns([1, 1, 1])
        area = c1.number_input("Area (sq.m)", min_value=0.0)
        slope = c2.text_input("Slope (e.g., gentle, steep)")
        drainage = c3.selectbox("Drainage", ["Good", "Moderate", "Poor"])

        c4, c5, c6 = st.columns([1, 1, 1])
        pH = c4.number_input("Soil pH", min_value=0.0, max_value=14.0)
        EC = c5.number_input("Soil EC (dS/m)", min_value=0.0)
        accessibility = c6.selectbox("Accessibility", ["Easy", "Moderate", "Difficult"])

        utilities = st.multiselect("Utilities Available", ["Water", "Electricity", "Road", "Internet"])

    # Climate
    with st.expander("🌦️ Climate"):
        st.markdown("#### Climate Parameters")
        c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
        wind_speed = c1.slider("Wind Speed (km/h)", 0, 100, 10)
        sunlight = c2.slider("Sunlight (hours/day)", 0, 24, 8)
        temperature = c3.slider("Temperature (°C)", -10, 50, 25)
        humidity = c4.slider("Humidity (%)", 0, 100, 60)
        rainfall = c5.number_input("Rainfall (mm/year)", min_value=0.0)

    # Design & Layout
    with st.expander("📐 Design & Layout"):
        st.markdown("#### Greenhouse Design")
        c1, c2 = st.columns([1, 2])
        dtype = c1.selectbox("Type", ["Gothic", "Quonset", "Sawtooth", "Other"])
        size = c2.text_input("Size (L x W x H in meters)")

        c3, c4 = st.columns([1, 1])
        orientation = c3.selectbox("Orientation", ["East-West", "North-South"])
        bay_width = c4.number_input("Bay Width (meters)", min_value=0.0)

        internal_layout = st.text_area("Internal Layout Description", height=80)

    # Structure
    with st.expander("🏗️ Structure"):
        st.markdown("#### Structural Details")
        c1, c2, c3 = st.columns([1, 1, 1])
        foundation = c1.selectbox("Foundation Type", ["Concrete", "Steel", "Wood", "Other"])
        columns = c2.text_input("Columns (Material/Spec)")
        trusses = c3.text_input("Trusses (Material/Spec)")

        c4, c5, c6 = st.columns([1, 1, 1])
        purlins = c4.text_input("Purlins (Material/Spec)")
        bracing = c5.text_input("Bracing (Type/Spec)")
        gutters = c6.text_input("Gutters (Type/Spec)")

        fasteners = st.text_input("Fasteners (Type/Spec)")

    # Cladding
    with st.expander("🪟 Cladding"):
        cladding = st.multiselect("Cladding Materials", ["Polyfilm", "Nets", "Shade Net", "Polycarbonate", "Glass"])

    # Ventilation
    with st.expander("🌬️ Ventilation"):
        st.markdown("#### Ventilation Features")
        c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
        ridge_vents = c1.checkbox("Ridge Vents")
        side_vents = c2.checkbox("Side Vents")
        rollup_sides = c3.checkbox("Roll-up Sides")
        netting = c4.checkbox("Netting")
        doors = c5.text_input("Doors (Type/Spec)")

    # Environmental Control
    with st.expander("🌡️ Environmental Control"):
        st.markdown("#### Environmental Controls")
        c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 1, 1])
        fans = c1.checkbox("Fans")
        pads = c2.checkbox("Pads")
        heaters = c3.checkbox("Heaters")
        foggers = c4.checkbox("Foggers")
        sensors = c5.checkbox("Sensors")
        automation = c6.checkbox("Automation")

    # Irrigation & Fertigation
    with st.expander("💧 Irrigation & Fertigation"):
        st.markdown("#### Irrigation System")
        c1, c2 = st.columns([2, 1])
        water_source = c1.text_input("Water Source")
        drip_system = c2.checkbox("Drip System")
        fert_unit = c2.checkbox("Fertigation Unit")
        pumps = c2.checkbox("Pumps")
        filters = c2.checkbox("Filters")

    # Crop Planning
    with st.expander("🌱 Crop Planning"):
        st.markdown("#### Crop Details")
        c1, c2 = st.columns([2, 1])
        crop_type = c1.text_input("Crop Type(s)")
        crop_height = c2.number_input("Crop Height (cm)", min_value=0.0)
        crop_layout = st.text_area("Crop Layout", height=80)
        rotation = st.text_input("Crop Rotation Plan")

    # Operations & Safety
    with st.expander("🛡️ Operations & Safety"):
        st.markdown("#### Operations & Safety")
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
        pathways = c1.text_input("Pathways (Spec/Material)")
        lighting = c2.checkbox("Lighting")
        emergency_exits = c3.checkbox("Emergency Exits")
        fire_safety = c4.checkbox("Fire Safety")
        security = st.checkbox("Security Measures")

    # Regulatory
   # Regulatory
    with st.expander("📑 Regulatory"):
        st.markdown("#### Regulatory Compliance")
        c1, c2 = st.columns([1, 1])
        standards = c1.text_area("Applicable Standards", height=68)
        certificates = c2.text_area("Required Certificates", height=68)
        c3, c4 = st.columns([1, 1])
        permits = c3.text_area("Permits Needed", height=68)
        training = c4.text_area("Training Requirements", height=68)

    submitted = st.form_submit_button("Submit All Details")

if submitted:
    st.success("✅ All details submitted! You can now process or display the results as needed.")
    # Here you can add code to process, display, or save the collected data.
