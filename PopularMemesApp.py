import streamlit as st
import json
import requests


# App description
st.markdown('''
# Popular Memes App
This web app displays a vast collection of current popular meme templates.

- Source Code: 
- Language: `Python`
- Libraries: `streamlit`
''')
st.write('---')


# Retrieving countries code
retrieveMemes = requests.get('https://api.imgflip.com/get_memes')

memes = json.loads(retrieveMemes.content)

for meme in memes['data']['memes']:
    st.image(meme['url'])
    st.write(meme['name'])

