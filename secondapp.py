import streamlit as st
# page setup
st.set_page_config(page_title="🌏 My Streamlit App - Wira")

st.title("Layout And Sidebar")
col1, col2 = st.columns(2)

with col1:
    st.header("Left Side")
    name = st.text_input("Enter Your Name : ")
    if name:
        st.success(f'Welcome User {name}!')

with col2:
    st.header("Odd Even Checker")
    num = st.slider("Select A NUmber",1,100,3)
    if num%2==0:
        st.write("Even Number")
    else:
        st.write("Odd Number")


with st.sidebar:
    st.header("Control Panel")
    user_color = st.color_picker("Pick Your Favourite Color","#000000")
    st.write("You have selected : ", user_color)

# in sidebar provide 2 options to user
# select dark or light theme
# if user selects Dark change the theme of streamlit app

# --- Sidebar Theme Selector ---
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])

# --- CSS Styles for Themes ---
light_theme = """
<style>
body {
    background-color: #ffffff;
    color: #000000;
}
</style>
"""

dark_theme = """
<style>
body {
    background-color: #0e1117;
    color: #fafafa;
}
</style>
"""

# --- Apply Selected Theme ---
if theme == "Light":
    st.markdown(light_theme, unsafe_allow_html=True)
else:
    st.markdown(dark_theme, unsafe_allow_html=True)

# --- Main App Content ---
st.title("Streamlit Theme Switcher")
st.write(f"Current theme: **{theme}**")
st.write("The background and text color change based on your selection.")
