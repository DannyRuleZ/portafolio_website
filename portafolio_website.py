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

st.subheader("Daniel's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("Tell me", use_container_width=400):
    prompt = persona + "Here is the question that the user ask: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.subheader(" ")

st.subheader("Future events")
with st.expander("IEEEXtreme 18.0"):
	col1, col2 = st.columns(2)
	with col1:
	    st.subheader("IEEEXtreme")
	    st.write("- Hackaton from IEEE 18.0 Version")
	    st.write("- 700+ Students branchs")
	    st.write("- 24 hours programming")
	    st.write("- 18k+ participants")
	    st.write("[Mas informacion](https://ieeextreme.org/)")
	
	with col2:
	    st.video("https://www.youtube.com/watch?v=zpvw8AjW7iU&ab_channel=Daniel")

st.subheader(" ")

st.subheader("Which channel woutld you like to see?")
list = ["Select channel", "Electronic", "Robotic", "Programming", "embedded systems", "Math & Science", "Office", "Technology news"]
result = st.selectbox("Select", list)
#st.write(f"tu canal es: {result}")
if result == "Electronic":
    st.write("- [LaBuhardillaDelLoco](https://www.youtube.com/@LaBuhardillaDelLoco/videos)")
	st.write("- [Ampletos](https://www.youtube.com/c/Ampletos/videos)")
st.write("- []()")
st.write("- []()")
st.write("- []()")
st.write("- []()")
st.write("- []()")
elif result == "Robotic":
    st.write("- [Héctor Pérez](https://www.youtube.com/c/hectorperezwordpress)")
st.write("- []()")
st.write("- []()")
st.write("- []()")
elif result == "Programming":
st.write("- [Programación ATS](https://www.youtube.com/c/Programaci%C3%B3nATS)")
st.write("- []()")
st.write("- []()")
elif result == "embedded systems":
    st.write("- [Wels](https://www.youtube.com/c/Wels_Theory/videos)")
st.write("- []()")
st.write("- []()")
elif result == "Math & Science":
    st.write("- [The Organic Chemistry Tutor](https://www.youtube.com/c/TheOrganicChemistryTutor/videos)")
st.write("- [Edgar Salazar](https://www.youtube.com/@edgarsalazar1045/featured)")
st.write("- [Anderson Matemáticas R8](https://www.youtube.com/c/andersonmatematicas/videos)")
st.write("- [Creciendo en Ingeniería Mecánica y Eléctrica](https://www.youtube.com/channel/UCGoUK4hID8QOjQBfp-yeYBw)")
st.write("- []()")
elif result == "Office":
    st.write("- [Franklin García](https://www.youtube.com/user/MrFranklingr/featured)")
st.write("- [Dostin Hurtado](https://www.youtube.com/c/DostinHurtado)")
st.write("- []()")
st.write("- []()")
st.write("- []()")
elif result == "Technology news":
st.write("- [GioCode](https://www.youtube.com/channel/UC3yDP9DLJI7rPqPovQaOJMg)")
st.write("- []()")
else:
    st.write("Por favor, selecciona un canal")

st.write(" ")
st.subheader("My skills")
st.slider("Programming", 0, 100, 70)
st.slider("Electronic", 0, 100, 80)
st.slider("Robotic", 0, 100, 90)

st.file_uploader("Upload a file")

st.write(" ")
st.subheader("Galery")
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
