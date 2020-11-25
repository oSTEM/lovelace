import importlib
import inspect
import os
import pkgutil

from dotenv import load_dotenv

from bot import exts
from bot.bot import bot

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    for module in pkgutil.walk_packages(exts.__path__, f"{exts.__name__}."):
        if module.ispkg:
            imported = importlib.import_module(module.name)
            if not inspect.isfunction(getattr(imported, "setup", None)):
                # If there's no setup function, we skip it as it's not an extension and will fail to load
                continue
        bot.load_extension(module.name)

    bot.run(TOKEN)
