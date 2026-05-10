import discord
from discord.ext import commands
from model import get_class
from keras.models import load_model
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="¿", intents=intents)

# Carga el modelo una sola vez al arrancar
MODEL = load_model("./keras_model.h5", compile=False)

RAZAS_INFO = {
    "Golden Retriever": "🐶 Raza muy popular, conocida por ser amigable y obediente.",
    "Xoloitzcuintle":   "🐶 Raza ancestral mexicana, también conocida como 'perro sin pelo'.",
    "Siames":           "🐱 Raza muy reconocida por sus ojos azules y personalidad vocal.",
    "Khao Manee":       "🐱 Raza tailandesa poco conocida, considerada símbolo de buena suerte.",
}

EXTENSIONES_VALIDAS = (".jpg", ".jpeg", ".png", ".webp")

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user.name} ({bot.user.id})")

@bot.command()
async def check(ctx):
    if not ctx.message.attachments:
        await ctx.send("📎 Por favor adjunta una imagen para clasificarla. Ejemplo: `?check` + imagen.")
        return

    for attachment in ctx.message.attachments:

        # Verificar que sea una imagen válida
        if not attachment.filename.lower().endswith(EXTENSIONES_VALIDAS):
            await ctx.send("⚠️ Solo se aceptan imágenes en formato JPG, PNG o WEBP.")
            continue

        file_path = f"temp_{attachment.filename}"

        try:
            await attachment.save(file_path)

            class_name, confidence_score = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=file_path
            )

            # Mensaje con Embed
            descripcion = RAZAS_INFO.get(class_name.strip(), "Raza identificada por el modelo.")

            embed = discord.Embed(
                title="🔍 Resultado de Clasificación",
                color=discord.Color.blurple()
            )
            embed.add_field(name="Raza detectada", value=f"**{class_name.strip()}**", inline=False)
            embed.add_field(name="Confianza",       value=f"`{confidence_score:.2f}%`",  inline=True)
            embed.add_field(name="Sobre esta raza", value=descripcion,                    inline=False)
            embed.set_footer(text=f"Solicitado por {ctx.author.display_name}")

            await ctx.send(embed=embed)

        finally:
            # Elimina el archivo temporal siempre, aunque haya error
            if os.path.exists(file_path):
                os.remove(file_path)

@bot.command()
async def razas(ctx):
    """Muestra las razas que el bot puede identificar."""
    embed = discord.Embed(
        title="🐾 Razas que puedo identificar",
        color=discord.Color.green()
    )
    for raza, info in RAZAS_INFO.items():
        embed.add_field(name=raza, value=info, inline=False)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))