import streamlit as st

st.title("Hi I'm Uzair👋")
st.text("")
st.text("")
st.text("")
st.subheader("Professional Summary")
st.write("""I'm a Ethical Hacker and a Security Researcher.Currently working in the AWS Cloud 
I love to explore new technologies and their working.I have a 5 year working experience in the 
field of networking👨🏽‍💻 and cybersecurity👮🔑⚠️🔒 """)
st.sidebar.caption('Want to connect with me 👇?')
st.sidebar.write('📧: m.uzairkhan799@gmail.com')

st.text("")
st.text("")
st.text("")
st.subheader("My Skills🤹 and Tool Set⚒️")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.button('AWSCloud')
with col2:
    st.button(' Penetration testing')
with col3:
    st.button('Networking')


col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.button('Wireshark')
with col2:
    st.button('NetworkSecurity')
with col3:
    st.button('Kali Linux')


st.text("")
st.text("")
st.text("")
st.subheader("My Education🎓")
st.write("Following is my Academic Education")
st.markdown("- Bsc in Space Science and Technology")
st.markdown("- PGD in CyberSecurity")
st.markdown("- BS in Computer Science")


st.text("")
st.text("")
st.text("")
st.subheader("My Achievements🏆")

st.markdown("- Microsoft Azure Cloud Champion(Asian Region)")
st.markdown("- Nasa Certified Junior Researcher")
st.markdown("- AWS Community Builder(Top member)")
