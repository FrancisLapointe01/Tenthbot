from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.twitch import Twitch


import asyncio
import dontLeak


TARGET_CHANNEL = 'TenthEmperor'
PINKY_CHANNEL = "shiningbutterfly4"

async def pinky_command(cmd: ChatCommand):
    if not (cmd.user.mod or cmd.user.name.lower() == TARGET_CHANNEL.lower()):
        return

    user = None
    async for u in cmd.chat.twitch.get_users(logins=[PINKY_CHANNEL]):
        user = u
        break

    if not user:
        await cmd.reply("User not found.")
        return

    channel_data = await cmd.chat.twitch.get_channel_information(
        broadcaster_id=[user.id]
    )

    game_name = channel_data[0].game_name if channel_data else None

    message = (
        f"OMG IT'S PINKY I MEAN PINK PENGUIN I MEAN "
        f"SHININGBUTTERFLY4 I MEAN...." 
        f"Whatever her name is she's an amazing nintendo variety streamer and close friend of the channel"
        f"Go check her out at https://twitch.tv/{user.login} and tell her Franis Sent Ya!"
    )

    if game_name:
        message += f" She was last streaming {game_name}"

    await cmd.reply(message)


