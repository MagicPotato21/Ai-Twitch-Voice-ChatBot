# SETUP


# API SETUP

Step 1  https://dev.twitch.tv/console

<p float="left">
   1 <img src="imgs/api1.PNG" width="150" />
    2<img src="imgs/api2.PNG" width="150" /> 
   3 <img src="imgs/api3.PNG" width="150" />
</p>


# Add API KEY
Open Main.py
APP_ID = 'ADD YOUR TWITCH API ID'
APP_SECRET = 'ADD YOUR TWITCH API SECRET KEY'
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'ADD TWITCH USERNAME HERE'

# OPENAI API SETUP