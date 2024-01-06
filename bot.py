from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate

load_dotenv()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    description="Runs models on Replicate!",
    intents=intents,
)


@bot.command(aliases=["gen"])
async def generate(ctx, *, prompt):
    try:
        """Generate an image from a text prompt using the stable-diffusion model"""
        msg = await ctx.send(f"“{prompt}”\n> Generating...")
        output = replicate.run(
            "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            input={"prompt": prompt}
        )
        await msg.edit(content=f"{output}")
        print(output)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

@bot.command(aliases=["hin"])  # Define hdin as a bot command
async def hdin(ctx, *, prompt):
    try:
        msg = await ctx.send(f"“{prompt}”\n> Generating...")
        output = replicate.run(
            "xinntao/realesrgan:1b976a4d456ed9e4d1a846597b7614e79eadad3032e9124fa63859db0fd59b56",
            input={
                "img": prompt,
                "tile": 0,
                "scale": 2,
                "version": "General - v3",
                "face_enhance": True
            }
        )
        await msg.edit(content=f"{output}")
        print(output)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

bot.run(os.environ["DISCORD_TOKEN"])
