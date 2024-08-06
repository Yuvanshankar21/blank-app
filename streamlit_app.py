import streamlit as st
from googleapiclient.discovery import build

API_KEY="AIzaSyCuekQFfYgP8dPgShVZRyQg3havu7kN6jA"
youtube = build("youtube","v3",developerKey=API_KEY);
channelId = "UC9dQjP9Vp1swi-UBA8vxu3g"
request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channelId
    )

response = request.execute();
st.write(response)