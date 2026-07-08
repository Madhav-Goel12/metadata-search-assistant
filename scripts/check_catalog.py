from backend.database import get_connection
import pandas as pd

conn = get_connection()

df = pd.read_sql("SELECT * FROM catalog", conn)

print(df.head())

print("\nTotal Records:", len(df))

conn.close()