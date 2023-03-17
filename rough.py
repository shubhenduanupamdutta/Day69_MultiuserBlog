from pathlib import Path
from dotenv import load_dotenv
import os
print(Path().resolve())

load_dotenv()
print(os.environ.get("DATABASE_URI"))
print(type(os.environ.get("DATABASE_URI")))


