from crud import create_tables
from database import engine


with engine.connect() as conn:
    create_tables()