import streamlit as st

# 1. Create the Sidebar Selection
st.sidebar.title("Appearance")
theme_selection = st.sidebar.radio("Choose your theme:", ["Light", "Dark"])

# 2. Define the CSS for Light and Dark modes
# Note: We target the main app (.stApp) and the sidebar (section[data-testid="stSidebar"])
dark_theme_css = """
<style>
    /* Main App Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #262730;
        color: #FAFAFA;
    }
    /* Adjust Header/Text Colors */
    h1, h2, h3, h4, h5, h6, p, li {
        color: #FAFAFA !important;
    }
</style>
"""

light_theme_css = """
<style>
    /* Main App Background */
    .stApp {
        background-color: #FFFFFF;
        color: #000000;
    }
    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #F0F2F6;
        color: #000000;
    }
    /* Adjust Header/Text Colors */
    h1, h2, h3, h4, h5, h6, p, li {
        color: #000000 !important;
    }
</style>
"""

# 3. Apply the CSS based on selection
if theme_selection == "Dark":
    st.markdown(dark_theme_css, unsafe_allow_html=True)
else:
    st.markdown(light_theme_css, unsafe_allow_html=True)

# --- DEMO CONTENT ---
st.title("Dynamic Theme Switcher")
st.write("This is an example of changing colors using CSS injection.")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
with col2:
    st.metric(label="Humidity", value="45%", delta="-2%")

st.line_chart([10, 20, 30, 40, 35, 45, 50])