import streamlit as st
import pyrebase
from datetime import datetime
from streamlit_option_menu import option_menu
from PIL import Image
import requests
import streamlit.components.v1 as components


#streamlit-1.16.0


im = Image.open("icons8-rabbit-100.png")
st.set_page_config(
    page_title="Rabbit.web",
    page_icon=im
   
)




def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.squarespace-cdn.com/content/v1/5fe4caeadae61a2f19719512/1609537599282-NP1M5U8V0U0NDWQY9QRR/Starfield");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

firebaseConfig = {
  "apiKey": "AIzaSyDTY8XA0vTApBwTVurob82FFUOMBkWzg-w",
  "authDomain": "none-d12f3.firebaseapp.com",
  "projectId": "none-d12f3",
  "storageBucket": "none-d12f3.appspot.com",
  "databaseURL":"https://none-d12f3-default-rtdb.firebaseio.com/",
  "messagingSenderId": "300216235483",
  "appId": "1:300216235483:web:cf88ae462225f8ce16e3fe",
  "measurementId": "G-MLZN385TMD"
};

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

data=firebase.database()
storage=firebase.storage()

st.markdown("<center><img src=https://img.icons8.com/ios-filled/100/228BE6/rabbit.png; alt=centered image; height=100; width=100> </center>",unsafe_allow_html=True)
labela=("<h1 style='font-family:arial;color:#228BE6;text-align:center'>Rabbit.web</h1>")
st.markdown(labela,unsafe_allow_html=True)
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
streamlitstyle = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.sidebar.markdown(streamlitstyle, unsafe_allow_html=True)
st.sidebar.markdown("<center><img src=https://img.icons8.com/ios-filled/100/228BE6/rabbit.png ; alt=centered image; height=100; width=100> </center>",unsafe_allow_html=True)



label=("<h1 style='font-family:arial;color:#228BE6;text-align:center'>Rabbit.web</h1>")
st.sidebar.markdown(label,unsafe_allow_html=True)

labelb=("<h4 style='font-family:arial;color:#228BE6;text-align:center'>A perfect place to chat with your friend's</h4>")
st.sidebar.markdown(labelb,unsafe_allow_html=True)

choice=st.sidebar.selectbox("Sign in to your account or create an account :",["sign in","create an account"])



email=st.sidebar.text_input("",placeholder="Hello please enter you email")
passw=st.sidebar.text_input("",placeholder="Hello please enter your password",type="password")



if choice=="create an account":
    handle=st.sidebar.text_input("",placeholder="Hello please enter your name")
    subbt=st.sidebar.button("Create an new account")

    if subbt:
        user=auth.create_user_with_email_and_password(email,passw)
        st.success("Your Rabbit.web account has created successfully !")
     
        user=auth.sign_in_with_email_and_password(email,passw)
        data.child(user["localId"]).child("Handle").set(handle)
        data.child(user["localId"]).child("ID").set(user["localId"])
        st.info("You have successfully logged in")
        
            
       

       
