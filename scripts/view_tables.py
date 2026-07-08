import sqlite3
from pathlib import Path

db = Path("metadata") / "metadata.db"

conn = sqlite3.connect(db)

cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

print(cursor.fetchall())

conn.close()