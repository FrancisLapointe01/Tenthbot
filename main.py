from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch

import asyncio
import dontLeak
import PersonaSystem
import custom_shoutouts

APP_ID = dontLeak.client_id
APP_SECRET = dontLeak.client_secret
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_BROADCAST]
TARGET_CHANNEL = 'TenthEmperor'

# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
async def on_message(msg: ChatMessage):
    print(f'{msg.user.display_name} - {msg.text}')
async def shoutout_command(cmd: ChatCommand):
    if not (cmd.user.mod or cmd.user.name.lower() == TARGET_CHANNEL.lower()):
        return

    if not cmd.parameter:
        await cmd.reply("Usage: !so <username>")
        return

    username = cmd.parameter.strip().lstrip('@').lower()

    # get user
    user = None
    async for u in cmd.chat.twitch.get_users(logins=[username]):
        user = u
        break

    if user is None:
        await cmd.reply("User not found.")
        return

    # get channel info
    channel_data = await cmd.chat.twitch.get_channel_information(
        broadcaster_id=[user.id]
    )

    game_name = None
    if channel_data and len(channel_data) > 0:
        game_name = channel_data[0].game_name

    if game_name:
        message = (
            f"Go check out https://twitch.tv/{user.login}! "
            f"They were last streaming {game_name}"
        )
    else:
        message = (
            f"Go check out https://twitch.tv/{user.login}!"
        )

    await cmd.reply(message)
async def discord_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('We have a Discord over at: https://discord.gg/yBqBNeb')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')
async def run_bot():
    bot = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(bot, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await bot.set_user_authentication(token, USER_SCOPE, refresh_token)
    
    chat = await Chat(bot)
    
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.register_command('so', shoutout_command)
    chat.register_command('discord', discord_command)
    # chat.register_command('contract', PersonaSystem.summon_command)
    chat.register_command('pinky', custom_shoutouts.pinky_command)
    chat.start()
    
    try:
        input('Press Enter TO Stop Bot \n')
    finally:
        chat.stop()
        await bot.close()
        
bot_loop = asyncio.new_event_loop()
asyncio.set_event_loop(bot_loop)

bot_loop.run_until_complete(run_bot())
bot_loop.close()