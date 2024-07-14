import streamlit as st
import google.generativeai as genai

#st.set_page_config(page_tittle='Daniel S', page_icon='🦾')

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Hii!! :wave:")
    st.title("I am Daniel S.")

with col2:
    st.image("images/profile_hack.png")

st.title(" ")

persona = """
        You are Daniel AI bot. You help people answer questions about your self (i.e Daniel)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Daniel: 
         
 	Daniel Sarabia is an electronic engineering graduate, passionate about technology, programming, computer vision and is learning cybersecurity.
	Daniel studied at the "Universidad del Valle" (La Paz - Bolivia) and is interested in continuing to study the integration of artificial vision with robotics, and electronics with cybersecurity.
	Daniel has been president of the scientific society of electronics, telecommunications and mechatronics (SOCIETM). He was also the chair of the IEEE student branch of his university.
 	Daniel has experience teaching educational robotics, carrying out electronics and robotics projects.

	Daniel's Email: dsarabiay@gmail.com
	Daniel's Facebook: https://www.facebook.com/daniel.sarabia.5811/
	Daniel's Linkdin: https://www.linkedin.com/in/daniel-sarabia-638112176/
	SOCIETM's Facebook: https://www.facebook.com/profile.php?id=100091430621831
	IEEE Student Branch's Facebook: https://www.facebook.com/profile.php?id=100092660732519
	"""

st.title("Daniel's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("Tell me", use_container_width=400):
    prompt = persona + "Here is the question that the user ask: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

with st.expander("IEEEXtreme 18.0"):
	col1, col2 = st.columns(2)
	with col1:
	    st.subheader("IEEEXtreme")
	    st.write("- Hackaton from IEEE 18.0 Version")
	    st.write("- 700+ Students branchs")
	    st.write("- 24 hours programming")
	    st.write("- 18k+ participants")
	    st.button("Youtube", "https://www.youtube.com/@Daniel-xg2lk", "Canal de youtube")
	
	with col2:
	    st.video("https://www.youtube.com/watch?v=zpvw8AjW7iU&ab_channel=Daniel")

st.title(" ")

st.title("My inspiration morning")
st.image("images/g1.jpg")

st.write(" ")
st.title("My skills")
st.slider("Programming", 0, 100, 70)
st.slider("Electronic", 0, 100, 80)
st.slider("Robotic", 0, 100, 90)

st.file_uploader("Upload a file")

st.write(" ")
st.title("Galery")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")
    st.image("images/g4.jpg")

with col2:
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
    st.image("images/g7.jpg")

with col3:
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")
    st.image("images/g10.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("dsarabiay@gmail.com")
