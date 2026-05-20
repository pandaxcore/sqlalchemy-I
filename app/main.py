from crud import create_tables, add_data
from database import engine

if __name__ == "__main__":
    with engine.connect() as conn:
        create_tables()