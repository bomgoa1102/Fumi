import discord
import environ
from gtts import gTTS
from discord.ext import commands
from VoiceBot import VoiceCommand

import responses


async def run():
    env = environ.Env(
            DEBUG=(bool, False),
        )
    environ.Env.read_env('.env')

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(intents=intents, command_prefix= commands.when_mentioned_or('*'))
    await bot.add_cog(VoiceCommand(bot))

    @bot.event
    async def on_ready():
        print(f'{bot.user} is running')

    bot.run(env('TOKEN'))

        
    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return
    #     if message.channel.name != 'spambot':
    #         return
        
        
        # username = str(message.author)
        # user_message = str(message.content)
        # channel = str(message.channel)
        
        
        
        # if str(message.author.id) != ID:
        #     if user_message[0] == '/' and user_message[1] == '/':
        #         await message.channel.send(send_other(message))
        #     else: await message.author.send(send_other(message))
        # else:

        #     print(message)
        #     print("vvvvvvvvvvvvvvvvv")
        #     print(user_message)
            
        #     if user_message[0] == '/' and user_message[1] == '/':
        #         user_message = user_message[1:]
        #         await send_message(message, user_message, is_private=True)
        #     else:
        #         await send_message(message, user_message, is_private=False)
        
        # for mess in message.content:
        #     print(mess)
        
        
        
        
