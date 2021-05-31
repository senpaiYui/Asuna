# Import Discord Package
import discord
from discord.ext import commands

import os

# Client (our bot)

client = commands.Bot(command_prefix='A!')

@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
         member = ctx.message.author
    userAvatar = member.avatar_url

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar of {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

snipe_message_content = None
snipe_messgae_author = None

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    await asyncio.sleep(60)
    snipe_message_author = None
    snipe_message_content = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:

        await message.channel.send("Nothing to snipe is found here!")
    else:
        embed =discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Resquested By {message.author.name}#{message.author.discriminator}")
        embed.set_author(name=f"Get sniped bitch deleted by : {snipe_message_author}")
    
        await message.channel.send(embed=embed)
        return

@client.command(aliases=['user', 'info'])

async def whois(ctx, member : discord.Member = None):
    member = ctx.author if not member else member

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}, icon_url=ctx.author.avatar_url")

    embed.add_field(name ="ID", value = member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"))

    embed.add_field(name="Top roles", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} messages got deleted")

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("you need to spectify an amount")
    if isinstance(error, commands.BadArgument):
        await ctx.send("Give an intiger")

    raise error

@commands.command
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason= "No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} was kicked by{ctx.author.mention}. [{reason}]")

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.send(f"{member.mention} was banned by{ctx.author.mention}. [{reason}]")
    await member.ban(reason=reason)

@client.command(aliases=['M'])
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member : discord.Member, *, reason= None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not muteRole: 
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_messages_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for a reason {reason}")
        await member.send(send(f"You were muted in the server {guild.name} for {reason}"))

@client.command(name='version')
async def Version(context):

        myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0.0", color=0x00FDDF)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="April 23, 2021", inline=False)
        myEmbed.set_footer(text="You gay for looking at this")
        myEmbed.set_author(name="Bella")

        await context.message.channel.send(embed=myEmbed)
        await general_channel.send(embed=myEmbed)
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Eating meow out'))
    print('Asuna bot is now online')

@client.event
async def on_message(message):

    if message.content == 'Gay boy':
        general_channel = client.get_channel(835151717749227524)
        await general_channel.send('He is very gay')

    if message.content == 'Butterfly':
        general_channel = client.get_channel(834425526767976481)
        await general_channel.send('She is very gay')
    

         

    await client.process_commands(message)   

async def on_message_delete(self, message):
    await message.channel.send("A message was deleted here")




     
     # Run the client on the server

client.run('ODM0NDIzNjE0MjU4NDEzNjE4.YIArjA.woo9wfOvkWAk1XJj3CzN2e97XWM')