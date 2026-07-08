from backend.database import get_connection
from backend.services.ai_service import extract_search_terms


def search_metadata(user_query):
    """
    Search metadata using AI extracted search terms.
    """

    search_terms = extract_search_terms(user_query)

    conn = get_connection()
    cursor = conn.cursor()

    results = []
    seen = set()

    for keyword in search_terms:

        # ---------- First Search ----------
        cursor.execute(
            """
            SELECT
                database_name,
                table_name,
                column_name,
                data_type
            FROM catalog
            WHERE
                LOWER(database_name) LIKE ?
                OR LOWER(table_name) LIKE ?
                OR LOWER(column_name) LIKE ?
            ORDER BY database_name, table_name
            """,
            (
                f"%{keyword.lower()}%",
                f"%{keyword.lower()}%",
                f"%{keyword.lower()}%"
            )
        )

        rows = cursor.fetchall()

        # ---------- Backup Search ----------
        if not rows:

            words = keyword.split("_")

            for word in words:

                cursor.execute(
                    """
                    SELECT
                        database_name,
                        table_name,
                        column_name,
                        data_type
                    FROM catalog
                    WHERE
                        LOWER(column_name) LIKE ?
                    """,
                    (
                        f"%{word.lower()}%",
                    )
                )

                rows.extend(cursor.fetchall())

        # ---------- Store Results ----------
        for row in rows:

            key = (
                row[0],
                row[1],
                row[2]
            )

            if key not in seen:

                seen.add(key)

                results.append({

                    "database_name": row[0],
                    "table_name": row[1],
                    "column_name": row[2],
                    "data_type": row[3]

                })

    conn.close()

    return results