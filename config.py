import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", ""))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "BQGlhLEARnzKQUO9fhjjo65GWUVbf2OuowzqJYhqZDUclW029UEa4ix4Zl8ejr0pL8jdPkdCxPN8fgWzBxNSBniIGxfiqdvziRNweZ_PlI__1jsEVnD65pgLzdz8-ugPg8W5Fy5AGabAEzZ63AsLCIZk7DerIgcFx_NwEkjJ7y19eRYWybaHdFhVvPhjvVniCIRdVgI6Fc-dc9dztE2ZWRYWKjkb0wgPVRdgJwSRy5AtFmbHyeLfwsvRUkGUmES9jjVxzPZI2lxXu6D_-Rik0ryL0J02LvJoixGwYfXTcV3v3oh6S3jCEEdJtPDHKUsrLWDuRGZ7xcwrqNrIVt7ulkqauJE6FQAAAAGdpDQAAA")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "Anime_Lumino")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002568229104"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://tirokaitube:ymDe3VLWXQ05JazI@cluster0.tktl52k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "tirokaitube")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/PvHsTVXC/x.jpg")
