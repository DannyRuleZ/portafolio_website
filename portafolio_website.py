import streamlit as st
import google.generativeai as genai
import random
import string

#st.set_page_config(page_tittle="Daniel S", page_icon="🦾")

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_?.!$<#>&+%="

base = minus + mayus + numeros + simbolos


col1 , col2 = st.columns(2)

with col1:
    st.title(" ")
    st.subheader("Hii!! :wave:")
    st.title("I am Daniel S.")

with col2:
    st.image("images/Daniel_Sarabia.png")

st.subheader(" ")

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
	    st.write("[More information](https://ieeextreme.org/)")
	
	with col2:
	    st.video("https://www.youtube.com/watch?v=zpvw8AjW7iU&ab_channel=Daniel")

st.subheader(" ")



def generate_password(length):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = "".join(random.choice(characters) for _ in range(length))
	return password

with st.expander("Password generator"):
	length = st.text_input("Password size")
	if st.button("Tell me", use_container_width=300):
		try:
			password_length = int(length)
			if password_length <= 0:
				st.error("Password legth must be greater than 0")
			else:
				generate_password = generate_password(password_length)
				st.success(f"Generated password: {generate_password}")
		except ValueError:
			st.error("Invalid password length. Enter a number pls")
		

st.subheader("Which channel woutld you like to see?")
list = ["What would you like to learn?", "Best channel", "Electronic", "Robotic", "Programming", "Embedded systems", "Hacking", "Network", "Math & Science", "Office", "Technology news"]
result = st.selectbox("Select", list)
#st.write(f"tu canal es: {result}")
channels = {
	"Best channel": [
        ("Murtaza's Workshop - Robotics and AI", "https://www.youtube.com/@murtazasworkshop")
    ],
    "Electronic": [
        ("LaBuhardillaDelLoco", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_1"),
        ("Ampletos", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_2"),
	    ("Electrónica y Circuitos", "https://www.youtube.com/c/Electr%C3%B3nicayCircuitos97/videos"),
	    ("Humberto Higinio", "https://www.youtube.com/c/HumbertoHiginio/videos"),
	    ("ELECTRONOOBS en Español", "https://www.youtube.com/c/ELECTRONOOBSenEspa%C3%B1ol"),
	    ("ELECTRONOOBS", "https://www.youtube.com/@ELECTRONOOBS/featured"),
	    ("Mentalidad De Ingeniería", "https://www.youtube.com/c/MentalidadDeIngenier%C3%ADa")
    ],
    "Robotic": [
        ("Héctor Pérez", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_3"),
	    ("Oscar gonzalez", "https://www.youtube.com/c/oscargo9/videos"),
	    ("Electronic Clinic", "https://www.youtube.com/@ElectroniClinic/videos"),
	    ("Bitwise Ar", "https://www.youtube.com/@BitwiseAr"),
	    ("hash include electronics", "https://www.youtube.com/c/hashincludeelectronics"),
	    ("CarlosVolt Electrónica y Robótica", "https://www.youtube.com/@Carlosvolt/videos"),
	    ("That Project", "https://www.youtube.com/@ThatProject/videos"),
	    ("Jadsa Tech", "https://www.youtube.com/@jadsa/videos"),
	    ("Edison R Sasig - Roboticoss", "https://www.youtube.com/@roboticoss/videos")
    ],
    "Programming": [
        ("Programación ATS", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_4"),
	    ("Fazt", "https://www.youtube.com/@FaztTech")
    ],
    "Embedded systems": [
        ("Wels", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_5")
    ],
	"Hacking": [
        ("s4vitar", "https://www.youtube.com/@s4vitar"),
        ("Cosmodium CyberSecurity", "https://www.youtube.com/@CosmodiumCS/videos"),
		("Academia de Ciberseguridad", "https://www.youtube.com/@academiadeciberseguridad"),
		("Dolbuck S.L.", "https://www.youtube.com/@dolbuck_ciberseguridad"),
		("Hixec", "https://www.youtube.com/@Hixec"),
		("VulnHunters", "https://www.youtube.com/@VulnHunters/featured")
    ],
	"Network": [
        ("Network Warriors", "https://www.youtube.com/@NetworkWarriors/videos"),
		("RedesCiber - Tu Academia de Redes y Ciberseguridad", "https://www.youtube.com/@RedesCiber")
	],
    "Math & Science": [
        ("The Organic Chemistry Tutor", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_6"),
        ("Edgar Salazar", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_7"),
        ("Anderson Matemáticas R8", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_8"),
        ("Creciendo en Ingeniería Mecánica y Eléctrica", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_9"),
	    ("MIT OpenCourseWare", "https://www.youtube.com/c/mitocw"),
	    ("Luis Felipe de Jesús Hernández Quintanar", "https://www.youtube.com/@luisfelipedejesushernandez5661/videos")
    ],
    "Office": [
        ("Franklin García", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_10"),
        ("Dostin Hurtado", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_11"),
	    ("SMARTpro Academy", "https://www.youtube.com/channel/UCqtA50lNwtNAg6S0UkI5bxw"),
	    ("Officefacil", "https://www.youtube.com/@Officefacil")
    ],
    "Technology news": [
        ("GioCode", "https://www.youtube.com/channel/YOUR_CHANNEL_ID_12"),
	    ("Branch Education", "https://www.youtube.com/@BranchEducation")
    ]
}

# Imprimir enlaces según la selección
if result in channels:
    for channel, link in channels[result]:
        st.write(f"- [{channel}]({link})")
else:
    st.write("Please, select a topic")

st.write(" ")
st.subheader("My skills")
st.slider("Programming", 0, 100, 70)
st.slider("Electronic", 0, 100, 80)
st.slider("Robotic", 0, 100, 90)
st.slider("Cybersecurity", 0, 100, 70)

#st.file_uploader("Upload a file")

st.write(" ")
st.subheader("Galery")
with st.expander("FETIN - Brasil"):
	st.subheader("Do we believe together?")
	st.write("This is the FETIN theme for the year 2023, which proposes that we all together make our ideas and dreams come true.")
	st.write("FETIN is more than a technology fair, it is a space for people from all corners, from our corner here in Inatel to other corners of the world, to make their creativity and desire come true.")
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
		
with st.expander("Sao Paulo"):
	st.write("A very impressive and very large city, the people are very happy and the food is extraordinary, if you have the opportunity to visit it, do it!")
	col1, col2, col3 = st.columns(3)
	with col1:
		st.image("images/g11.jpg")
	with col2:
		st.image("images/g12.jpg")
	with col3:
		st.image("images/g13.jpg")
		
#with st.expander("warbot death"):
	#st.video("warbot1.mp4")
	

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("dsarabiay@gmail.com")
