from pathlib import Path
from dotenv import dotenv_values

print(Path().resolve())

config = dotenv_values(".env")
print(config)
print(config["DOMAIN"])
