import sqlite3
from pathlib import Path

# -------------------------------
# Project Paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_DIR = BASE_DIR / "metadata"
DB_PATH = METADATA_DIR / "metadata.db"


# -------------------------------
# Database Connection
# -------------------------------

def get_connection():
    """
    Returns a SQLite connection.
    """

    return sqlite3.connect(DB_PATH)


# -------------------------------
# Create Catalog Table
# -------------------------------

def initialize_database():
    """
    Creates the catalog table if it doesn't exist.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS catalog (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    database_name TEXT NOT NULL,

    table_name TEXT NOT NULL,

    column_name TEXT NOT NULL,

    data_type TEXT,

    row_count INTEGER,

    null_count INTEGER,

    unique_count INTEGER,

    sample_values TEXT,

    min_value TEXT,

    max_value TEXT,

    memory_usage INTEGER,

    is_numeric BOOLEAN,

    is_datetime BOOLEAN,

    file_path TEXT,

    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    """)

    conn.commit()

    conn.close()

    print("✅ Metadata database initialized successfully.")