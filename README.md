# SETUP


# API SETUP

  https://dev.twitch.tv/console

<p float="left">
   1 <img src="imgs/api1.PNG" width="150" />
    2<img src="imgs/api2.PNG" width="150" /> 
   3 <img src="imgs/api3.PNG" width="150" />
</p>


# Add API KEY
Open Main.py Add API KEYS

APP_ID = 'ADD YOUR TWITCH API ID'

APP_SECRET = 'ADD YOUR TWITCH API SECRET KEY'

USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]

TARGET_CHANNEL = 'ADD TWITCH USERNAME HERE'

# OPENAI API SETUP

https://platform.openai.com/account/api-keys

Open Main.py and add the API key in two spots using the same api key. Make sure to add the API to both spots.

async def on_message(msg: ChatMessage):

    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')

    openai.api_key = "ADD YOUR OPENAI API KEY"

    response = openai.Completion.create(


# PYTHON SETUP

https://www.python.org/downloads/release/python-390/

 simply download and install, then open the Command Prompt (CMD). Navigate to the folder where the Main.py file is located using the CD command. Then, run the command pip install -r requirements.txt to install the required packages. Finally, run the Python script and the AI voice chatbot will be ready to use!