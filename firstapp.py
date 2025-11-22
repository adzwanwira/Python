import streamlit as st
# title() --> it will display big title on web page
st.title("My first Streamlit App")
# write() --> it will print normal text on web page
st.write("Hello world!")

st.title("😀 Exploring Streamlit Widgets")
st.header("Bold and Italic Text")
st.write("**Bold** and *Italic* Text")

st.header("Number Slider")
age = st.slider("Select Your Age",1,100,30)   # min,max,defaultValue
st.write("Your age is 👴 : ",age)

st.header("Taking user input")
name = st.text_input("What is your name: ")
if name:
    st.success(f"Nice to meet you {name}! 😍")

st.header("Streamlit Button")
if st.button("Click Me!"):
    st.balloons()   # pops ballon animation

st.header("Markdown")
st.markdown("Hi I am **Markdown** method of *Streamlit*")
# markdown can be used for writing HTML content unlike write()

st.markdown("""
<h3>HTML Tag</h3>
<p>This is a paragraph</p>
""",unsafe_allow_html=True)

st.markdown("""
<p>Learn More About Streamlit Using :  
            <a href="https://streamlit.io/" title="Streamlit Official Docs">Streamlit</a> Link</p>
""",unsafe_allow_html=True)

st.header("Streamlit Code")
code1 = '''
def hello()
    print('I am the function")
'''
st.code(code1,language="python")

# latex() --> used to show ML Formula's
st.latex("(a+b)^2 = a^2 + b^2 + 2*a*b")
st.latex(r"\frac {1}{1+e^-score}")