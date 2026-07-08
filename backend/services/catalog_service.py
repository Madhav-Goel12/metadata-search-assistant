from backend.database import get_connection


def insert_metadata(metadata_records):
    """
    Insert metadata records into the catalog.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO catalog (
            database_name,
            table_name,
            column_name,
            data_type,
            row_count,
            null_count,
            unique_count,
            sample_values,
            min_value,
            max_value,
            memory_usage,
            is_numeric,
            is_datetime,
            file_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [

        (
            m["database_name"],
            m["table_name"],
            m["column_name"],
            m["data_type"],
            m["row_count"],
            m["null_count"],
            m["unique_count"],
            m["sample_values"],
            m["min_value"],
            m["max_value"],
            m["memory_usage"],
            m["is_numeric"],
            m["is_datetime"],
            m["file_path"]
        )

        for m in metadata_records

    ])

    conn.commit()
    conn.close()

def clear_catalog():
    """
    Remove all existing metadata from the catalog.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM catalog")

    conn.commit()
    conn.close()

    print("Catalog cleared successfully.")

def get_statistics():
    """
    Return catalog statistics.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(DISTINCT database_name),
            COUNT(DISTINCT table_name),
            COUNT(*)
        FROM catalog
    """)

    databases, tables, columns = cursor.fetchone()

    conn.close()

    return {
        "databases": databases,
        "tables": tables,
        "columns": columns
    }

def get_all_databases():
    """
    Return all unique database names.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT database_name
        FROM catalog
        ORDER BY database_name
    """)

    databases = [row[0] for row in cursor.fetchall()]

    conn.close()

    return databases

def get_tables(database_name):
    """
    Return all tables for a given database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT table_name
        FROM catalog
        WHERE database_name = ?
        ORDER BY table_name
    """, (database_name,))

    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return tables

def get_columns(table_name):
    """
    Return complete metadata for all columns in a table.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            column_name,
            data_type,
            row_count,
            null_count,
            unique_count,
            sample_values,
            min_value,
            max_value,
            memory_usage,
            is_numeric,
            is_datetime
        FROM catalog
        WHERE table_name = ?
        ORDER BY column_name
    """, (table_name,))

    rows = cursor.fetchall()

    conn.close()

    columns = []

    for row in rows:

        columns.append({
            "column_name": row[0],
            "data_type": row[1],
            "row_count": row[2],
            "null_count": row[3],
            "unique_count": row[4],
            "sample_values": row[5],
            "min_value": row[6],
            "max_value": row[7],
            "memory_usage": row[8],
            "is_numeric": bool(row[9]),
            "is_datetime": bool(row[10])
        })

    return columns