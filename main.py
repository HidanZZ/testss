from pyrogram import Client, filters
from pyrogram import enums

app = Client(
    "mvip",
    api_id="29249286",
    api_hash="952c7ee7c812bfb85e66a8eb26cb1d44"
)

users_replied_to = set()

@app.on_message(filters.private & ~filters.me)
def auto_reply(client, message):
    user_id = message.from_user.id
    if user_id not in users_replied_to:
        message.reply('''**salut  frero j’ai créé un vip avec que des media payant mym, actuellement j’ai dépensé 6000€ de media en 2 mois. 

Le vip est totalement gratuit, si tu veux le rejoindre tu dois OBLIGATOIREMENT créé un compte ici [fans.ly](https://fans.ly)

Une fois que tu as créé le compte fait une capture d’écran et je t’explique la suite ⭐️**

( RÉPOND JUSTE AVEC LE SCREEN POUR QUE JE VOIS RAPIDEMENT TON MESSAGE)''',parse_mode=enums.ParseMode.MARKDOWN)
        # Add the user ID to the set
        users_replied_to.add(user_id)

app.run()
