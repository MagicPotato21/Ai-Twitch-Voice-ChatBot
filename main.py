from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio
import pyttsx3
import openai
import threading

APP_ID = 'ADD YOUR TWITCH API ID'
APP_SECRET = 'ADD YOUR TWITCH API SECRET KEY'
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'ADD TWITCH USERNAME'


# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    # you can do other bot initialization things in here



# this will be called whenever a message in a channel was send by either the bot OR another user
async def on_message(msg: ChatMessage):
    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
    openai.api_key = "ADD YOUR OPENAI API KEY"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{msg.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response["choices"][0]["text"].strip()

    speak_text(text, voice="female")




# this will be called whenever someone subscribes to a channel
async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\\n'
          f'  Type: {sub.sub_plan}\\n'
          f'  Message: {sub.sub_message}')


# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    task = asyncio.create_task(get_response(cmd))

    try:
        await asyncio.wait_for(task, timeout=5.0)
    except asyncio.TimeoutError:
        text = "I'm sorry, I didn't respond in time."
    else:
        text = task.result()

    speak_text(text, voice="female")


async def get_response(cmd: ChatCommand):
    openai.api_key = "ADD YOUR OPENAI API KEY"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{cmd.parameter}",
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"].strip()


def speak_text(text="I will speak this text", voice="female"):
    def run_speak():
        engine = pyttsx3.init()
        lock = threading.Lock()
        voices = engine.getProperty('voices')
        if voice.lower() == "male":
            engine.setProperty('voice', voices[0].id)
        elif voice.lower() == "female":
            engine.setProperty('voice', voices[1].id)

        else:
            raise Exception("voice param must either be 'male' or 'female' ")
        engine.say(text)
        engine.runAndWait()

    t = threading.Thread(target=run_speak)
    t.start()




# this is where we set up the bot
async def run():
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # register the handlers for the events you want

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)
    # listen to chat messages
    chat.register_event(ChatEvent.MESSAGE, on_message)
    # listen to channel subscriptions
    chat.register_event(ChatEvent.SUB, on_sub)
    # there are more events, you can view them all in this documentation

    # you can directly register commands and their handlers, this will register the !reply command



    # we are done with our setup, lets start this bot up!
    chat.start()

    # lets run till we press enter in the console
    try:
        input('press ENTER to stop\\n')
    finally:
        # now we can close the chat bot and the twitch api client
        chat.stop()
        await twitch.close()


# lets run our setup
asyncio.run(run())