if choice=="sign in":
   
    signin=st.sidebar.checkbox("sign in")
    

    if signin:
            user=auth.sign_in_with_email_and_password(email,passw)
            
             
            nav = option_menu(menu_title=None,   options=["Home", "Posts", "Settings","About us"],icons=["house", "book", "gear","info"],menu_icon="cast",default_index=0,orientation="verticle",styles={
        "container": {"padding": "0!important", "background-color": "#1c1c1c"},
        "icon": {"color": "lightblue", "font-size": "20px"}, 
        "nav-link": {"text-align":"left", "margin":"0px", "--hover-color": "#1c1c1c"},
        "nav-link-selected": {"background-color": "#228BE6","color":"#1c1c1c"},})
            
            if nav =="Home":
                
                post=st.text_input("",placeholder="share your thought with your friend's",max_chars=250)
                add_post=st.button("Share your thought")
                

                    
                if add_post:
                    now=datetime.now()
                    dt=now.strftime("%d / %m / %y")
                    dtt=now.strftime("%I:%M %p")

                    post="Post: "+post+ ";"+"  Posted on:"+ dt +"  at  "+dtt
                    results=data.child(user["localId"]).child("Posts").push(post)
                    st.balloons()
                components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                col1,col2=st.columns(2)

                with col1:
                    nimg=data.child(user["localId"]).child("Image").get().val()
                    if nimg is not None:
                        v=data.child(user["localId"]).child("Image").get()
                        for img in v.each():
                            imgc=img.val()
                        st.image(imgc,use_column_width=True)
                       
                    else:
                         st.info("Oop's no profile pic till now ")
                
            

                with col2:
                    st.title("Post's :")
                    all_posts=data.child(user['localId']).child("Posts").get()
                   
                    if all_posts.val() is not None:
                        for Posts in reversed(all_posts.each()):
                             st.success(Posts.val())
                   
                    else:
                            st.info("Oop's no thought till now")
                col3=st.columns(1)
                with col1:
                    st.title("Bio :")
                    all_bio=data.child(user["localId"]).child("Bio").get()

                    if all_bio.val() is not None:
                        
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)
                    else:
                        st.info("Oop's no Bio  till now")
                
                
            elif nav =="Settings":
                    nimg=data.child(user["localId"]).child("Image").get().val()
                    if nimg is not None:
                        Image=data.child(user["localId"]).child("Image").get()
                        for img in Image.each():
                            imgc=img.val()
                        st.image(imgc)

                        expa=st.expander("Change your profile pic")

                        with expa:
                            newimgp=st.file_uploader("Please choose  your profile pic")
                            upbt=st.button("Upload profile pic")
                            if upbt:
                                uid=user["localId"]
                                dataup=storage.child(uid).put(newimgp,user["idToken"])
                                aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])

                                data.child(user["localId"]).child("Image").push(aimgdata)

                                st.info("Your profile pic is set successfully")
                                st.balloons()
                    else:
                                st.info("Oop's no profile pic till now")
                                newimgp=st.file_uploader("Please  choose your profile pic")
                                upbt=st.button("Upload profile pic")
                                if upbt:
                                    uid=user["localId"]
                                    dataup=storage.child(uid).put(newimgp,user["idToken"])
                                    aimgdata=storage.child(uid).get_url(dataup["downloadTokens"])
                                    data.child(user["localId"]).child("Image").push(aimgdata)

                    bio=data.child(user["localId"]).child("Bio").get().val()
                    if bio is not None:
                        bio=data.child(user["localId"]).child("Bio").get()
                        for bio in bio.each():
                            bioc=bio.val()
                        st.info(bioc)

                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                            

                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Your Bio is set successfully")
                            st.balloons()
                    else:
                        st.info("Oop's no Bio till now")
                        bioin=st.text_area("",placeholder="Enter your Bio to be uploaded eg: name,date of birth etc")
                        upbtn=st.button("Upload Bio")

                        if upbtn:
                           
                           
                            data.child(user["localId"]).child("Bio").push(bioin)

                            st.info("Your Bio is set successfully")
                            st.balloons()
               

            elif nav=="Posts":
                allu=data.get()
                resa=[]

                for ush in allu.each():
                  
                    k=ush.val().get("Handle")
                    resa.append(k)
            
                n = len(resa)
            
                st.title("Search your Friend's :")
                cho = st.selectbox('',resa)
                pusha = st.button('Show Profile')

                if pusha:
                    for ush in allu.each():
                        k=ush.val().get("Handle")
                        if k==cho:
                            l=ush.val().get("ID")

                            hn=data.child(l).child("Handle").get().val()

                            st.markdown(hn,unsafe_allow_html=True)
                            components.html("""<hr style="height:2px;border:none;color:#333;background-color:white;" /> """)
                            col1,col2=st.columns(2)
                            with col1:
                                nimg=data.child(l).child("Image").get().val()
                                if nimg is not None:
                                    v=data.child(l).child("Image").get()
                                    for img in v.each():
                                        imgc=img.val()
                                    st.image(imgc,use_column_width=True)
                       
                                else:
                                    st.info("Oop's no profile pic till now ")
                
                                
                            

                            with col2:
                                st.title("Post's :")
                                all_posts=data.child(l).child("Posts").get()
                                if all_posts.val() is not None:
                                    for Posts in reversed(all_posts.each()):
                                        st.success(Posts.val())
                                else:
                                    st.info("Oop's no thought till now")
                            col3=st.columns(1)
                            with col1:
                                st.title("Bio :")
                                all_bio=data.child(l).child("Bio").get()

                                if all_bio.val() is not None:
                                    bio=data.child(l).child("Bio").get()
                                    for bio in bio.each():
                                        bioc=bio.val()
                                        st.info(bioc)
                                else:
                                   st.info("Oop's no Bio  till now")
            
            else:
                 st.write("Rabbit.web")
                 st.write("Created and maintained by Navpreet Singh")
                 st.write("For help,feedback or suggestion contact our company at rabbitweb854@gmail.com")
                 st.write("For reporting a user on Rabbit.web  contact us at rabbitweb854@gmail.com")
                


                  

                  
                 

                        
                    
            
                
            
                                    
