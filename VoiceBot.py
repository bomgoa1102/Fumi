import discord
import environ
from gtts import gTTS
from discord.ext import commands

import responses

class VoiceEntry:
    """Voice state cua nguoi request
    """
    def __init__(self, message):
        self.author = message.author
        self.channel = message.channel
        self.voice = message.author.voice

    def __str__(self) -> str:
        return f"{self.author} is the person who request text to speech in channel {self.channel}"

class VoiceState: # cai nay co don vi la 1, con trong VoiceCommand __init__ la mot dict ve cac bot trong cac server khac nhau, co the noi la hien gio ko can
    """Voice state cua bot
    """
    def __init__(self, bot):
        self.voice = None
        self.bot = bot

class VoiceCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_state = None #trang thai voice cua bot
        
    def __str__(self, bot) -> str:
        return f"{bot.message.content} >>> {VoiceEntry(bot.message)}"
        
    def get_user_state(self, message):
        state = VoiceEntry(message)
        return state
        
    def get_bot_voice_state(self, bot):
        state = VoiceState(bot)
        return state
    
    async def join_voice_channel(self, user: VoiceEntry):
        if user.voice is None:
            return await self.bot.say("Go join VC")
        
        if user.voice is self.bot.voice:
            return await self.bot.say("Already in your Voice Chat Channel")
        else: return await self.bot.say("W.I.P") #######################################
        # if self.
    
    @commands.command(name="say")
    async def say(self, ctx, *, arg):
        """
        Bot can say
        """
        await self.bot.say(arg)
    
    @commands.command(name="join")
    async def join(self, ctx):
        """
        Bot join voice chat
        """
        state_user = self.get_user_state(ctx.message) #lay trang thai user
        
        if state_user.channel is None:
            await self.bot.say("Join VC")
        else: await self.join_voice_channel(state_user)
        
# async def send_message(message, user_message, is_private):
#     try:
#         response = responses.handle(user_message)
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)

# def send_other(message):
#     try:
#         return f"Dit me may nhe {message.author.name}"
#     except Exception as e:
#         print(e)

# def is_connected(ctx):
#     voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
#     return voice_client and voice_client.is_connected()